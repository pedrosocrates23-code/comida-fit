"""
Lê produtos aprovados no Google Sheets, baixa imagens e gera JSON estruturado
para ser consumido pelo generate_content.py.

Uso:
  python extract_approved.py
  python extract_approved.py --category proteinas
"""

import os
import json
import argparse
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

import gspread
from google.oauth2.service_account import Credentials

load_dotenv(Path(__file__).parent / ".env")

SHEET_ID   = os.getenv("GOOGLE_SHEETS_ID")
SA_FILE    = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", "service_account.json")
SHEET_NAME = "Produtos"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Onde salvar as imagens no projeto Astro
PROJECT_ROOT = Path(__file__).parent.parent.parent
IMAGES_DIR   = PROJECT_ROOT / "public" / "afiliados" / "images"
OUTPUT_DIR   = Path(__file__).parent / "output"


def get_worksheet() -> gspread.Worksheet:
    sa_path = Path(__file__).parent / SA_FILE
    creds   = Credentials.from_service_account_file(str(sa_path), scopes=SCOPES)
    client  = gspread.authorize(creds)

    if SHEET_ID:
        spreadsheet = client.open_by_key(SHEET_ID)
    else:
        spreadsheet = client.open("Afiliados - Receitas Fit")

    return spreadsheet.worksheet(SHEET_NAME)


def download_image(url: str, asin: str) -> str:
    """Baixa imagem da Amazon e salva localmente. Retorna caminho público."""
    if not url:
        return ""

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    ext      = ".jpg"
    filename = f"{asin}{ext}"
    filepath = IMAGES_DIR / filename

    if filepath.exists():
        return f"/afiliados/images/{filename}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"  ↓ Imagem salva: {filename}")
        return f"/afiliados/images/{filename}"
    except Exception as e:
        print(f"  ⚠️  Falha ao baixar imagem {asin}: {e}")
        return url


def parse_row(headers: list[str], row: list[str]) -> dict:
    """Converte uma linha da planilha em dict."""
    d = dict(zip(headers, row + [""] * (len(headers) - len(row))))
    return {
        "asin":          d.get("ASIN", "").strip(),
        "titulo":        d.get("Título", "").strip(),
        "preco":         float(d["Preço (R$)"]) if d.get("Preço (R$)") else None,
        "imagem_url":    d.get("Imagem URL", "").strip(),
        "link_afiliado": d.get("Link Afiliado", "").strip(),
        "rating":        float(d["Rating"]) if d.get("Rating") else None,
        "rating_count":  int(d["Avaliações"]) if d.get("Avaliações") else None,
        "vendedor":      d.get("Vendedor", "").strip(),
        "categoria":     d.get("Categoria", "").strip(),
        "keywords":      d.get("Keywords", "").strip(),
        "status":        d.get("Status", "").strip(),
    }


def main():
    parser = argparse.ArgumentParser(description="Extrai aprovados do Google Sheets")
    parser.add_argument("--category", default="", help="Filtrar por categoria (opcional)")
    parser.add_argument("--no-images", action="store_true", help="Não baixar imagens")
    args = parser.parse_args()

    print("Conectando ao Google Sheets...")
    ws         = get_worksheet()
    all_values = ws.get_all_values()

    if len(all_values) < 2:
        print("Planilha vazia.")
        return

    headers  = all_values[0]
    rows     = all_values[1:]
    products = [parse_row(headers, row) for row in rows]

    # Filtra aprovados
    approved = [p for p in products if p["status"] == "aprovado"]
    if args.category:
        approved = [p for p in approved if p["categoria"] == args.category]

    if not approved:
        print("Nenhum produto aprovado encontrado.")
        return

    print(f"\n{len(approved)} produto(s) aprovado(s) encontrado(s).")

    # Baixa imagens e substitui URLs
    if not args.no_images:
        print("Baixando imagens...")
        for p in approved:
            if p["imagem_url"]:
                p["imagem_local"] = download_image(p["imagem_url"], p["asin"])
            else:
                p["imagem_local"] = ""

    # Agrupa por categoria
    by_category: dict[str, list] = {}
    for p in approved:
        cat = p["categoria"] or "suplementos"
        by_category.setdefault(cat, []).append(p)

    # Salva JSON por categoria
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for cat, items in by_category.items():
        out_file = OUTPUT_DIR / f"approved_{cat}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
        print(f"✅ {cat}: {len(items)} produto(s) → {out_file.name}")

    print(f"\nPróximo passo: python generate_content.py")


if __name__ == "__main__":
    main()
