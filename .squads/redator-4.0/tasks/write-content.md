# Task: Write Content

**Task ID:** write-content
**Version:** 1.0.0
**Execution Type:** Sequential (seção por seção com gates)
**Purpose:** Escrever conteúdo HTML completo do artigo seguindo PMR19, E.E.A.T.S. e Style Guide
**Executor:** seo-writer
**Elicit:** false (aguarda "ok" entre seções como gate)
**Precondition:** Gate RS-002 PASS (outline aprovado)

---

## Inputs

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|------------|-----------|
| `outline_estruturado` | object | SIM | Output do generate-outline |
| `contexto_estruturado` | object | SIM | Entidades do cliente do pre-check |
| `keyword` | string | SIM | Keyword principal do artigo |
| `tipo_artigo` | string | SIM | Tipo de artigo |

---

## Preconditions

- [ ] Gate RS-002 PASS (outline validado)
- [ ] `outline_estruturado` disponível
- [ ] `contexto_estruturado` com dados do cliente
- [ ] Style Guide carregado: `redator-2.0/knowledge/05_STYLE_GUIDE.md`
- [ ] Premissas carregadas: `redator-2.0/knowledge/Premissas.md`
- [ ] Restrições carregadas: `redator-2.0/knowledge/restricao.md`

---

## Execution Steps

### Step 0: Carregar referências de escrita

```yaml
load_before_writing:
  - "redator-2.0/knowledge/05_STYLE_GUIDE.md"
  - "redator-2.0/knowledge/Premissas.md"
  - "redator-2.0/knowledge/restricao.md"
  - "redator-2.0/knowledge/03_ARTICLE_TEMPLATES.md"
  - "redator-2.0/knowledge/02_KNOWLEDGE_BASE.md"
note: "Consultar antes de cada entrega para garantir conformidade"
```

### Step 1: Escrever Summarization

```yaml
action: "Produzir summarization GEO"
format: '<p class="summarization">{50-60 palavras}</p>'
rules:
  - "Resume TODO o artigo em 50-60 palavras"
  - "Keyword principal na primeira ou segunda frase"
  - "Inclui dados numéricos do cliente quando disponíveis"
  - "Autossuficiente — deve fazer sentido sem ler o artigo"
  - "Sem conectores proibidos"
wait_for_ok: true
```

### Step 2: Escrever H1 (Introdução)

```yaml
action: "Escrever introdução completa"
word_count: "100-200 palavras"
structure:
  p1: "Lead GEO — entidade + dado + contexto + relevância (30-50 palavras)"
  p2: "Por que isso importa — problema que resolve (1 parágrafo)"
  p3: "O que o leitor vai encontrar neste artigo (1 parágrafo)"
rules:
  - "Entidade nomeada (não pronome)"
  - "Dado numérico do cliente na primeira frase quando disponível"
  - "Voz ativa predominante"
  - "Zero conectores proibidos"
wait_for_ok: true
```

### Step 3: Loop de escrita por seção (H2/H3)

```yaml
for_each_section_in_outline:
  load_section_metadata:
    - titulo
    - intencao
    - entidades
    - elementos (tabela/lista/link)
    - word_count_target

  writing_protocol:
    lead: "Primeira frase responde à intenção da seção sozinha"
    body: "Desenvolver com entidades, atributos, relações — 2-3 frases por parágrafo (mobile-first)"
    structure: "Adicionar tabela ou lista se especificado"
    close: "Último parágrafo sintetiza a seção (sem conector)"

  self_check_before_deliver:
    - "[ ] Zero conectores proibidos"
    - "[ ] Entidade nomeada (sem pronomes vagos)"
    - "[ ] Lead autossuficiente"
    - "[ ] Dados do cliente = exatos do contexto"
    - "[ ] Word count dentro da faixa (±50 palavras)"
    - "[ ] Bold apenas em entidades, dados, termos-chave"
    - "[ ] Tags HTML permitidas apenas"
    - "[ ] Parágrafos 2-3 frases (mobile-first)"
    - "[ ] Voz ativa predominante"

  wait_for_ok: true
```

