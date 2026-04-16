# Checklist: Quality Gate do Briefing E.E.A.T.S.

> Executar antes de salvar o briefing na planilha.
> Todos os itens obrigatórios (🔴) devem passar. Itens recomendados (🟡) devem ter ≥80%.

## Bloco 1 — Presença das 7 Camadas (obrigatório)

- [ ] 🔴 Camada 1 (Entity Lock-in) presente e com definição-base
- [ ] 🔴 Camada 2 (Essential Entity Set) com tabela ≥8 sub-entidades
- [ ] 🔴 Camada 3 (Attribute Coverage) com árvore ≥10 atributos
- [ ] 🔴 Camada 4 (Relational Semantics) com tabela ≥5 relações
- [ ] 🔴 Camada 5 (Intent Completeness) com tabelas explícita (≥7) + latente (≥5)
- [ ] 🔴 Camada 6 (Contextual Embedding) com exemplos + frases GEO
- [ ] 🔴 Camada 7 (Entity Loop Closure) com síntese + CTA

## Bloco 2 — Qualidade da Entidade Principal (obrigatório)

- [ ] 🔴 Keyword nomeada explicitamente na definição-base (não pronome vago)
- [ ] 🔴 Definição tem: finalidade + mecanismo + requisito principal + restrição
- [ ] 🔴 Escopo delimitado: "É" e "Não é" preenchidos
- [ ] 🔴 ≥3 frases GEO-citáveis com entidade nomeada

## Bloco 3 — Integração do Contexto Empresa (obrigatório)

- [ ] 🔴 Nome da empresa cliente aparece no briefing (seção CTA ou restrições)
- [ ] 🔴 Tom de comunicação do cliente refletido nas restrições editoriais
- [ ] 🔴 Aviso legal do cliente incluído
- [ ] 🔴 Segmentos do cliente usados em exemplos ou intenções latentes

## Bloco 4 — Base em Pesquisa Real (obrigatório)

- [ ] 🔴 Research findings de @nebula referenciados (entidades, LSI, dados)
- [ ] 🔴 ≥1 dado recente (2025-2026) mencionado em Contextual Embedding
- [ ] 🔴 Sub-entidades de C2 vieram da pesquisa SERP (não inventadas)

## Bloco 5 — Saídas Complementares (obrigatório)

- [ ] 🔴 Termos LSI em ≥4 clusters com ≥25 termos totais
- [ ] 🔴 Outline sugerida com H1 + ≥6 H2s + H3s aninhados + FAQ
- [ ] 🔴 Restrições SEMPRE/NUNCA preenchidas com ≥5 itens cada
- [ ] 🔴 CTA com URL, frase de fechamento e texto do botão

## Bloco 6 — Qualidade Editorial (recomendado)

- [ ] 🟡 Power keywords sugeridas por posição (H1, H2s, CTA)
- [ ] 🟡 Tabela comparativa sugerida em H2 de modalidades
- [ ] 🟡 ≥5 perguntas FAQ sugeridas
- [ ] 🟡 Lead GEO de 2-3 frases sugerido abaixo do H1

## Bloco 7 — Formatação para Planilha (obrigatório)

- [ ] 🔴 Briefing começa com "## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK"
- [ ] 🔴 Termos LSI separados para coluna U (formato de clusters)
- [ ] 🔴 Tamanho total: ≥800 palavras (briefings muito curtos são sinal de falha)
- [ ] 🔴 Sem placeholders não substituídos ({{campo}} sem valor)

---

## Decisão

| Resultado | Ação |
|-----------|------|
| Todos os 🔴 passaram | SALVAR na planilha |
| 1-2 🔴 falharam | Completar os gaps antes de salvar |
| ≥3 🔴 falharam | REGENERAR — briefing insuficiente |
| 🔴 falharam por falta de pesquisa | Executar @nebula *pesquisar-topico novamente |
