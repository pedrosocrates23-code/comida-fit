"""
Crawler Amazon Brasil — sem dependência de API.
Usa Playwright para navegar, buscar e extrair dados reais de produtos.

Estratégia Prime: filtra por Prime diretamente na URL da busca
(&rh=p_85:17314609011) — todos os resultados já são Prime.

Extrai:
  - Título, preço, imagem, link afiliado com tag fits000-20
  - Rating e quantidade de reviews
  - Feedbacks positivos de clientes (da página do produto)

Uso:
  python crawler.py --keywords "whey protein isolado" --category proteinas
  python crawler.py --keywords "creatina monohidratada" --category creatinas --pages 2
  python crawler.py --keywords "pre treino" --category pre-treino --min-reviews 50
"""

import re
import json
import time
import random
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import quote_plus

AMAZON_TAG      = "fits000-20"
AMAZON_BASE_URL = "https://www.amazon.com.br"
PRIME_FILTER    = "p_85:17314609011"   # filtro Prime para Amazon Brasil

MIN_REVIEWS_DEFAULT = 30
MIN_RATING_DEFAULT  = 4.0
MAX_PAGES_DEFAULT   = 2

OUTPUT_DIR = Path(__file__).parent / "output"


def delay(min_s=1.5, max_s=3.0):
    time.sleep(random.uniform(min_s, max_s))


def build_affiliate_link(asin: str) -> str:
    """Constrói link afiliado limpo diretamente pelo ASIN."""
    return f"{AMAZON_BASE_URL}/dp/{asin}?tag={AMAZON_TAG}"


def build_product_url(asin: str) -> str:
    return f"{AMAZON_BASE_URL}/dp/{asin}"


def extract_asin(url: str) -> str:
    m = re.search(r"/dp/([A-Z0-9]{10})", url)
    return m.group(1) if m else ""


def parse_price(text: str) -> float | None:
    text = text.replace("R$", "").replace("\xa0", "").replace(" ", "").replace(".", "").replace(",", ".").strip()
    try:
        v = float(text)
        return v if v > 0 else None
    except ValueError:
        return None


def parse_rating(text: str) -> float | None:
    m = re.search(r"(\d)[,\.](\d)", text)
    if m:
        try:
            return float(f"{m.group(1)}.{m.group(2)}")
        except ValueError:
            pass
    return None


def parse_reviews(text: str) -> int | None:
    text = text.replace(".", "").replace(",", "").strip()
    try:
        v = int(text)
        return v if v > 0 else None
    except ValueError:
        return None


def get_product_details(page, product_url: str) -> dict:
    """
    Acessa a página do produto e extrai:
      - rating_count (total de avaliações)
      - feedbacks positivos (4-5 estrelas)
      - imagens extras
      - vendedor (fulfilled by)
    """
    result = {"rating_count": None, "feedbacks": [], "imagens_extras": [], "vendedor": "", "is_amazon": False}

    try:
        page.goto(product_url, wait_until="domcontentloaded", timeout=20000)
        delay(1.5, 2.5)

        # Total de avaliações — seletor da página do produto
        for sel in [
            "#acrCustomerReviewText",
            "[data-hook='total-review-count']",
            "span[data-hook='total-review-count']",
            "#averageCustomerReviews span.a-size-base",
        ]:
            el = page.query_selector(sel)
            if el:
                text = el.inner_text().replace(".", "").replace(",", "").strip()
                # Remove texto como "avaliações" ou "ratings"
                text = re.sub(r"[^\d]", "", text)
                try:
                    v = int(text)
                    if v > 0:
                        result["rating_count"] = v
                        break
                except ValueError:
                    pass

        # Vendedor
        for sel in ["#merchant-info", "#sellerProfileTriggerId", "#tabular-buybox-truncate-0"]:
            el = page.query_selector(sel)
            if el:
                text = el.inner_text().strip()
                if text:
                    result["vendedor"] = text[:60]
                    result["is_amazon"] = "amazon" in text.lower()
                    break

        # Imagens extras (thumbnails)
        thumbs = page.query_selector_all("#altImages .imageThumbnail img, #altImages img")
        for img in thumbs[:4]:
            src = img.get_attribute("src") or ""
            src = re.sub(r"\._[A-Z]{2}\d+_\.", "._AC_SX450_.", src)
            if src and "sprite" not in src and "transparent" not in src:
                result["imagens_extras"].append(src)

        # Feedbacks positivos (4-5 estrelas)
        reviews = page.query_selector_all("[data-hook='review']")
        for review in reviews[:10]:
            try:
                star_el = review.query_selector("[data-hook='review-star-rating'], [data-hook='cmps-review-star-rating']")
                if not star_el:
                    continue
                rating = parse_rating(star_el.inner_text() or star_el.get_attribute("class") or "")
                if rating and rating >= 4.0:
                    body = review.query_selector("[data-hook='review-body'] span")
                    if body:
                        text = body.inner_text().strip()
                        if 20 < len(text) < 350:
                            result["feedbacks"].append(text)
                            if len(result["feedbacks"]) >= 3:
                                break
            except Exception:
                continue

    except Exception as e:
        print(f"    Aviso produto: {e}")

    return result


