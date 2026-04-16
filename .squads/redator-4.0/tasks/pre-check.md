# Task: Pre-Check

**Task ID:** pre-check
**Version:** 1.0.0
**Execution Type:** Hybrid (automático + bloqueante se falhar)
**Purpose:** Validar cliente e contexto antes de qualquer produção de conteúdo
**Executor:** client-validator (com supervisão do redator-seo-chief)
**Elicit:** false (validação automática, bloqueante)

---

## Inputs

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|------------|-----------|
| `cliente_slug` | string | SIM | Identificador do cliente (ex: `peggo`) |
| `planilha_path` | string | SIM | Caminho da planilha Excel |

---

## Preconditions

- [ ] redator-seo-chief ativo
- [ ] client-validator disponível
- [ ] Permissão de leitura em `redator-2.0/knowledge/`

---

## Execution Steps

### Step 1: Validar cliente_slug

```yaml
action: Verificar se cliente_slug foi fornecido e não está vazio
pass: "Slug presente → prosseguir"
fail:
  output: |
    ❌ PRE-CHECK BLOQUEADO — Gate RS-000
    Motivo: Cliente não identificado.
    Informe o slug do cliente para continuar.
    Exemplo: *produce peggo "redator-2.0/knowledge/Peggo março 2026.xlsx"
  status: BLOCKED
```

### Step 2: Localizar arquivo de contexto

```yaml
action: "Verificar existência de: redator-2.0/knowledge/{cliente_slug}-marketing.md"
pass: "Arquivo existe → prosseguir"
fail:
  output: |
    ❌ PRE-CHECK BLOQUEADO — Gate RS-000
    Motivo: Arquivo de contexto não encontrado.
    Caminho esperado: redator-2.0/knowledge/{cliente_slug}-marketing.md

    Por favor, crie o arquivo com as informações do cliente antes de continuar.
    O arquivo deve conter:
    - Nome e descrição da empresa
    - Modelo de negócio
    - Dados financeiros (faturamento, margens, investimento)
    - Diferenciais competitivos
    - Público-alvo
  status: BLOCKED
```

### Step 3: Ler e validar conteúdo do contexto

```yaml
action: "Ler conteúdo do arquivo {cliente_slug}-marketing.md"
validations:
  not_empty:
    check: "word_count > 0"
    fail: "BLOQUEAR — arquivo vazio"
  minimum_content:
    check: "word_count >= 200"
    warn: "word_count < 300 → AVISAR sobre contexto insuficiente"
    pass: "word_count >= 300 → PASS sem aviso"
```

### Step 4: Extrair entidades do contexto

```yaml
action: "Parsear arquivo e extrair entidades estruturadas"
extract:
  nome_empresa:
    from: "Primeira menção do nome da empresa no texto"
  modelo_negocio:
    from: "Descrição do modelo operacional"
  dados_financeiros:
    from: "Qualquer menção a valores (R$, %, ROI, payback)"
    preserve_exact: true
  diferenciais:
    from: "Características que diferenciam o negócio"
  publico_alvo:
    from: "Quem usa ou investe no modelo"
  presenca:
    from: "Localização, cidades, estados, cobertura"
```

### Step 5: Validar planilha

```yaml
action: "Verificar existência do arquivo da planilha"
pass: "Arquivo existe → prosseguir"
warn:
  condition: "Arquivo não encontrado mas cliente identificado"
  output: |
    ⚠️ Planilha não localizada em: {planilha_path}
    Verifique o caminho ou forneça as keywords manualmente.
    O pipeline continuará com keyword-analyst solicitando input manual.
```

### Step 6: Compor output estruturado

```yaml
action: "Montar contexto_estruturado para injetar em todos os agentes"
output_structure:
  cliente:
    slug: "{cliente_slug}"
    nome: "{nome_empresa}"
    modelo: "{modelo_negocio}"
    diferenciais: ["{diferencial_1}", "{diferencial_2}"]
    dados_financeiros: "{extraido_literalmente}"
    publico: "{publico_alvo}"
    presenca: "{cobertura_geografica}"
  arquivos:
    contexto_path: "redator-2.0/knowledge/{cliente_slug}-marketing.md"
    planilha_path: "{planilha_path}"
```

---

## Outputs

### PASS

```
✅ PRE-CHECK APROVADO — Gate RS-000 PASS

Cliente: {nome_empresa}
Slug: {cliente_slug}
Contexto: {caminho} ({word_count} palavras)

Entidades extraídas:
  Empresa: {nome_empresa}
  Modelo: {modelo_negocio}
  Dados financeiros: {dados}
  Diferenciais: {lista}
  Público-alvo: {publico}

Planilha: {planilha_path}
Status planilha: {encontrada/não encontrada}

Pipeline autorizado. Próxima fase: keyword intake.
```

### BLOCKED

```
❌ PRE-CHECK BLOQUEADO — Gate RS-000 FAIL
Motivo: {motivo_especifico}
Ação necessária: {instrucao_clara}
Pipeline pausado até resolução.
```

---

## Validation Criteria (Gate RS-000)

- [ ] cliente_slug fornecido e não vazio
- [ ] arquivo `{slug}-marketing.md` existe em `redator-2.0/knowledge/`
- [ ] arquivo de contexto tem conteúdo (> 0 palavras)
- [ ] entidades mínimas extraídas (nome_empresa, modelo_negocio)

---

## Error Handling

| Erro | Ação |
|------|------|
| Slug vazio | BLOQUEAR + instruções de como fornecer |
| Arquivo não existe | BLOQUEAR + informar path esperado |
| Arquivo vazio | BLOQUEAR + solicitar preenchimento |
| Arquivo < 200 palavras | AVISAR + perguntar se continua |
| Planilha não encontrada | AVISAR + continuar com fallback manual |

---

## Heuristics Applied

- SP_CHF_001: Bloqueio por falta de contexto
- SP_CHF_005: Solicitar sem adivinhar
- SP_CV_001: Slug obrigatório
- SP_CV_002: Contexto deve existir
- SP_CV_003: Extrair entidades essenciais
- SP_CV_004: Verificar completude do contexto

---

_Task Version: 1.0.0_
_Executor: client-validator_
