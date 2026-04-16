# Task: Package Output

**Task ID:** package-output
**Version:** 1.0.0
**Execution Type:** Agent (automático, não requer input do usuário)
**Purpose:** Montar o pacote de entrega com os 4 deliverables por keyword: HTML completo (com FAQ integrado), meta description, H1 e slug
**Executor:** output-packager
**Elicit:** false
**Precondition:** Gate RS-003 PASS (conteúdo completo escrito)

---

## Inputs

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|------------|-----------|
| `html_completo` | string | SIM | HTML completo produzido pelo seo-writer |
| `outline_estruturado` | object | SIM | Outline com H1 título e FAQ |
| `keyword` | string | SIM | Keyword principal |
| `contexto_estruturado` | object | SIM | Dados do cliente |

---

## Preconditions

- [ ] Gate RS-003 PASS
- [ ] `html_completo` disponível e não vazio
- [ ] `outline_estruturado` com título H1 definido

---

## Execution Steps

### Step 1: Extrair H1

```yaml
action: "Localizar <h1> no html_completo"
primary: "Pegar texto dentro de <h1>...</h1>"
fallback: "SE não encontrado → usar titulo do outline_estruturado"
clean: "Remover tags HTML, espaços extras"
validate:
  max_length: 70
  has_keyword: true
  no_caps: true
```

### Step 2: Gerar Meta Description

```yaml
action: "Compor meta description original — NÃO extrair do HTML"
formula: "keyword → benefício principal → dado numérico → diferencial"
rules:
  - "18-22 palavras"
  - "Keyword na primeira ou segunda palavra"
  - "Incluir ao menos 1 dado numérico (se disponível no contexto)"
  - "Tom declarativo, sem imperativo"
  - "Sem aspas, travessões, emojis, reticências"
  - "Terminar com ponto ou sem pontuação"
process:
  - "Ler contexto_estruturado.dados_financeiros"
  - "Identificar benefício mais relevante para a keyword"
  - "Compor frase seguindo as regras"
quality_check:
  word_count: "18-22 palavras — se < 15 → refazer"
  has_keyword: "Keyword presente? SE não → revisar"
examples:
  keyword: "franquia de minimercado autônomo"
  bad: "Saiba tudo sobre franquia Peggô Market e invista agora!"
  good: "A franquia de minimercado autônomo opera 24h sem atendentes, com faturamento médio de R$ 25.000 por loja e payback de 8 a 12 meses."
```

### Step 3: Gerar Slug

```yaml
action: "Transformar H1 em slug kebab-case"
transformation_steps:
  1: "Converter para lowercase"
  2: "Remover acentos e cedilha (ã→a, ç→c, é→e, etc.)"
  3: "Remover stopwords: o, a, os, as, um, uma, de, do, da, em, no, na, por, para, com, que, e"
  4: "Substituir espaços por hífens"
  5: "Remover caracteres especiais (:, /, ?, !, .)"
  6: "Remover hífens duplos (--) → -"
  7: "Truncar em 60 caracteres no último hífen"
validate:
  lowercase: true
  no_accents: true
  max_length: 60
  has_keyword_variant: true
examples:
  input: "Franquia de minimercado autônomo: como funciona e quanto investir"
  output: "franquia-minimercado-autonomo-como-funciona-investimento"
```

### Step 4: Verificar FAQ no HTML

```yaml
action: "Verificar que a seção FAQ está presente e corretamente posicionada no html_completo"
rule: "FAQ NÃO deve ser extraído como deliverable separado — pertence ao html_content"
locate: "Encontrar <h2> que contenha 'FAQ', 'Perguntas' ou 'Frequentes'"
position_check: "FAQ deve ser a ÚLTIMA seção do HTML (após o último H2 do corpo do artigo)"
validate:
  faq_present: true
  faq_is_last_section: true
  min_questions: 4
  max_questions: 8
  answer_length: "45-60 palavras por resposta"
  structure: "h2 > h3 > p"
  no_prohibited_connectors: true
if_faq_not_found:
  action: "BLOQUEAR — solicitar ao seo-writer que adicione a seção FAQ ao final do HTML"
  note: "NÃO gerar FAQ separado — o seo-writer deve escrever o FAQ dentro do HTML"
if_faq_not_last:
  action: "AVISAR — FAQ deve ser a última seção. Solicitar repositionamento ao seo-writer"
```

