"""
Orquestrador completo: crawl → approve → imagens → conteúdo
Gera 5 artigos de afiliados prontos para publicar.

Uso:
  python run_all.py
"""

import json
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime

BASE_DIR    = Path(__file__).parent
OUTPUT_DIR  = BASE_DIR / "output"
PROJECT_ROOT = BASE_DIR.parent.parent

# ─── 5 artigos × 5 produtos ──────────────────────────────────────────────────
ARTICLES = [
    {
        "slug":     "proteinas",
        "title":    "Melhores Whey Protein 2025",
        "searches": [
            {"keywords": "whey protein isolado", "pages": 3},
            {"keywords": "whey protein concentrado", "pages": 2},
        ],
    },
    {
        "slug":     "creatinas",
        "title":    "Melhores Creatinas 2025",
        "searches": [
            {"keywords": "creatina monohidratada pura", "pages": 3},
            {"keywords": "creatina creapure", "pages": 2},
        ],
    },
    {
        "slug":     "pre-treino",
        "title":    "Melhores Pré-Treinos 2025",
        "searches": [
            {"keywords": "pre treino termogenico", "pages": 3},
            {"keywords": "pre workout energia", "pages": 2},
        ],
    },
    {
        "slug":     "aminoacidos",
        "title":    "Melhores BCAAs e Aminoácidos 2025",
        "searches": [
            {"keywords": "bcaa aminoacidos essenciais", "pages": 3},
            {"keywords": "glutamina aminoacidos", "pages": 2},
        ],
    },
    {
        "slug":     "vitaminas",
        "title":    "Melhores Vitaminas para Atletas 2025",
        "searches": [
            {"keywords": "vitamina d3 k2 atleta", "pages": 3},
            {"keywords": "multivitaminico fitness", "pages": 2},
        ],
    },
]

MIN_ITEMS_PER_ARTICLE = 5


def run_crawler(keywords: str, category: str, pages: int) -> list[dict]:
    """Executa o crawler e retorna os produtos coletados."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = str(OUTPUT_DIR / f"{category}_{timestamp}.json")

    cmd = [
        sys.executable, str(BASE_DIR / "crawler.py"),
        "--keywords",    keywords,
        "--category",    category,
        "--pages",       str(pages),
        "--min-reviews", "10",
        "--min-rating",  "4.0",
        "--output",      out_file,
    ]

    print(f"\n  Buscando: '{keywords}' ({pages} paginas)...")
    result = subprocess.run(cmd, capture_output=False, text=True)

    if Path(out_file).exists():
        with open(out_file, encoding="utf-8") as f:
            products = json.load(f)
        print(f"  -> {len(products)} produtos coletados")
        return products

    return []


def auto_approve(products: list[dict]) -> list[dict]:
    """Marca todos como aprovados para publicação imediata."""
    for p in products:
        p["status"] = "aprovado"
    return products


def sync_to_sheets(products: list[dict], category: str) -> None:
    """Sincroniza produtos aprovados para o Google Sheets."""
    import gspread
    from google.oauth2.service_account import Credentials

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds  = Credentials.from_service_account_file(str(BASE_DIR / "service_account.json"), scopes=SCOPES)
    client = gspread.authorize(creds)

    import os
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / ".env")
    sheet_id = os.getenv("GOOGLE_SHEETS_ID")

    spreadsheet = client.open_by_key(sheet_id)
    try:
        ws = spreadsheet.worksheet("Produtos")
    except Exception:
        ws = spreadsheet.add_worksheet("Produtos", 1000, 20)
        ws.append_row(["ASIN","Titulo","Preco","Imagem","Link Afiliado","Rating","Reviews",
                       "Prime","Amazon","Vendedor","Feedbacks","Categoria","Status","Data"])

    all_values = ws.get_all_values()
    existing   = {row[0] for row in all_values[1:] if row} if len(all_values) > 1 else set()

    rows = []
    for p in products:
        if p["asin"] in existing:
            continue
        rows.append([
            p.get("asin",""), p.get("titulo",""), p.get("preco",""),
            p.get("imagem_url",""), p.get("link_afiliado",""),
            p.get("rating",""), p.get("rating_count",""),
            "Sim" if p.get("prime") else "Nao",
            "Sim" if p.get("is_amazon") else "Nao",
            p.get("vendedor",""),
            " | ".join(p.get("feedbacks") or []),
            p.get("categoria",""), p.get("status","aprovado"),
            p.get("buscado_em",""),
        ])

    if rows:
        ws.append_rows(rows, value_input_option="USER_ENTERED")
        print(f"  Sheets: {len(rows)} produto(s) adicionados")


def download_image(url: str, asin: str) -> str:
    """Baixa imagem e retorna path local."""
    import requests
    images_dir = PROJECT_ROOT / "public" / "afiliados" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{asin}.jpg"
    filepath = images_dir / filename

    if filepath.exists():
        return f"/afiliados/images/{filename}"

    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        filepath.write_bytes(r.content)
        return f"/afiliados/images/{filename}"
    except Exception as e:
        print(f"    Falha imagem {asin}: {e}")
        return url


def generate_markdown(article: dict, products: list[dict]) -> str:
    """Gera o arquivo markdown do artigo."""
    import re
    from datetime import date

    slug      = article["slug"]
    title     = article["title"]
    today     = date.today().isoformat()

    # Pega imagem de capa do produto destaque
    cover = products[0].get("imagem_local") or products[0].get("imagem_url", "")

    # Monta lista de produtos no frontmatter
    produtos_yaml = ""
    for p in products:
        img = p.get("imagem_local") or p.get("imagem_url", "")
        titulo_safe = p.get("titulo","").replace('"',"'")[:100]
        vend = p.get("vendedor","").replace('"',"'")[:60]
        produtos_yaml += f"""  - asin: "{p.get('asin','')}"
    titulo: "{titulo_safe}"
    imagem: "{img}"
    preco: {p.get('preco') or 'null'}
    rating: {p.get('rating') or 'null'}
    ratingCount: {p.get('rating_count') or 'null'}
    link: "{p.get('link_afiliado','')}"
    vendedor: "{vend}"
    destaque: {str(products.index(p) == 0).lower()}
