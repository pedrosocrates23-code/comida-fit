# Task: Read Spreadsheet

**Task ID:** read-spreadsheet
**Version:** 1.0.0
**Execution Type:** Hybrid (automático + fallback manual)
**Purpose:** Ler planilha Excel de keywords e retornar lista priorizada e classificada
**Executor:** keyword-analyst
**Elicit:** true (quando arquivo não pode ser lido automaticamente)
**Precondition:** Gate RS-000 PASS (pre-check aprovado)

---

## Inputs

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|------------|-----------|
| `planilha_path` | string | SIM | Caminho para o arquivo .xlsx |
| `contexto_estruturado` | object | SIM | Output do pre-check com entidades do cliente |

---

## Preconditions

- [ ] Gate RS-000 aprovado
- [ ] `planilha_path` fornecido
- [ ] `contexto_estruturado` disponível

---

## Execution Steps

### Step 1: Tentar ler arquivo Excel

```yaml
action: "Ler arquivo {planilha_path} usando ferramenta disponível"
tools_to_try:
  - "Read tool (se xlsx puder ser lido como texto)"
  - "Bash com Node.js (xlsx library se disponível)"
  - "Bash com Python (pandas/openpyxl se disponível)"
fallback: "SE nenhuma ferramenta disponível → ir para Step 1b (manual)"
```

### Step 1b: Fallback manual (se arquivo não legível)

```yaml
elicit: true
action: |
  ⚠️ Não foi possível ler o arquivo Excel automaticamente.
  Por favor, forneça as keywords no formato abaixo:

  keyword | volume | kd
  --------|--------|---
  [keyword 1] | [número ou -] | [número ou -]
  [keyword 2] | [número ou -] | [número ou -]

  (volume e kd são opcionais — use - se não tiver)
```

### Step 2: Identificar estrutura da planilha

```yaml
action: "Analisar primeiras 3 linhas para identificar colunas"
column_mapping:
  keyword: ["keyword", "kw", "palavra-chave", "termo", "term", "query"]
  volume: ["volume", "vol", "search volume", "busca mensal"]
  kd: ["kd", "dificuldade", "difficulty", "keyword difficulty"]
  cpc: ["cpc", "valor", "custo por clique"]
  intent: ["intenção", "intent", "tipo"]
handling_if_no_header:
  - "Tratar primeira linha como dado"
  - "Assumir ordem: keyword | volume | kd | cpc"
```

### Step 3: Processar cada linha

```yaml
for_each_row:
  extract:
    - keyword (limpar espaços extras)
    - volume (converter para int, 0 se vazio)
    - kd (converter para int, 100 se vazio = tratar como difícil)

  skip_if:
    - "Linha vazia"
    - "keyword vazia ou null"
    - "keyword parece ser cabeçalho duplicado"
```

### Step 4: Classificar intenção de busca

```yaml
for_each_keyword:
  if_intent_column_exists: "Usar valor da coluna"
  else: "Inferir pelos sinais lexicais"

  intent_signals:
    informacional:
      patterns: ["o que é", "como funciona", "o que significa", "tipos de",
                 "o que são", "como é", "para que serve", "definição"]
    investigacional:
      patterns: ["melhor", "vale a pena", "comparar", "vs", "review",
                 "análise", "avaliação", "qual é melhor"]
    transacional:
      patterns: ["comprar", "preço", "contratar", "investimento", "quanto custa",
                 "franquia", "abrir", "montar", "investir"]
    latente:
      patterns: ["como abrir", "como montar", "passo a passo", "guia",
                 "tutorial", "aprenda"]
```

### Step 5: Recomendar tipo de artigo

```yaml
intent_to_type_map:
  informacional: ["educacional", "pilar", "silo"]
  investigacional: ["afiliado", "comparativo", "listicle"]
  transacional: ["afiliado", "pilar", "educacional"]
  latente: ["tutorial", "pilar", "educacional"]

  selection_rule: |
    SE volume > 5000 → preferir pilar
    SE keyword é [X] vs [Y] → comparativo
    SE keyword tem número (10 melhores) → listicle
    SE keyword é branded (nome da empresa) → institucional (pular)
    SENÃO → primeiro tipo da lista para a intenção
```

### Step 6: Validar relevância para o cliente

```yaml
action: "Verificar se keyword é relevante para o contexto do cliente"
using: contexto_estruturado.modelo_negocio + contexto_estruturado.diferenciais
skip_if:
  - "Keyword claramente de outro segmento"
  - "Keyword navegacional sem relação com o cliente"
mark_high_relevance_if:
  - "Keyword menciona setor do cliente diretamente"
  - "Keyword menciona público-alvo do cliente"
```

### Step 7: Calcular prioridade

```yaml
priority_scoring:
  high:
    condition: "volume > 1000 AND kd < 40"
    label: "🔴 Alta"
  medium:
    condition: "volume > 500 OR kd < 60"
    label: "🟡 Média"
  low:
    condition: "outros casos"
    label: "🟢 Baixa"
  no_data:
    condition: "volume = 0 AND kd = 100 (sem dados)"
    label: "⚪ Sem dados — manter ordem original"
```

### Step 8: Remover duplicatas e ordenar

```yaml
deduplication:
  - "Identificar keywords semanticamente idênticas"
  - "Manter a de maior volume (ou primeira se empate)"

ordering:
  - "Alta prioridade primeiro"
  - "Dentro de cada prioridade: maior volume"
  - "Sem dados: manter ordem original da planilha"
```

### Step 9: Formatar output

```yaml
output: keywords_classificadas (lista ordenada)
```

---

## Outputs

### PASS

```
✅ KEYWORD INTAKE CONCLUÍDO — Gate RS-001 PASS

Total processado: {N} keywords
Alta prioridade: {n_alta}
Média prioridade: {n_media}
Baixa prioridade: {n_baixa}
Ignoradas (navegacional/irrelevante): {n_skip}
Duplicatas removidas: {n_dup}

LISTA PARA PRODUÇÃO (ordem de execução):

1. {keyword_1}
   Volume: {vol} | KD: {kd} | Prioridade: 🔴 Alta
   Intenção: {intent} | Tipo: {tipo}

2. {keyword_2}
   Volume: {vol} | KD: {kd} | Prioridade: 🟡 Média
   Intenção: {intent} | Tipo: {tipo}

[...]

Iniciar produção pela keyword #1? (s/n)
```

### FAIL

```
❌ KEYWORD INTAKE FALHOU — Gate RS-001 FAIL
Motivo: {motivo}
Ação: {instrucao}
```

---

## Validation Criteria (Gate RS-001)

- [ ] Pelo menos 1 keyword processada
- [ ] Todas as keywords têm intenção classificada
- [ ] Todas as keywords têm tipo de artigo definido
- [ ] Lista ordenada por prioridade

---

## Error Handling

| Erro | Ação |
|------|------|
| Arquivo não existe | Fallback manual (elicitation) |
| Arquivo não legível | Fallback manual |
| Planilha vazia | BLOQUEAR + solicitar keywords |
| Nenhuma keyword relevante | AVISAR + perguntar se continua |

---

_Task Version: 1.0.0_
_Executor: keyword-analyst_