def get_extra_images(page) -> list[str]:
    """Coleta imagens adicionais do produto."""
    imgs = []
    try:
        thumbs = page.query_selector_all("#altImages .imageThumbnail img, #altImages img")
        for img in thumbs[:4]:
            src = img.get_attribute("src") or ""
            src = re.sub(r"\._[A-Z]{2}\d+_\.", "._AC_SX450_.", src)
            if src and "sprite" not in src and "transparent-pixel" not in src:
                imgs.append(src)
    except Exception:
        pass
    return imgs


def extract_item(item) -> dict | None:
    """Extrai dados de um item da listagem de resultados."""
    try:
        asin = item.get_attribute("data-asin") or ""

        # Título — h2 > span é o seletor mais estável
        titulo = ""
        for sel in ["h2 span", "h2 a span", ".a-size-base-plus", ".a-size-medium"]:
            el = item.query_selector(sel)
            if el:
                t = el.inner_text().strip()
                if len(t) > 8 and "Patrocinado" not in t:
                    titulo = t
                    break
        if not titulo:
            return None

        # URL do produto
        url_produto = ""
        for sel in ["h2 a[href*='/dp/']", "a[href*='/dp/']"]:
            el = item.query_selector(sel)
            if el:
                href = el.get_attribute("href") or ""
                if href.startswith("/"):
                    href = AMAZON_BASE_URL + href
                url_produto = href
                break

        if not asin and url_produto:
            asin = extract_asin(url_produto)
        if not asin:
            return None

        # Imagem — pega URL completa e substitui tamanho pelo maior disponível
        imagem_url = ""
        img = item.query_selector("img.s-image")
        if img:
            src = img.get_attribute("src") or ""
            # Substitui qualquer dimensão Amazon pelo tamanho 450px
            src = re.sub(r"\._AC_U[LY]\d+_\.", "._AC_SX450_.", src)
            src = re.sub(r"\._[A-Z]{2}\d+_\.", "._AC_SX450_.", src)
            imagem_url = src

        # Preço
        preco = None
        preco_original = None
        desconto = None

        for sel in [
            ".a-price[data-a-color='base'] .a-offscreen",
            ".a-price .a-offscreen",
            "[data-cy='price-recipe'] .a-offscreen",
        ]:
            el = item.query_selector(sel)
            if el:
                v = parse_price(el.inner_text())
                if v:
                    preco = v
                    break

        el_orig = item.query_selector(".a-price[data-a-color='secondary'] .a-offscreen")
        if el_orig:
            v = parse_price(el_orig.inner_text())
            if v:
                preco_original = v

        if preco and preco_original and preco_original > preco:
            desconto = round(((preco_original - preco) / preco_original) * 100, 1)

        # Rating
        rating = None
        for sel in [".a-icon-alt", "span[aria-label*='estrela']", "i[class*='a-icon-star'] + span"]:
            el = item.query_selector(sel)
            if el:
                text = el.inner_text() or el.get_attribute("aria-label") or ""
                v = parse_rating(text)
                if v:
                    rating = v
                    break

        # Reviews — Amazon BR usa formato "9.982" (ponto como milhar)
        rating_count = None
        for sel in [
            "span.a-size-base.s-underline-text",
            "[data-cy='reviews-block'] .a-size-base",
            "a[href*='customerReviews'] span.a-size-base",
            ".a-row .a-link-normal span.a-size-base",
        ]:
            el = item.query_selector(sel)
            if el:
                text = el.inner_text().strip()
                # Remove ponto de milhar BR (9.982 → 9982)
                text = text.replace(".", "").replace(",", "")
                try:
                    v = int(text)
                    if v > 0:
                        rating_count = v
                        break
                except ValueError:
                    pass

        # URL do produto e link afiliado construídos pelo ASIN
        url_produto    = build_product_url(asin)
        link_afiliado  = build_affiliate_link(asin)

        return {
            "asin":           asin,
            "titulo":         titulo,
            "imagem_url":     imagem_url,
            "imagens_extras": [],
            "url_produto":    url_produto,
            "link_afiliado":  link_afiliado,
            "preco":          preco,
            "preco_original": preco_original,
            "desconto":       desconto,
            "rating":         rating,
            "rating_count":   rating_count,
            "prime":          True,   # garantido pelo filtro da URL
            "vendedor":       "",
            "is_amazon":      False,
            "feedbacks":      [],
        }
    except Exception as e:
        print(f"    Erro ao extrair item: {e}")
        return None


