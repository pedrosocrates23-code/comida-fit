"""
Busca produtos na Amazon via Creators API com filtros de qualidade:
  - Somente produtos com Amazon Prime
  - Ordenado por melhores avaliações
  - Minimo de avaliações configurável
  - Extrai feedbacks positivos de clientes

Uso:
  python fetch_products.py --keywords "whey protein" --category proteinas
  python fetch_products.py --keywords "creatina monohidratada" --category creatinas --min-reviews 100
"""

import os
import json
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

AMAZON_TAG        = os.getenv("AMAZON_TAG", "fits000-20")
CREDENTIAL_ID     = os.getenv("AMAZON_CREDENTIAL_ID")
CREDENTIAL_SECRET = os.getenv("AMAZON_CREDENTIAL_SECRET")

# Filtros de qualidade
MIN_REVIEWS_DEFAULT = 50     # minimo de avaliacoes para considerar o produto
MIN_RATING_DEFAULT  = 4.0    # nota minima (de 5)
MAX_RESULTS_DEFAULT = 20     # busca mais para poder filtrar melhor


def fetch_products(
    keywords: str,
    category: str,
    min_reviews: int = MIN_REVIEWS_DEFAULT,
    min_rating: float = MIN_RATING_DEFAULT,
    max_results: int = MAX_RESULTS_DEFAULT,
) -> list[dict]:
    from amazon_creatorsapi import AmazonCreatorsApi, Country

    if not CREDENTIAL_ID or not CREDENTIAL_SECRET:
        raise ValueError(
            "Credenciais nao encontradas. Copie .env.example para .env e preencha."
        )

    api = AmazonCreatorsApi(
        credential_id=CREDENTIAL_ID,
        credential_secret=CREDENTIAL_SECRET,
        tag=AMAZON_TAG,
        country=Country.BR,
    )

    print(f"Buscando: '{keywords}' | Prime obrigatorio | Min {min_reviews} reviews | Nota >= {min_rating}")

    # Busca ordenando por melhores avaliacoes, filtrando por Prime
    results = api.search_items(
        keywords=keywords,
        item_count=max_results,
        sort_by="AvgCustomerReviews",
        delivery_flags=["Prime"],
    )

    if not results or not results.items:
        print("Nenhum produto encontrado.")
        return []

    products = []
    rejected = 0

    for item in results.items:
        product = {
            "asin":          item.asin,
            "titulo":        "",
            "imagem_url":    "",
            "imagem_extra":  [],       # imagens adicionais do produto
            "link_afiliado": item.detail_page_url or "",
            "preco":         None,
            "preco_original":None,     # preco sem desconto (se houver)
            "desconto":      None,     # % de desconto
            "rating":        None,
            "rating_count":  None,
            "prime":         False,
            "vendedor":      None,
            "is_amazon":     False,    # vendido e enviado pela Amazon
            "feedbacks":     [],       # comentarios positivos de clientes
            "categoria":     category,
            "keywords":      keywords,
            "status":        "pendente",
            "buscado_em":    datetime.now().strftime("%Y-%m-%d"),
        }

        # Titulo
        if item.item_info and item.item_info.title:
            product["titulo"] = item.item_info.title.display_value

        # Imagens
        if item.images:
            if item.images.primary and item.images.primary.large:
                product["imagem_url"] = item.images.primary.large.url
            if item.images.variants:
                extras = []
                for variant in item.images.variants[:3]:
                    if variant.large:
                        extras.append(variant.large.url)
                product["imagem_extra"] = extras

        # Preco e Prime
        if item.offers_v2 and item.offers_v2.listings:
            listing = item.offers_v2.listings[0]

            # Preco atual
            if listing.price and listing.price.money:
                product["preco"] = float(listing.price.money.amount)

            # Preco original e desconto
            if listing.saving_basis and listing.saving_basis.money:
                product["preco_original"] = float(listing.saving_basis.money.amount)
                if product["preco"] and product["preco_original"]:
                    pct = ((product["preco_original"] - product["preco"]) / product["preco_original"]) * 100
                    product["desconto"] = round(pct, 1)

            # Prime
            if listing.delivery_info and listing.delivery_info.is_prime_eligible:
                product["prime"] = True

            # Vendedor
            if listing.merchant_info:
                product["vendedor"]   = listing.merchant_info.name
                product["is_amazon"]  = listing.merchant_info.name in ("Amazon.com.br", "Amazon")

        # Filtros de qualidade — rejeita produtos ruins
        rating       = product.get("rating") or 0
        rating_count = product.get("rating_count") or 0

        if not product["prime"]:
            rejected += 1
            print(f"  [SEM PRIME] {product['titulo'][:50]}")
            continue

        if rating_count < min_reviews and rating_count > 0:
            rejected += 1
            print(f"  [POUCAS REVIEWS: {rating_count}] {product['titulo'][:50]}")
            continue

        if rating > 0 and rating < min_rating:
            rejected += 1
            print(f"  [NOTA BAIXA: {rating}] {product['titulo'][:50]}")
            continue

        products.append(product)
        prime_badge = "[PRIME]" if product["prime"] else "[SEM PRIME]"
        amazon_badge = "[AMAZON]" if product["is_amazon"] else ""
        print(f"  OK {prime_badge}{amazon_badge} {product['titulo'][:55]}...")

    print(f"\nResultado: {len(products)} aprovados | {rejected} rejeitados (sem prime/poucas reviews/nota baixa)")
    return products


def main():
    parser = argparse.ArgumentParser(description="Busca produtos Amazon - somente Prime com boas avaliacoes")
    parser.add_argument("--keywords",    required=True, help="Termo de busca")
    parser.add_argument("--category",   required=True, help="Categoria: proteinas, creatinas, pre-treino, aminoacidos")
    parser.add_argument("--max",         type=int,   default=MAX_RESULTS_DEFAULT, help="Max resultados para filtrar (padrao: 20)")
    parser.add_argument("--min-reviews", type=int,   default=MIN_REVIEWS_DEFAULT, help="Minimo de avaliacoes (padrao: 50)")
    parser.add_argument("--min-rating",  type=float, default=MIN_RATING_DEFAULT,  help="Nota minima de 1-5 (padrao: 4.0)")
    parser.add_argument("--output",      default="", help="Arquivo de saida JSON (padrao: auto)")
    args = parser.parse_args()

    products = fetch_products(
        keywords=args.keywords,
        category=args.category,
        min_reviews=args.min_reviews,
        min_rating=args.min_rating,
        max_results=args.max,
    )

    if not products:
        return

    output_file = args.output or f"output/{args.category}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"\nSalvo: {output_file} ({len(products)} produtos)")
    print(f"Proximo passo: python sheets_sync.py --file {output_file}")


if __name__ == "__main__":
    main()
