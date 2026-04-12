"""
Gera arquivos markdown para src/content/afiliados/ a partir dos JSONs aprovados.
Cria o frontmatter completo — o conteúdo de texto é gerado pelo agente AIOX @affiliate.

Uso:
  python generate_content.py                          # processa todos os JSONs em output/
  python generate_content.py --category proteinas     # só uma categoria
  python generate_content.py --tipo comparativo       # tipo de página
"""

import os
import json
import argparse
import re
from pathlib import Path
from datetime import date

PROJECT_ROOT  = Path(__file__).parent.parent.parent
CONTENT_DIR   = PROJECT_ROOT / "src" / "content" / "afiliados"
OUTPUT_DIR    = Path(__file__).parent / "output"

CATEGORIA_LABELS = {
    "proteinas":   "Proteínas",
    "creatinas":   "Creatinas",
    "pre-treino":  "Pré-Treino",
    "aminoacidos": "Aminoácidos",
    "vitaminas":   "Vitaminas e Minerais",
    "termogenicos":"Termogênicos",
    "suplementos": "Suplementos",
}

TIPO_LABELS = {
    "comparativo": "Comparativo",
    "review":      "Review",
    "top-lista":   "Top Lista",
}


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[áàãâä]", "a", text)
    text = re.sub(r"[éèêë]", "e", text)
    text = re.sub(r"[íìîï]", "i", text)
    text = re.sub(r"[óòõôö]", "o", text)
    text = re.sub(r"[úùûü]", "u", text)
    text = re.sub(r"[ç]", "c", text)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text.strip())
    return text


def format_price(preco) -> str:
    if preco is None:
        return ""
    return f"R$ {preco:.2f}".replace(".", ",")


def build_product_section(p: dict, rank: int) -> str:
    """Gera seção markdown de um produto individual."""
    rating       = p.get("rating") or 0
    rating_count = p.get("rating_count") or 0
    stars_full   = int(rating)
    stars_str    = "★" * stars_full + "☆" * (5 - stars_full)
    rating_str   = f"{stars_str} {rating}/5 ({rating_count:,} avaliações)".replace(",", ".") if rating else ""

    preco_str    = format_price(p.get("preco"))
    preco_orig   = format_price(p.get("preco_original"))
    desconto     = p.get("desconto")
    imagem       = p.get("imagem_local") or p.get("imagem_url", "")
    link         = p.get("link_afiliado", "")
    titulo       = p.get("titulo", "Produto")
    vendedor     = p.get("vendedor", "")
    prime        = p.get("prime", False)
    is_amazon    = p.get("is_amazon", False)
    destaque_str = " — **Melhor Escolha**" if rank == 1 else ""

    # Badges
    badges = []
    if prime:
        badges.append("🔵 **Prime**")
    if is_amazon:
        badges.append("✅ **Vendido pela Amazon**")
    if desconto and desconto >= 10:
        badges.append(f"🏷️ **{desconto:.0f}% OFF**")
    badges_str = "  ".join(badges)

    # Preco com desconto
    preco_display = preco_str
    if preco_orig and desconto:
        preco_display = f"~~{preco_orig}~~ **{preco_str}** ({desconto:.0f}% OFF)"

    pros_list     = "\n".join(f"- {pro}" for pro in (p.get("pros") or []))
    contras_list  = "\n".join(f"- {c}" for c in (p.get("contras") or []))

    # Feedbacks de clientes
    feedbacks     = p.get("feedbacks") or []
    feedback_section = ""
    if feedbacks:
        feedback_section = "\n**O que dizem os clientes:**\n\n"
        for fb in feedbacks[:3]:
            feedback_section += f'> *"{fb}"*\n\n'

    section = f"""### {rank}. {titulo}{destaque_str}

{"![" + titulo + "](" + imagem + ")" if imagem else ""}

{badges_str}

| | |
|---|---|
| **Preço** | {preco_display} |
| **Avaliação** | {rating_str} |
| **Vendedor** | {vendedor} |

<!-- AIOX @affiliate: Escreva 2-3 paragrafos sobre este produto. Destaque beneficios, para quem e indicado e diferenciais. Publico: pessoas que treinam e querem suplementar com segurança. -->

{("**Prós:**\n" + pros_list) if pros_list else ""}

{("**Contras:**\n" + contras_list) if contras_list else ""}
{feedback_section}
<a href="{link}" target="_blank" rel="noopener sponsored" class="btn-afiliado">
  Ver preço na Amazon →
</a>

---
"""
    return section


