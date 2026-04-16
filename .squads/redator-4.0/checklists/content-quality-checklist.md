# Content Quality Checklist

**ID:** content-quality-checklist
**Gates:** SP-002 (Outline), SP-003 (Conteúdo), SP-004 (Pacote)
**Executor:** redator-seo-chief (revisão final)
**Blocking:** Sim para itens CRÍTICOS

---

## Checklist SP-002 — Outline

### Estrutura

- [ ] **[CRÍTICO]** Mínimo 4 H2 presentes (exceto news: 3)
- [ ] **[CRÍTICO]** Artigo tem ao menos 1 H3 no corpo (fora do FAQ). Cada H2 que usa H3: 1-3 H3 filhos máximo.
- [ ] **[CRÍTICO]** Nenhum H2 com distância semântica > 3
- [ ] **[CRÍTICO]** FAQ com 4+ perguntas planejadas
- [ ] Ordem lógica: definição → mecanismo → tipos → aplicação → erros → FAQ
- [ ] Tipo de artigo refletido na estrutura
- [ ] Títulos H2/H3 em sentence case (apenas primeira letra + nomes próprios em maiúscula)

### Semântica

- [ ] **[CRÍTICO]** Entidade central identificada
- [ ] Intencoes explícitas e latentes mapeadas
- [ ] Dados do cliente injetados nas seções relevantes

### Qualidade

- [ ] H3 são necessários (não artificiais)
- [ ] Word count estimado adequado ao tipo de artigo
- [ ] Pelo menos 1 seção com tabela/lista planejada

---

## Checklist SP-003 — Conteúdo HTML

### PMR19

- [ ] **[CRÍTICO]** Estrutura lógica do macro ao micro
- [ ] **[CRÍTICO]** Primeiro parágrafo de cada seção resume o tema
- [ ] Parágrafos de 2-3 linhas (mais parágrafos por seção, não mais longos)
- [ ] Voz ativa predominante
- [ ] Variação sintática (frases simples e complexas alternadas)
- [ ] Frases enxutas (15-25 palavras ideal, máximo 35)

### E.E.A.T.S. + GEO

- [ ] **[CRÍTICO]** Lead de cada seção é autossuficiente (chunk independente)
- [ ] **[CRÍTICO]** Entidade nomeada no primeiro parágrafo de cada H2/H3 (lead explícito)
- [ ] Pronomes contextuais aceitáveis no corpo da seção ("a rede", "o modelo") — não bloqueia
- [ ] Dados numéricos quantificados
- [ ] Summarization presente (<p class="summarization">)
- [ ] Summarization tem 50-60 palavras com keyword

### Restrições de Estilo

- [ ] **[CRÍTICO]** Zero conectores proibidos (Além disso, Portanto, Dessa forma, etc.)
- [ ] **[CRÍTICO]** Zero travessões usados como conectores
- [ ] Sem CAIXA ALTA em títulos
- [ ] Sem emojis no texto
- [ ] Bold apenas em: entidades, dados numéricos, termos-chave
- [ ] Máximo 3 bolds por parágrafo
- [ ] Sem adjetivação exagerada (incrível, revolucionário, etc.)

### HTML

- [ ] **[CRÍTICO]** Tags apenas: h1, h2, h3, p, ul, ol, li, strong, table, thead, tbody, tr, th, td, a
- [ ] **[CRÍTICO]** Sem wrappers: html, head, body, section, div, article
- [ ] Sem comentários HTML (`<!-- -->`)
- [ ] Sem estilos inline
- [ ] Quebra de linha entre todas as tags
- [ ] 1 linha vazia entre elementos diferentes

### Dados do Cliente

- [ ] **[CRÍTICO]** Nenhum dado inventado — apenas do contexto do cliente
- [ ] Valores monetários preservados exatamente (R$ 50.000, 6%, etc.)
- [ ] Nomes da empresa preservados exatamente

### Word Count

- [ ] Summarization: 50-60 palavras
- [ ] H1 intro: 100-200 palavras (summarization + 2-3 parágrafos)
- [ ] H2 total (todos os H3 filhos): 300-400 palavras (tolerância ±50)
- [ ] H3 subsecão: 100-150 palavras (3-4 parágrafos de 2-3 linhas)
- [ ] FAQ por resposta: 30-60 palavras

---

## Checklist SP-004 — Pacote de Entrega

### Meta Description

- [ ] **[CRÍTICO]** 18-22 palavras
- [ ] **[CRÍTICO]** Keyword presente (primeira ou segunda palavra)
- [ ] Dado numérico incluído (quando disponível)
- [ ] Sem aspas, travessões, emojis
- [ ] Tom declarativo (sem imperativo: saiba, descubra, etc.)

### H1

- [ ] **[CRÍTICO]** Keyword principal presente
- [ ] **[CRÍTICO]** Máximo 70 caracteres
- [ ] Sem CAIXA ALTA
- [ ] Sem pontuação excessiva (!?, ...)

### Slug

- [ ] **[CRÍTICO]** Kebab-case lowercase
- [ ] **[CRÍTICO]** Sem acentos ou cedilha
- [ ] **[CRÍTICO]** Máximo 60 caracteres
- [ ] Keyword incluída
- [ ] Sem stopwords desnecessárias

### FAQ

- [ ] **[CRÍTICO]** 4-8 perguntas
- [ ] Respostas autossuficientes (30-60 palavras)
- [ ] Tags corretas: h2 > h3 > p
- [ ] Nenhum conector proibido nas respostas

### Conteúdo HTML

- [ ] **[CRÍTICO]** Summarization presente
- [ ] **[CRÍTICO]** Sem wrappers HTML
- [ ] **[CRÍTICO]** Tags apenas permitidas
- [ ] Todos os 5 deliverables não vazios

---

## Escala de Aprovação

| Gates OK | Status |
|----------|--------|
| SP-000 + SP-001 + SP-002 + SP-003 + SP-004 | ✅ Pacote completo aprovado |
| SP-000 + SP-001 + SP-002 + SP-003 (sem SP-004) | ⚠️ Conteúdo OK, pacote com problema |
| SP-000 + SP-001 (sem SP-002) | ❌ Outline bloqueou — verificar keyword |
| SP-000 (sem SP-001) | ❌ Planilha sem keywords válidas |
| Falha no SP-000 | 🚫 Pipeline bloqueado — resolver cliente/contexto |