### Step 5: Limpar HTML do conteúdo

```yaml
action: "Verificar e limpar html_completo"
checks:
  - remove_wrappers: "Remover <html>, <head>, <body> se presentes"
  - remove_comments: "Remover <!-- -->"
  - remove_inline_styles: "Remover style=''"
  - validate_tags: "Tags permitidas: h1, h2, h3, p, ul, ol, li, strong, table, thead, tbody, tr, th, td, a"
  - line_breaks: "Garantir quebra de linha entre tags"
  - empty_lines: "1 linha vazia entre elementos diferentes"
  - summarization: "Verificar <p class='summarization'> presente"
```

### Step 6: Montar pacote usando template

```yaml
action: "Usar templates/delivery-package-tmpl.md para formatar output"
inject:
  keyword: "{keyword}"
  meta_description: "{meta_description}"
  h1: "{h1}"
  slug: "{slug}"
  html_content: "{html_completo_limpo}"
note: "O FAQ já está integrado no html_content — não injetar como campo separado"
```

### Step 7: Quality check final

```yaml
checklist:
  meta_description:
    - "[ ] 18-22 palavras"
    - "[ ] Keyword presente"
    - "[ ] Dado numérico incluído (se disponível)"
    - "[ ] Sem aspas/travessões/emojis"
  h1:
    - "[ ] Keyword presente"
    - "[ ] Máximo 70 caracteres"
    - "[ ] Sem CAIXA ALTA"
  slug:
    - "[ ] Kebab-case lowercase"
    - "[ ] Sem acentos"
    - "[ ] Máximo 60 caracteres"
  html_content:
    - "[ ] Summarization presente"
    - "[ ] Sem wrappers HTML"
    - "[ ] Tags apenas permitidas"
    - "[ ] Sem comentários HTML"
    - "[ ] FAQ presente como ÚLTIMA seção do HTML"
    - "[ ] FAQ com 4-8 perguntas (h2 > h3 > p)"
    - "[ ] Respostas FAQ com 45-60 palavras cada"
    - "[ ] Nenhum conector proibido nas respostas FAQ"
```

### Step 8: Entregar pacote ao chief

```yaml
action: "Enviar pacote_completo para redator-seo-chief"
format: "delivery-package-tmpl.md preenchido"
gate: "RS-004"
```

---

## Outputs

Pacote completo usando o template `templates/delivery-package-tmpl.md`.

---

## Validation Criteria (Gate RS-004)

- [ ] 4 deliverables presentes e não vazios (html_content, meta_description, h1, slug)
- [ ] Meta description: 18-22 palavras, keyword presente
- [ ] H1: máximo 70 chars, sem CAIXA ALTA
- [ ] Slug: kebab-case, sem acentos, máximo 60 chars
- [ ] HTML: sem wrappers, tags permitidas, summarization presente
- [ ] FAQ integrado no final do html_content (4-8 perguntas, 45-60 palavras cada)

---

## Error Handling

| Erro | Ação |
|------|------|
| H1 não encontrado no HTML | Usar título do outline |
| FAQ ausente no HTML | Gerar FAQ a partir das perguntas do outline |
| Meta description > 22 palavras | Reformular mais concisa |
| Slug > 60 chars | Truncar no último hífen antes do limite |
| Tag proibida no HTML | Substituir ou remover |

---

_Task Version: 1.0.0_
_Executor: output-packager_