def build_frontmatter(products: list[dict], categoria: str, tipo: str) -> str:
    cat_label = CATEGORIA_LABELS.get(categoria, categoria.title())
    today     = date.today().isoformat()

    # Produto destaque (primeiro da lista)
    cover_image = ""
    if products:
        cover_image = products[0].get("imagem_local") or products[0].get("imagem_url", "")

    # Keywords automáticas
    keywords = list({
        *[p.get("keywords", "") for p in products],
        categoria,
        "suplementos fitness",
        "amazon",
    })
    keywords_str = "\n".join(f'  - "{k}"' for k in keywords if k)

    # Lista de produtos para o frontmatter
    produtos_yaml = ""
    for p in products:
        imagem = p.get("imagem_local") or p.get("imagem_url", "")
        produtos_yaml += f"""  - asin: "{p.get('asin', '')}"
    titulo: "{p.get('titulo', '').replace('"', "'")}"
    imagem: "{imagem}"
    preco: {p.get('preco') or 'null'}
    rating: {p.get('rating') or 'null'}
    ratingCount: {p.get('rating_count') or 'null'}
    link: "{p.get('link_afiliado', '')}"
    vendedor: "{p.get('vendedor', '')}"
    destaque: {str(products.index(p) == 0).lower()}
"""

    title = f"Melhores {cat_label} 2025: {TIPO_LABELS.get(tipo, 'Comparativo')} Completo"
    desc  = f"Compare os melhores produtos de {cat_label.lower()} com avaliações reais, preços atualizados e links diretos para a Amazon."

    return f"""---
title: "{title}"
description: "{desc}"
publishDate: {today}
categoria: {categoria}
tipo: {tipo}
image: "{cover_image}"
imageAlt: "Melhores {cat_label} - Comparativo"
keywords:
{keywords_str}
featured: false
produtos:
{produtos_yaml}---
"""


def generate_page(products: list[dict], categoria: str, tipo: str) -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    slug     = f"melhores-{slugify(CATEGORIA_LABELS.get(categoria, categoria))}-{date.today().year}"
    filepath = CONTENT_DIR / f"{slug}.md"

    frontmatter = build_frontmatter(products, categoria, tipo)

    cat_label = CATEGORIA_LABELS.get(categoria, categoria.title())
    body = f"""
<!-- AIOX @affiliate: Escreva uma introdução de 3-4 parágrafos sobre {cat_label} para o público fit -->
<!-- Inclua: benefícios, quando usar, o que considerar na hora de comprar -->

## Como Escolhemos os Melhores {cat_label}

<!-- AIOX @affiliate: Explique os critérios de seleção (qualidade, preço, avaliações, marca) -->

## Tabela Comparativa

| Produto | Preço | Avaliação | Vendedor |
|---------|-------|-----------|----------|
"""

    for i, p in enumerate(products, 1):
        preco = format_price(p.get("preco"))
        rating = p.get("rating", "")
        body += f"| {p.get('titulo', '')[:40]}... | {preco} | {rating} | {p.get('vendedor', '')} |\n"

    body += "\n## Análise Detalhada\n\n"
    for i, p in enumerate(products, 1):
        body += build_product_section(p, i)

    body += """
## Perguntas Frequentes

<!-- AIOX @affiliate: Escreva 3-5 FAQs sobre este tipo de suplemento -->

## Conclusão

<!-- AIOX @affiliate: Escreva conclusão de 2 parágrafos com recomendação final -->
"""

    content = frontmatter + body

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Página gerada: src/content/afiliados/{filepath.name}")
    print(f"   {len(products)} produtos | Tipo: {tipo}")


def main():
    parser = argparse.ArgumentParser(description="Gera páginas de afiliados em Markdown")
    parser.add_argument("--category", default="", help="Filtrar por categoria")
    parser.add_argument("--tipo",     default="comparativo", choices=["comparativo", "review", "top-lista"])
    args = parser.parse_args()

    json_files = list(OUTPUT_DIR.glob("approved_*.json"))
    if args.category:
        json_files = [f for f in json_files if f.stem == f"approved_{args.category}"]

    if not json_files:
        print("Nenhum arquivo approved_*.json encontrado em output/")
        print("Execute primeiro: python extract_approved.py")
        return

    for json_file in json_files:
        with open(json_file, encoding="utf-8") as f:
            products = json.load(f)

        if not products:
            continue

        categoria = json_file.stem.replace("approved_", "")
        print(f"\nProcessando: {categoria} ({len(products)} produtos)...")
        generate_page(products, categoria, args.tipo)

    print("\n🎯 Conteúdo gerado! Próximo passo:")
    print("   Abra os arquivos em src/content/afiliados/ e preencha os comentários")
    print("   <!-- AIOX @affiliate: ... --> com o agente de conteúdo.")


if __name__ == "__main__":
    main()