"""

    keywords_str = "\n".join(f'  - "{k}"' for k in [
        slug, "suplementos fitness", "amazon brasil", "prime",
        "melhor custo beneficio", "suplemento para treino"
    ])

    desc = f"Compare os {len(products)} melhores produtos de {slug.replace('-',' ')} com avaliações reais, preços atualizados e entrega Prime pela Amazon."

    frontmatter = f"""---
title: "{title}: Comparativo com os {len(products)} Melhores"
description: "{desc}"
publishDate: {today}
categoria: {slug}
tipo: comparativo
image: "{cover}"
imageAlt: "{title}"
keywords:
{keywords_str}
featured: false
produtos:
{produtos_yaml}---
"""

    # ── Corpo do artigo ──────────────────────────────────────────────────────
    intro_placeholder = f"<!-- AIOX @affiliate: Escreva uma introdução envolvente (3 parágrafos) sobre {slug.replace('-',' ')} para praticantes de musculação e fitness. Inclua benefícios comprovados, quando usar e o que considerar na compra. Tom: especialista amigável. -->"

    criterios_placeholder = "<!-- AIOX @affiliate: Explique em 2 parágrafos os critérios usados para selecionar estes produtos: certificação, qualidade, custo-benefício, avaliações de clientes reais e entrega Prime. -->"

    # Tabela comparativa
    tabela = "## Tabela Comparativa Rápida\n\n"
    tabela += "| # | Produto | Preço | Avaliação | Reviews |\n"
    tabela += "|---|---------|-------|-----------|--------|\n"
    for i, p in enumerate(products, 1):
        preco  = f"R$ {p['preco']:.2f}".replace(".",",") if p.get("preco") else "-"
        rating = f"{p['rating']}/5" if p.get("rating") else "-"
        rc     = f"{p['rating_count']:,}".replace(",",".") if p.get("rating_count") else "-"
        titulo_curto = p.get("titulo","")[:45]
        tabela += f"| {i} | {titulo_curto}... | {preco} | {rating} | {rc} |\n"

    # Seções individuais dos produtos
    secoes = "\n## Análise Detalhada de Cada Produto\n\n"
    for i, p in enumerate(products, 1):
        img        = p.get("imagem_local") or p.get("imagem_url","")
        titulo     = p.get("titulo","Produto")
        preco_str  = f"R$ {p['preco']:.2f}".replace(".",",") if p.get("preco") else "Ver na Amazon"
        rating     = p.get("rating","")
        rc         = p.get("rating_count","")
        link       = p.get("link_afiliado","")
        vendedor   = p.get("vendedor","")
        destaque   = " — **Melhor Escolha**" if i == 1 else ""
        stars      = "★" * int(rating or 0) + "☆" * (5 - int(rating or 0))
        feedbacks  = p.get("feedbacks") or []

        secoes += f"### {i}. {titulo}{destaque}\n\n"
        if img:
            secoes += f"![{titulo[:50]}]({img})\n\n"

        if i == 1:
            secoes += "🏆 **Melhor Custo-Benefício**  \n"
        if p.get("prime"):
            secoes += "🔵 **Amazon Prime** — Entrega rápida  \n"
        secoes += "\n"

        secoes += f"| | |\n|---|---|\n"
        secoes += f"| **Preço** | **{preco_str}** |\n"
        secoes += f"| **Avaliação** | {stars} {rating}/5 |\n"
        secoes += f"| **Avaliações** | {rc} clientes |\n"
        if vendedor:
            secoes += f"| **Vendedor** | {vendedor} |\n"
        secoes += "\n"

        secoes += f"<!-- AIOX @affiliate: Escreva 2-3 parágrafos sobre este produto. Destaque: para quem é indicado, benefícios principais, diferencial em relação aos concorrentes. Produto: '{titulo[:60]}' -->\n\n"

        if feedbacks:
            secoes += "**O que dizem os compradores:**\n\n"
            for fb in feedbacks[:3]:
                secoes += f'> *"{fb}"*\n\n'

        secoes += f'<a href="{link}" target="_blank" rel="noopener sponsored" class="btn-afiliado">Ver preço na Amazon →</a>\n\n---\n\n'

    faq_placeholder = f"<!-- AIOX @affiliate: Escreva 5 perguntas e respostas frequentes sobre {slug.replace('-',' ')}. Formato: ### Pergunta? / Resposta em 2-3 frases. Perguntas comuns de quem está comprando pela primeira vez. -->"

    conclusao_placeholder = f"<!-- AIOX @affiliate: Escreva uma conclusão de 2 parágrafos. Recomende o produto #1 como melhor escolha geral e mencione alternativas para diferentes perfis (iniciante, avançado, maior orçamento). Call-to-action para ver na Amazon. -->"

    body = f"""
{intro_placeholder}

