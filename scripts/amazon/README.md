# Sistema de Afiliados Amazon — Receitas Fit

Tag de afiliado: `fits000-20`

## Fluxo completo

```
1. fetch_products.py   → busca produtos na Amazon → salva JSON
2. sheets_sync.py      → envia JSON para Google Sheets
3. [você revisa]       → muda Status de "pendente" para "aprovado"
4. extract_approved.py → lê aprovados, baixa imagens → gera JSON final
5. generate_content.py → gera arquivos markdown em src/content/afiliados/
```

---

## Configuração inicial (fazer 1 vez)

### 1. Instalar dependências Python

```bash
cd scripts/amazon
pip install -r requirements.txt
```

### 2. Credenciais Amazon Creators API

1. Acesse: https://associados.amazon.com.br
2. Vá em: **Ferramentas → Creators API**
3. Crie uma nova aplicação
4. Copie o `Credential ID` e `Credential Secret`

### 3. Credenciais Google Sheets (Service Account)

1. Acesse: https://console.cloud.google.com
2. Crie um projeto (ou use um existente)
3. Ative a API **Google Sheets** e **Google Drive**
4. Vá em: **IAM e Admin → Contas de serviço**
5. Crie uma conta de serviço → gere e baixe a chave JSON
6. Renomeie o arquivo para `service_account.json` e coloque em `scripts/amazon/`
7. Copie o e-mail da conta de serviço (termina em `@...iam.gserviceaccount.com`)

### 4. Configurar o .env

```bash
cp .env.example .env
```

Edite `.env`:
```
AMAZON_CREDENTIAL_ID=seu_id
AMAZON_CREDENTIAL_SECRET=sua_chave
AMAZON_TAG=fits000-20

GOOGLE_SHEETS_ID=           # deixe vazio — será criado automaticamente na 1ª execução
GOOGLE_SERVICE_ACCOUNT_FILE=service_account.json
```

### 5. Compartilhar planilha com a conta de serviço

Na 1ª execução do `sheets_sync.py`, uma planilha será criada automaticamente.
Você precisará **compartilhar a planilha** com o e-mail da service account
(permissão de Editor).

---

## Comandos de uso

### Buscar proteínas
```bash
python fetch_products.py --keywords "whey protein isolado" --category proteinas --max 10
python sheets_sync.py --file output/proteinas_YYYYMMDD_HHMMSS.json
```

### Buscar creatinas
```bash
python fetch_products.py --keywords "creatina monohidratada" --category creatinas --max 10
python sheets_sync.py --file output/creatinas_YYYYMMDD_HHMMSS.json
```

### Outras categorias sugeridas
```bash
python fetch_products.py --keywords "pre treino termogenico" --category pre-treino
python fetch_products.py --keywords "bcaa aminoacidos" --category aminoacidos
python fetch_products.py --keywords "vitamina d3 k2" --category vitaminas
```

### Após aprovar na planilha
```bash
python extract_approved.py           # processa todos os aprovados
python generate_content.py           # gera markdown em src/content/afiliados/
```

### Processar só uma categoria
```bash
python extract_approved.py --category proteinas
python generate_content.py --category proteinas --tipo comparativo
```

---

## Estrutura de arquivos gerada

```
scripts/amazon/output/
  proteinas_20250101_143022.json    ← bruto da Amazon
  approved_proteinas.json           ← aprovados com imagens locais

public/afiliados/images/
  B01N5IB20Q.jpg                    ← imagens baixadas da Amazon

src/content/afiliados/
  melhores-proteinas-2025.md        ← página gerada (editar com @affiliate)
```

---

## Status da planilha

| Status    | Significado |
|-----------|-------------|
| pendente  | Produto encontrado, aguardando revisão |
| aprovado  | Será incluído na página |
| rejeitado | Ignorado pelo extract_approved.py |
