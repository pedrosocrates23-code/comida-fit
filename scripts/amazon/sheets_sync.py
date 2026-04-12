"""
Sincroniza produtos do JSON para o Google Sheets.
Cria a planilha automaticamente se não existir.

Uso:
  python sheets_sync.py --file output/proteinas_20240101.json
  python sheets_sync.py --file output/creatinas_20240101.json --sheet "Afiliados Suplementos"

Estrutura da planilha:
  Aba "Produtos" — todos os produtos buscados
  Colunas: ASIN | Título | Preço | Imagem URL | Link Afiliado |
           Rating | Rating Count | Vendedor | Categoria | Keywords | Status | Buscado Em
"""

import os
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

import gspread
from google.oauth2.service_account import Credentials

load_dotenv(Path(__file__).parent / ".env")

SHEET_ID      = os.getenv("GOOGLE_SHEETS_ID")
SA_FILE       = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", "service_account.json")
SHEET_NAME    = "Produtos"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

HEADERS = [
    "ASIN", "Título", "Preço (R$)", "Preço Original", "Desconto %",
    "Imagem URL", "Link Afiliado", "Rating", "Avaliações",
    "Prime", "Vendido pela Amazon", "Vendedor",
    "Categoria", "Keywords", "Feedbacks Clientes",
    "Status", "Buscado Em",
]

STATUS_OPTIONS = ["pendente", "aprovado", "rejeitado"]


def get_client() -> gspread.Client:
    sa_path = Path(__file__).parent / SA_FILE
    if not sa_path.exists():
        raise FileNotFoundError(
            f"Arquivo de credenciais não encontrado: {sa_path}\n"
            "Veja as instruções em scripts/amazon/README.md"
        )
    creds = Credentials.from_service_account_file(str(sa_path), scopes=SCOPES)
    return gspread.authorize(creds)


def get_or_create_sheet(client: gspread.Client, sheet_title: str) -> gspread.Spreadsheet:
    if SHEET_ID:
        return client.open_by_key(SHEET_ID)

    try:
        return client.open(sheet_title)
    except gspread.SpreadsheetNotFound:
        print(f"Criando nova planilha: '{sheet_title}'...")
        spreadsheet = client.create(sheet_title)
        print(f"OK Planilha criada! ID: {spreadsheet.id}")
        print(f"Adicione ao .env: GOOGLE_SHEETS_ID={spreadsheet.id}")
        return spreadsheet


def get_or_create_worksheet(spreadsheet: gspread.Spreadsheet) -> gspread.Worksheet:
    try:
        ws = spreadsheet.worksheet(SHEET_NAME)
    except gspread.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(title=SHEET_NAME, rows=1000, cols=len(HEADERS))
        ws.append_row(HEADERS)
        ws.format("A1:L1", {"textFormat": {"bold": True}, "backgroundColor": {"red": 0.2, "green": 0.6, "blue": 0.3}})
        print(f"OK Aba '{SHEET_NAME}' criada com cabeçalhos.")
    return ws


def get_existing_asins(ws: gspread.Worksheet) -> set[str]:
    all_values = ws.get_all_values()
    if len(all_values) <= 1:
        return set()
    return {row[0] for row in all_values[1:] if row}


def sync_products(products: list[dict], ws: gspread.Worksheet) -> tuple[int, int]:
    existing = get_existing_asins(ws)
    new_rows = []
    skipped = 0

    for p in products:
        if p["asin"] in existing:
            skipped += 1
            continue
        feedbacks_str = " | ".join(p.get("feedbacks") or [])
        new_rows.append([
            p.get("asin", ""),
            p.get("titulo", ""),
            p.get("preco", ""),
            p.get("preco_original", ""),
            p.get("desconto", ""),
            p.get("imagem_url", ""),
            p.get("link_afiliado", ""),
            p.get("rating", ""),
            p.get("rating_count", ""),
            "Sim" if p.get("prime") else "Nao",
            "Sim" if p.get("is_amazon") else "Nao",
            p.get("vendedor", ""),
            p.get("categoria", ""),
            p.get("keywords", ""),
            feedbacks_str,
            p.get("status", "pendente"),
            p.get("buscado_em", ""),
        ])

    if new_rows:
        ws.append_rows(new_rows, value_input_option="USER_ENTERED")

    return len(new_rows), skipped


def main():
    parser = argparse.ArgumentParser(description="Sincroniza produtos JSON → Google Sheets")
    parser.add_argument("--file",  required=True, help="Arquivo JSON gerado pelo fetch_products.py")
    parser.add_argument("--sheet", default="Afiliados - Receitas Fit", help="Nome da planilha")
    args = parser.parse_args()

    json_path = Path(args.file)
    if not json_path.exists():
        print(f"ERRO Arquivo não encontrado: {json_path}")
        return

    with open(json_path, encoding="utf-8") as f:
        products = json.load(f)

    print(f"Carregando {len(products)} produtos de {json_path.name}...")

    client      = get_client()
    spreadsheet = get_or_create_sheet(client, args.sheet)
    ws          = get_or_create_worksheet(spreadsheet)
    added, skipped = sync_products(products, ws)

    print(f"\nOK Sincronização concluída!")
    print(f"   Adicionados: {added} | Ignorados (duplicados): {skipped}")
    print(f"   Planilha: {spreadsheet.url}")
    print(f"\nPróximo passo: Abra a planilha, mude Status de 'pendente' para 'aprovado'")
    print(f"   Depois execute: python extract_approved.py")


if __name__ == "__main__":
    main()