{tabela}

{criterios_placeholder}

{secoes}

## Perguntas Frequentes

{faq_placeholder}

## Conclusão

{conclusao_placeholder}

*Links com tag de afiliado `fits000-20` — ao comprar pelos links você apoia o blog sem pagar nada a mais.*
"""

    return frontmatter + body


def main():
    print("=" * 60)
    print("ORQUESTRADOR AFILIADOS — Receitas Fit")
    print(f"Meta: 5 artigos x {MIN_ITEMS_PER_ARTICLE} produtos")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    content_dir = PROJECT_ROOT / "src" / "content" / "afiliados"
    content_dir.mkdir(parents=True, exist_ok=True)

    articles_generated = []

    for article in ARTICLES:
        slug = article["slug"]
        print(f"\n{'='*50}")
        print(f"ARTIGO: {article['title']}")
        print(f"{'='*50}")

        # ── 1. Crawl ────────────────────────────────────────────
        all_products: list[dict] = []
        seen_asins: set[str] = set()

        for search in article["searches"]:
            if len(all_products) >= MIN_ITEMS_PER_ARTICLE * 2:
                break
            products = run_crawler(search["keywords"], slug, search["pages"])
            for p in products:
                if p["asin"] not in seen_asins:
                    all_products.append(p)
                    seen_asins.add(p["asin"])

        if len(all_products) < MIN_ITEMS_PER_ARTICLE:
            print(f"  AVISO: Apenas {len(all_products)} produto(s) coletados (meta: {MIN_ITEMS_PER_ARTICLE})")
            if not all_products:
                print(f"  Pulando artigo {slug}")
                continue

        # Limita a 7 produtos por artigo (foco e qualidade)
        all_products = all_products[:7]

        # ── 2. Auto-aprova ──────────────────────────────────────
        all_products = auto_approve(all_products)
        print(f"\n  {len(all_products)} produtos aprovados automaticamente")

        # ── 3. Sincroniza para Sheets ───────────────────────────
        try:
            sync_to_sheets(all_products, slug)
        except Exception as e:
            print(f"  Aviso Sheets: {e}")

        # ── 4. Baixa imagens ────────────────────────────────────
        print("  Baixando imagens...")
        for p in all_products:
            if p.get("imagem_url"):
                p["imagem_local"] = download_image(p["imagem_url"], p["asin"])
            else:
                p["imagem_local"] = ""

        # ── 5. Gera markdown ────────────────────────────────────
        md = generate_markdown(article, all_products)

        from datetime import date
        filename = f"melhores-{slug}-{date.today().year}.md"
        filepath = content_dir / filename
        filepath.write_text(md, encoding="utf-8")

        print(f"\n  ARTIGO GERADO: src/content/afiliados/{filename}")
        print(f"  Produtos: {len(all_products)} | Feedbacks: {sum(len(p.get('feedbacks') or []) for p in all_products)}")
        articles_generated.append(filename)

        # Pausa entre artigos para não ser bloqueado
        if article != ARTICLES[-1]:
            print("\n  Pausa 5s antes do proximo artigo...")
            time.sleep(5)

    # ── Resultado final ─────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"CONCLUIDO: {len(articles_generated)} artigos gerados")
    for f in articles_generated:
        print(f"  src/content/afiliados/{f}")
    print(f"\nProximos passos:")
    print(f"  1. Abra os arquivos e preencha os comentários <!-- AIOX @affiliate: ... -->")
    print(f"  2. Ou use o agente @affiliate para gerar os textos automaticamente")
    print(f"  3. Execute: npm run build")


if __name__ == "__main__":
    main()