def crawl(keywords: str, category: str, min_reviews: int, min_rating: float, max_pages: int) -> list[dict]:
    from playwright.sync_api import sync_playwright

    products = []
    seen_asins: set[str] = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled", "--start-maximized"],
        )
        ctx = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1366, "height": 768},
            locale="pt-BR",
            extra_http_headers={"Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"},
        )
        ctx.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            window.chrome = { runtime: {} };
        """)

        main_page = ctx.new_page()

        # Visita a home antes para parecer usuário real
        main_page.goto(AMAZON_BASE_URL, wait_until="domcontentloaded", timeout=20000)
        delay(2, 3)

        for page_num in range(1, max_pages + 1):
            # URL com filtro Prime embutido e ordenação por reviews
            url = (
                f"{AMAZON_BASE_URL}/s"
                f"?k={quote_plus(keywords)}"
                f"&rh={quote_plus(PRIME_FILTER)}"
                f"&sort=review-rank"
                f"&page={page_num}"
            )

            print(f"\nPagina {page_num}/{max_pages}: {keywords} [Prime]")
            main_page.goto(url, wait_until="domcontentloaded", timeout=30000)
            delay(2, 3)

            # Scroll para carregar lazy content
            for _ in range(4):
                main_page.evaluate("window.scrollBy(0, 600)")
                delay(0.5, 0.8)
            main_page.evaluate("window.scrollTo(0, 0)")
            delay(1, 1.5)

            # CAPTCHA check
            if "captcha" in main_page.url.lower() or main_page.query_selector("form[action*='captcha']"):
                print("  CAPTCHA — aguarde e pressione Enter no terminal...")
                input("  Resolva o CAPTCHA no browser e pressione Enter para continuar...")

            items = main_page.query_selector_all("[data-component-type='s-search-result']")
            print(f"  {len(items)} itens encontrados")

            for item in items:
                try:
                    p_data = extract_item(item)
                    if not p_data:
                        continue
                    if p_data["asin"] in seen_asins:
                        continue

                    # Filtros de qualidade
                    rc = p_data["rating_count"] or 0
                    rt = p_data["rating"] or 0

                    if rc and rc < min_reviews:
                        print(f"  [POUCAS REVIEWS: {rc}] {p_data['titulo'][:45]}")
                        continue
                    if rt and rt < min_rating:
                        print(f"  [NOTA BAIXA: {rt}] {p_data['titulo'][:45]}")
                        continue

                    # Vai para a página do produto — pega reviews, feedbacks, imagens, vendedor
                    print(f"  Coletando detalhes: {p_data['titulo'][:50]}...")
                    detail_page = ctx.new_page()
                    details = get_product_details(detail_page, p_data["url_produto"])
                    detail_page.close()

                    # Usa rating_count da página do produto se não veio da listagem
                    if not p_data["rating_count"] and details["rating_count"]:
                        p_data["rating_count"] = details["rating_count"]
                    p_data["imagens_extras"] = details["imagens_extras"]
                    p_data["feedbacks"]      = details["feedbacks"]
                    p_data["vendedor"]       = details["vendedor"]
                    p_data["is_amazon"]      = details["is_amazon"]
                    delay(1, 2)

                    # Adiciona metadados finais
                    p_data.update({
                        "categoria":  category,
                        "keywords":   keywords,
                        "status":     "pendente",
                        "buscado_em": datetime.now().strftime("%Y-%m-%d"),
                    })

                    products.append(p_data)
                    seen_asins.add(p_data["asin"])

                    stars = f"{p_data['rating']}*" if p_data['rating'] else "?"
                    rc_str = str(p_data['rating_count']) if p_data['rating_count'] else "?"
                    print(f"  COLETADO [{stars} | {rc_str} reviews] {p_data['titulo'][:50]}")

                except Exception as e:
                    print(f"  Erro: {e}")
                    continue

            delay(2, 4)

        browser.close()

    return products


def main():
    parser = argparse.ArgumentParser(description="Crawler Amazon Brasil — Prime obrigatorio")
    parser.add_argument("--keywords",    required=True)
    parser.add_argument("--category",   required=True, help="proteinas, creatinas, pre-treino, aminoacidos")
    parser.add_argument("--pages",       type=int,   default=MAX_PAGES_DEFAULT)
    parser.add_argument("--min-reviews", type=int,   default=MIN_REVIEWS_DEFAULT)
    parser.add_argument("--min-rating",  type=float, default=MIN_RATING_DEFAULT)
    parser.add_argument("--output",      default="")
    args = parser.parse_args()

    print(f"Crawler: '{args.keywords}'")
    print(f"Filtros: Prime | Min {args.min_reviews} reviews | Nota >= {args.min_rating} | {args.pages} paginas")

    products = crawl(
        keywords=args.keywords,
        category=args.category,
        min_reviews=args.min_reviews,
        min_rating=args.min_rating,
        max_pages=args.pages,
    )

    if not products:
        print("\nNenhum produto encontrado. Tente reduzir --min-reviews.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = args.output or str(OUTPUT_DIR / f"{args.category}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

    with open(out, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"\n{len(products)} produtos -> {out}")
    print(f"Proximo: python sheets_sync.py --file {out}")


if __name__ == "__main__":
    main()