### Step 4: Escrever FAQ

```yaml
action: "Escrever seção FAQ"
format: |
  <h2>Perguntas Frequentes sobre {entidade}</h2>

  <h3>{Pergunta 1?}</h3>
  <p>{Resposta autossuficiente, 45-60 palavras}</p>

  <h3>{Pergunta 2?}</h3>
  <p>{Resposta}</p>
rules:
  - "4-8 perguntas cobrindo intenções latentes do outline"
  - "Cada resposta autossuficiente (chunk independente)"
  - "Dados numéricos do cliente quando relevantes"
  - "Zero conectores proibidos"
  - "Bold em entidades e dados nas respostas"
wait_for_ok: true
```

### Step 5: Montar HTML completo

```yaml
action: "Concatenar todas as seções em ordem"
order:
  1. "summarization (<p class='summarization'>)"
  2. "<h1>{titulo}</h1>"
  3. "paragrafos do H1"
  4. "H2 #1 + parágrafos + H3s"
  5. "H2 #2 + parágrafos + H3s"
  6. "[... demais H2s]"
  7. "FAQ (h2 + h3 + p)"
final_check:
  - "Sem wrappers (<html>, <head>, <body>)"
  - "Quebra de linha entre todas as tags"
  - "1 linha vazia entre elementos diferentes"
  - "Nenhuma tag proibida"
```

---

## Delivery Format (per section)

```
[HTML limpo com quebras de linha]


=============================================

**Posso continuar para {proxima_secao}?**

---
STATUS: {progresso} | PRÓXIMO: {titulo_proximo_outline} | Lembrete: {regra_critica}
```

---

## Delivery Format (final)

```
[HTML COMPLETO concatenado]


=============================================

**Conteúdo completo escrito. Enviando para output-packager.**

---
STATUS: ✅ Todas as seções concluídas | PRÓXIMO: output-packager (RS-004) | Artigo: {N} palavras
```

---

## Reference: Prohibited Connectors Check

```
PROIBIDO: Além disso, Portanto, Dessa forma, Assim sendo, Em suma, Logo,
Por fim, Ou seja, Nesse sentido, Vale ressaltar, É importante destacar,
Saiba mais, Confira, Incrível, Revolucionário

SE encontrar qualquer um → reescrever frase iniciando com SUJEITO + VERBO
```

---

## Reference: Lead GEO Formula

```
[SUJEITO ESPECÍFICO] + [VERBO DE AÇÃO] + [QUANTIFICAÇÃO] + [CONTEXTO] + [RELEVÂNCIA]

BOM: "A franquia Peggô Market opera mais de 350 unidades em 12 estados brasileiros,
     com faturamento médio de R$ 25.000 por loja e payback entre 8 e 12 meses."

RUIM: "Existem diversas opções de franchising no mercado brasileiro."
```

---

## Validation Criteria (Gate RS-003)

- [ ] Todas as seções do outline escritas
- [ ] Summarization presente e com 50-60 palavras
- [ ] Zero conectores proibidos no texto completo
- [ ] HTML com apenas tags permitidas
- [ ] Sem wrappers HTML
- [ ] Dados do cliente preservados exatamente
- [ ] FAQ com 4+ perguntas e respostas

---

## Error Handling

| Erro | Ação |
|------|------|
| Dado do cliente ausente no contexto | Omitir ou usar [DADO NÃO DISPONÍVEL] |
| Seção muito curta (<200 palavras) | Expandir com mais atributos da entidade |
| Conector proibido encontrado | Reescrever antes de entregar |
| Tag HTML proibida | Substituir por tag permitida |

---

_Task Version: 1.0.0_
_Executor: seo-writer_
