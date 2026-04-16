# Task: Generate Outline

**Task ID:** generate-outline
**Version:** 1.0.0
**Execution Type:** Agent (autônomo)
**Purpose:** Gerar outline H2/H3 semântico para uma keyword usando E.E.A.T.S. + Outline Generator
**Executor:** content-architect
**Elicit:** false
**Precondition:** Gate RS-001 PASS, keyword_atual selecionada

---

## Inputs

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|------------|-----------|
| `keyword` | string | SIM | Keyword principal do artigo |
| `tipo_artigo` | string | SIM | Tipo identificado pelo keyword-analyst |
| `intencao` | string | SIM | Intenção de busca classificada |
| `contexto_estruturado` | object | SIM | Entidades do cliente do pre-check |
| `knowledge_base_path` | string | SIM | `redator-2.0/knowledge/` |

---

## Preconditions

- [ ] Gate RS-001 PASS
- [ ] keyword_atual definida
- [ ] tipo_artigo definido
- [ ] Arquivos do Outline Generator e Templates disponíveis

---

## Execution Steps

### Step 1: Carregar referências

```yaml
load:
  - "redator-2.0/knowledge/04_OUTLINE_GENERATOR.md"
  - "redator-2.0/knowledge/03_ARTICLE_TEMPLATES.md"
  - "redator-2.0/knowledge/02_KNOWLEDGE_BASE.md"
  action: "Identificar template do tipo_artigo e regras do Outline Generator"
```

### Step 2: Identificar entidade central

```yaml
action: |
  Analisar keyword → extrair:
  - Entidade central (substantivo principal)
  - Hiperônimo (categoria superior)
  - Hiponimos (subtipos conhecidos)
  - Atributos esperados (propriedades da entidade)
  - Contexto do cliente (dados relevantes do contexto_estruturado)
```

### Step 3: Mapear intenções

```yaml
action: "Listar todas as intenções para esta entidade"
explicit_intents: "Derivadas da SERP (definição, mecanismo, tipos, custo, comparação)"
latent_intents: "Inferidas (como escolher, erros comuns, limitações, alternativas)"
```

### Step 4: Filtrar por tipo de artigo

```yaml
action: "Aplicar tabela de filtro do Outline Generator"
reference: "04_OUTLINE_GENERATOR.md — Seção 3 (Filtrar por Tipo)"
remove: "Intenções não adequadas para o tipo"
keep: "Intenções obrigatórias + opcionais relevantes"
```

### Step 5: Organizar hierarquia H2/H3

```yaml
ordering_rules:
  - "Definição sempre primeiro"
  - "Mecanismo antes de aplicação"
  - "Tipos antes de comparações"
  - "Custo no meio (após tipos)"
  - "Erros comuns antes do FAQ"
  - "FAQ sempre último"

h3_criteria:
  create_h3_when:
    - "H2 tem 2+ subtipos → cada subtipo é H3"
    - "H2 tem 3+ etapas → cada etapa pode ser H3"
    - "H2 tem aspecto técnico + prático → dividir em H3"
  skip_h3_when:
    - "H2 cobre um único aspecto linear"
    - "Subdivisão seria artificial"
    - "Total de palavras ficaria < 250 por H3"
```

### Step 6: Calcular distância semântica

```yaml
for_each_h2:
  calculate_semantic_distance:
    0-1: "Diretamente sobre a entidade → MANTER"
    2: "Atributo direto → MANTER"
    3: "Relacionado mas indireto → AVALIAR"
    4+: "Tangencial → REMOVER"
  rule: "Nenhum H2 com distância > 3 no outline final"
```

### Step 7: Contextualizar com dados do cliente

```yaml
action: "Para seções relevantes, adicionar entidades do cliente"
example:
  section: "Investimento e Custos"
  inject_entities:
    - "taxa de franquia: R$ 50.000"
    - "estrutura da loja: a partir de R$ 19.999,99"
    - "primeiro estoque: R$ 3.500 a R$ 10.000"
    - "royalties: 6% sobre faturamento bruto"
rule: "Dados injetados = apenas do contexto_estruturado, nunca inventados"
```

### Step 8: Estimar word count

```yaml
reference: "04_OUTLINE_GENERATOR.md — Seção 7 (Validação)"
per_type:
  educacional: "1.500-2.500 palavras"
  tutorial: "1.800-3.000 palavras"
  pilar: "2.500-4.000 palavras"
  silo: "2.000-3.000 palavras"
per_section: "300-350 palavras por H2/H3"
```

### Step 9: Gerar FAQ questions

```yaml
action: "Listar 4-8 perguntas cobrindo intenções latentes não cobertas nas seções"
format: "Q: {pergunta?} → Intenção: {intent} → Entidades: {lista}"
```

### Step 10: Validar outline

```yaml
checklist:
  - "[ ] Cada H2 responde a uma intenção distinta (sem sobreposição)"
  - "[ ] Ordem segue lógica informacional (definição antes de aplicação)"
  - "[ ] Nenhuma seção tem distância semântica > 3"
  - "[ ] H3 são necessários (não artificiais)"
  - "[ ] Tipo de artigo refletido na estrutura"
  - "[ ] FAQ cobre intenções não atendidas nos H2"
  - "[ ] Há pelo menos 1 seção com tabela/lista planejada"
  - "[ ] Word count estimado adequado ao tipo"
```

### Step 11: Formatar output

```yaml
action: "Usar formato padrão do Outline Generator (Seção 8)"
```

---

## Outputs

### Formato do Outline

```
OUTLINE: {titulo_artigo}
Tipo: {tipo}
Entidade central: {entidade}
Word count estimado: {total} palavras
Seções: {n_h2} H2 + {n_h3} H3
Dados do cliente injetados: {sim/não}

---

H1 - {titulo} (100-200 palavras)
  Summarization + Introdução
  Entidades: [{lista}]
  Elementos: summarization obrigatória

H2 - {titulo_h2_1} ({word_count} palavras)
  Intenção: {intencao}
  Entidades: [{entidades}]
  Elementos: {tabela/lista/link/nenhum}
  Distância semântica: {1-3}

  H3 - {titulo_h3} ({word_count} palavras)
    Foco: {aspecto_especifico}
    Entidades: [{entidades}]

H2 - {titulo_h2_N}
  ...

H2 - FAQ ({n} perguntas)
  Q1: {pergunta} → Intenção: {intent}
  Q2: {pergunta} → Intenção: {intent}
  ...

---
GATE RS-002: {PASS/FAIL}
Motivo (se FAIL): {motivo}
```

---

## Validation Criteria (Gate RS-002)

- [ ] Mínimo 4 H2 (exceto tipo news: mínimo 3)
- [ ] H2 com distância semântica ≤ 3
- [ ] Intenções mapeadas para todos os H2
- [ ] FAQ presente com 4+ perguntas
- [ ] Word count estimado dentro da faixa para o tipo
- [ ] Dados do cliente injetados corretamente (onde aplicável)

---

## Error Handling

| Erro | Ação |
|------|------|
| Tipo de artigo indefinido | Bloquear + solicitar ao chief |
| Menos de 4 H2 | Refazer com mais intenções |
| H2 com distância > 3 | Remover e substituir |
| Keyword ambígua | Alertar + aguardar desambiguação |

---

_Task Version: 1.0.0_
_Executor: content-architect_
