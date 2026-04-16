# Regras Canônicas — SEO Producer QA Squad

**Versão:** 2.0
**Total de regras:** 120+
**Conflitos resolvidos:** 4

---

## Conflitos Resolvidos

| Conflito | Descartado | Canônico |
|----------|-----------|----------|
| Tamanho do parágrafo | write-content.md "3-4 linhas" | **Mobile-first: ≤ 2-3 frases** |
| Bold máximo | "Mais de 3 é errado" | **≤ 3 permitido — 4+ é violação** |
| Conectores lista | 11 itens no seo-writer | **15 itens (união de todas as fontes)** |
| FAQ mínimo de palavras | 30 palavras | **45 palavras** |

---

## DIMENSÃO A — Estrutura do Outline

| ID | Regra | Bloqueante |
|----|-------|-----------|
| A00 | Conformidade com template: se template_resolvido presente, todas as seções obrigatórias do template devem estar no outline. H2 não previsto exige justificativa semântica. | SIM |
| A01 | Mínimo 4 H2 por artigo (exceto tipo news: mínimo 3) | SIM |
| A02 | O artigo deve ter ao menos 1 H3 no corpo (fora do FAQ). Cada H2 que usa H3: mínimo 1, máximo 3 H3 filhos. Artigo com zero H3 no corpo = violação bloqueante. | SIM |
| A03 | Nenhum H2 com distância semântica > 3 | SIM |
| A04 | FAQ presente com mínimo 4 perguntas planejadas | SIM |
| A05 | Ordem lógica: definição → mecanismo → tipos → aplicação → erros → FAQ | NÃO |
| A06 | Tipo de artigo refletido na estrutura do outline | NÃO |
| A07 | Títulos H2/H3 em sentence case — norma da língua portuguesa | SIM |
| A08 | Word count estimado adequado ao tipo de artigo | NÃO |
| A09 | Pelo menos 1 seção com tabela ou lista planejada | AVISO |
| A10 | Cada H2 responde a intenção distinta — sem sobreposição | NÃO |
| A11 | Dados do cliente injetados nas seções relevantes | NÃO |
| A12 | H3 são necessários e justificados — nunca artificiais | NÃO |
| A13 | FAQ cobre intenções latentes não cobertas nos H2 | NÃO |

---

## DIMENSÃO B — Estrutura do Texto

| ID | Regra | Bloqueante |
|----|-------|-----------|
| B01 | Lead de cada H2/H3: primeira frase autossuficiente | SIM |
| B02 | Lead GEO: [SUJEITO] + [VERBO] + [QUANTIFICAÇÃO] + [CONTEXTO] + [RELEVÂNCIA] | SIM |
| B03 | Entidade nomeada explicitamente no lead — nunca pronome vago na abertura | SIM |
| B04 | Pronomes contextuais aceitáveis no corpo da seção ("a rede", "o modelo") | — |
| B05 | Mobile-first: parágrafos de no máximo 2-3 frases curtas | AVISO |
| B06 | 1 ideia por parágrafo | NÃO |
| B07 | Estrutura lógica do macro ao micro dentro de cada seção | NÃO |
| B08 | Primeiro parágrafo resume o tema e o propósito da seção (PMR19-17) | SIM |
| B09 | Cada subtítulo inicia com frase-resumo clara do bloco (PMR19-18) | NÃO |
| B10 | Frases: 15-25 palavras ideal — máximo absoluto 35 palavras | AVISO |
| B11 | H2 NUNCA salta para H3 sem parágrafo introdutório (1-3 frases entre H2 e primeiro H3) | SIM |

---

## DIMENSÃO C — Word Count

| ID | Regra | Bloqueante |
|----|-------|-----------|
| C01 | Summarization: 50-60 palavras exatas | SIM |
| C02 | H1 intro: 100-200 palavras | NÃO |
| C03 | H2 intro (parágrafo introdutório do H2, sem contar H3 filhos): 300-400 palavras | NÃO |
| C04 | H3 subsecão: 100-150 palavras | NÃO |
| C05 | FAQ por resposta: 45-60 palavras | SIM |
| C06 | Total de perguntas FAQ: 4-8 | SIM |
| C07 | Total do artigo dentro da faixa do tipo de artigo | NÃO |

**Faixas por tipo:**
- educacional: 1.500-2.500 | tutorial: 1.800-3.000 | afiliado: 1.500-2.500
- comparativo: 1.500-2.000 | silo: 2.000-3.000 | científico: 2.000-3.500
- listicle: 1.800-3.500 | news: 1.200-2.000 | pilar: 2.500-4.000

---

## DIMENSÃO D — Conectores e Estilo

| ID | Regra | Bloqueante |
|----|-------|-----------|
| D01 | ZERO conectores proibidos (lista de 15 itens abaixo) | SIM |
| D02 | Voz ativa em ≥ 90% das frases | AVISO |
| D03 | Variação sintática: frases simples e complexas alternadas | NÃO |
| D04 | Frases enxutas, sem redundância ou rodeios | NÃO |
| D05 | Sem adjetivação exagerada: extraordinário, único, inovador, surpreendente, excepcional | AVISO |
| D06 | Reforço de termos-centrais sem repetição mecânica da keyword exata | NÃO |
| D07 | Sentence case em TODOS os títulos — norma da língua portuguesa | SIM |
| D08 | Sem emojis no texto | SIM |
| D09 | ZERO travessões (—) em qualquer posição do texto — substituir SEMPRE por vírgula, dois-pontos, ponto ou reescrita da frase. Travessão em qualquer forma = violação bloqueante imediata. | SIM |

**Lista completa de conectores proibidos (D01):**
```
Além disso | Portanto | Dessa forma | Assim sendo | Em suma
Logo | Por fim | Ou seja | Nesse sentido | Vale ressaltar
É importante destacar | Saiba mais | Confira | Incrível | Revolucionário
```

---

## DIMENSÃO E — Bold

| ID | Regra | Bloqueante |
|----|-------|-----------|
| E01 | Bold APENAS em: entidades, dados numéricos, termos-chave SEO, nomes de marcas/produtos | NÃO |
| E02 | NUNCA bold em frases inteiras | SIM |
| E03 | NUNCA bold em conectivos ou palavras genéricas | SIM |
| E04 | Máximo 3 elementos bold por parágrafo (≤ 3 = OK, ≥ 4 = violação) | AVISO |
| E05 | Não concentrar todos os bolds no mesmo parágrafo | NÃO |

---

## DIMENSÃO F — HTML

| ID | Regra | Bloqueante |
|----|-------|-----------|
| F01 | Tags PERMITIDAS: h1 h2 h3 p ul ol li strong table thead tbody tr th td a | — |
| F02 | Tags PROIBIDAS: section div article aside h4 h5 h6 span br hr img html head body header footer | SIM |
| F03 | Class permitida: APENAS "summarization" | SIM |
| F04 | Sem comentários HTML | SIM |
| F05 | Sem estilos inline (style="") | SIM |
| F06 | Quebra de linha entre todas as tags | NÃO |
| F07 | 1 linha vazia entre elementos diferentes | NÃO |
| F08 | Sem wrappers de documento (html, head, body) | SIM |

---

## DIMENSÃO G — Dados do Cliente

| ID | Regra | Bloqueante |
|----|-------|-----------|
| G01 | Zero dados inventados — 100% do contexto_estruturado | SIM |
| G02 | Valores monetários preservados exatamente: R$ 50.000 (não "cinquenta mil") | SIM |
| G03 | Percentuais preservados exatamente: 6% (não "cerca de 6%") | SIM |
| G04 | Prazos preservados exatamente: 8-12 meses (não "menos de um ano") | SIM |
| G05 | Nomes da empresa preservados exatamente | SIM |
| G06 | Dado ausente = omitir OU [DADO NÃO DISPONÍVEL] — nunca estimar | SIM |

---

## DIMENSÃO H — E.E.A.T.S.

| ID | Regra | Bloqueante |
|----|-------|-----------|
| H01 | Entidade central nomeada e definida nos primeiros 100 palavras | SIM |
| H02 | Subentidades obrigatórias do espaço semântico presentes | NÃO |
| H03 | Atributos internos da entidade cobertos (características, funcionamento, custo) | NÃO |
| H04 | Hiperônimos e hipônimos usados — pluralidade semântica | NÃO |
| H05 | Intenções explícitas da keyword respondidas nas seções | NÃO |
| H06 | Intenções latentes cobertas no FAQ | NÃO |
| H07 | Último parágrafo referencia a entidade principal (Entity Loop Closure) | NÃO |
| H08 | Dados do cliente usados como evidência de autoridade | NÃO |

---

## DIMENSÃO I — GEO

| ID | Regra | Bloqueante |
|----|-------|-----------|
| I01 | Summarization: `<p class="summarization">` imediatamente após H1 — proibido `<strong>` envolvendo o bloco inteiro como wrapper; `<strong>` em entidades e dados numéricos internos é permitido | SIM |
| I02 | Keyword presente na summarization (primeira ou segunda frase) | SIM |
| I03 | Summarization resume TODO o artigo em 50-60 palavras | SIM |
| I04 | Cada parágrafo-chave autossuficiente como chunk independente | NÃO |
| I05 | Dados numéricos sempre com contexto — nunca número solto | NÃO |
| I06 | Listas e tabelas para dados comparativos | NÃO |

---

## DIMENSÃO J — Meta Description

| ID | Regra | Bloqueante |
|----|-------|-----------|
| J01 | 18-22 palavras | SIM |
| J02 | Entre 70 e 155 caracteres | SIM |
| J03 | Keyword na primeira ou segunda palavra | SIM |
| J04 | Pelo menos 1 dado numérico quando disponível | NÃO |
| J05 | Tom declarativo — proibido: saiba, descubra, confira, aprenda, entenda, veja | SIM |
| J06 | Sem aspas, travessões ou emojis | SIM |
| J07 | Sem reticências no final | SIM |
| J08 | Autossuficiente: faz sentido sem ler o artigo | NÃO |
| J09 | Sentence case — norma portuguesa | SIM |

---

## DIMENSÃO K — H1 e Slug

| ID | Regra | Bloqueante |
|----|-------|-----------|
| K00 | H1: campo entregue como `<h1>Título</h1>` — não plain text | SIM |
| K01 | H1: keyword principal presente no texto interno | SIM |
| K02 | H1: máximo 70 caracteres no texto interno (sem contar a tag) | SIM |
| K03 | H1: sentence case — norma portuguesa | SIM |
| K04 | H1: sem pontuação excessiva (!?, ...) | NÃO |
| K05 | Slug: kebab-case lowercase | SIM |
| K06 | Slug: sem acentos, cedilha, ç | SIM |
| K07 | Slug: máximo 60 caracteres | SIM |
| K08 | Slug: keyword principal incluída | SIM |
| K09 | Slug: sem stopwords desnecessárias (o, a, de, do, da, em, no, na, por, com, que) | NÃO |
| K10 | Slug: NUNCA conter o ano (2024, 2025, 2026...) | SIM |

---

## DIMENSÃO L — FAQ

| ID | Regra | Bloqueante |
|----|-------|-----------|
| L01 | 4-8 perguntas por artigo | SIM |
| L02 | Respostas: 45-60 palavras cada | SIM |
| L03 | Estrutura: h2 (bloco) > h3 (pergunta) > p (resposta) | SIM |
| L04 | Nenhum conector proibido nas respostas (mesma lista D01) | SIM |
| L05 | Cada resposta autossuficiente — funciona como snippet isolado | SIM |
| L06 | Bold em entidades e dados nas respostas | AVISO |
| L07 | Cobertura de intenções latentes não abordadas no corpo | NÃO |
| L08 | Sem pronomes vagos no início das respostas | SIM |

---

## DIMENSÃO PKG — Integridade do Pacote XLSX

| ID | Regra | Bloqueante |
|----|-------|-----------|
| PKG01 | Todos os 6 campos da linha xlsx presentes e não vazios: slug, keyword, h1, sumario_html, meta_description, texto_html | SIM |
| PKG02 | texto_html não começa com wrappers de documento (html, head, body) nem com bloco summarization — deve iniciar em <h1> | SIM |
| PKG03 | FAQ integrado no texto_html como ÚLTIMA seção — NUNCA entregue como campo separado | SIM |
| PKG04 | sumario_html contém o bloco <p class="summarization">...</p> completo com a tag | SIM |

**Regra PKG03 detalhada:**
- O FAQ é escrito pelo seo-writer como parte do HTML (última seção após o último H2 do corpo)
- O output-packager verifica a presença do FAQ no texto_html — não extrai como campo
- O qa-package verifica PKG03 antes de qualquer outro check de conteúdo
- Linha xlsx com FAQ separado = FAIL absoluto independente do resto

**Regra PKG04 detalhada:**
- O sumario_html é extraído pelo output-packager do HTML completo recebido do seo-writer
- Contém o bloco <p class="summarization">...</p> com a tag HTML preservada
- O texto_html não contém o bloco summarization (campos são mutuamente exclusivos)

---

## DIMENSÃO M — Integridade Editorial

| ID | Regra | Bloqueante |
|----|-------|-----------|
| M01 | Sem promessas fantasiosas — nunca garantir resultado que o produto não comprova | SIM |
| M02 | Sem marketing sensacionalista — zero hipérboles sobre o negócio do cliente | SIM |
| M03 | Sem clickbait — títulos e metas descrevem o conteúdo real | SIM |
| M04 | Nunca manipular dados reais para fins de impacto (arredondar, omitir ressalvas, descontextualizar) | SIM |

**Palavras e expressões M02 proibidas:**
```
líder absoluto | o melhor do Brasil | revoluciona o setor | muda sua vida
resultado garantido | oportunidade única | incrível | extraordinário
o único | sem igual | incomparável | exclusivo (quando não verificável)
```

---

## DIMENSÃO QA_CIT — Citações e Fontes

| ID | Regra | Bloqueante |
|----|-------|-----------|
| QA_CIT_001 | Nenhum número ou percentual no corpo sem marcação de fonte (FONTE-INTERNA, FONTE: label, ou CITAÇÃO PENDENTE) | SIM |
| QA_CIT_002 | Se fontes foram citadas no corpo, seção "Referências e fontes" deve estar presente antes do FAQ | SIM |
| QA_CIT_003 | Nenhuma fonte inventada — todas as URLs devem vir das fontes_declaradas ou ser identificadas como "dados internos {empresa}" | SIM |
| QA_CIT_004 | CITAÇÃO PENDENTE presente = aviso ao chief — conteúdo aprovado mas requer verificação humana antes da publicação | AVISO |

---

## DIMENSÃO QP — QA Process (Processo de Revisão)

| ID | Regra | Bloqueante |
|----|-------|-----------|
| QP01 | Agente QA DEVE executar todos os checks da sua dimensão antes de declarar PASS ou FAIL | SIM |
| QP02 | redator-seo-chief NÃO pode avançar gate sem relatório QA formatado com resultado explícito | SIM |
| QP03 | PASS implícito (sem execução de rules) = violação de protocolo equivalente a gate_fail | SIM |

**Aplicação por gate:**
- RS-002-QA (qa-outline): executar A00-A13 antes de declarar resultado
- RS-003-QA (qa-content): executar B01-B11, C01-C07, D01-D09, E01-E05, F01-F08, G01-G06, H01-H08, I01-I06, M01-M04, QA_CIT_001-004, N, O, P antes de declarar resultado
- RS-004-QA (qa-package): executar PKG01-PKG03, J01-J09, K01-K10, L01-L08, M01-M04 antes de declarar resultado

---

## Resumo por Dimensão

| Dimensão | Total | Bloqueantes | Avisos |
|----------|-------|------------|--------|
| A — Outline | 14 | 5 | 1 |
| B — Texto | 11 | 5 | 1 |
| C — Word Count | 7 | 3 | 0 |
| D — Conectores | 9 | 6 | 2 |
| E — Bold | 5 | 2 | 1 |
| F — HTML | 8 | 6 | 0 |
| G — Dados | 6 | 6 | 0 |
| H — E.E.A.T.S. | 8 | 1 | 0 |
| I — GEO | 6 | 3 | 0 |
| J — Meta | 9 | 7 | 0 |
| K — H1/Slug | 10 | 8 | 0 |
| L — FAQ | 8 | 7 | 1 |
| M — Integridade | 4 | 4 | 0 |
| N — Por tipo artigo | variável | variável | variável |
| O — Lead length | 2 | 0 | 2 |
| P — Desambiguação | 1 | 0 | 1 |
| PKG — Integridade | 3 | 3 | 0 |
| QA_CIT — Citações | 4 | 3 | 1 |
| QP — QA Process | 3 | 3 | 0 |
| **TOTAL BASE** | **131+** | **72+** | **10+** |

---

## DIMENSÃO N — Checks por Tipo de Artigo

Executar apenas o bloco do tipo_artigo correspondente à keyword atual.

| Tipo | Bloqueantes | Avisos |
|------|-------------|--------|
| educacional | Definição como 1º H2 | Tabela comparativa, lista <ol> |
| tutorial | Tabela resumo pós H1 | Verbo de ação bold, erros comuns |
| afiliado | Tabela specs, prós E contras | Para quem indicado |
| comparativo | Tabela geral pós H1, seção veredicto | Bold em diferenciais |
| silo | Link em cada H2, anchor descritivo | — |
| citacao | Formato correto, análise após citação | Max 1 por H2 |
| cientifico | Seção metodologia, dados com fonte | Limitações |
| listicle | Número em cada H2 | Critério de seleção |
| news | Data explícita, fonte identificada | — |
| pilar | Tabela conteúdos pós H1, mínimo 6 H2 | Links para relacionados |

---

## DIMENSÃO O — Comprimento do Lead

| ID | Regra | Bloqueante |
|----|-------|-----------|
| O01 | Lead H2: 30-40 palavras (faixa ideal) | AVISO |
| O02 | Lead H3: 25-35 palavras (faixa ideal) | AVISO |

---

## DIMENSÃO P — Desambiguação de Entidade

| ID | Regra | Bloqueante |
|----|-------|-----------|
| P01 | Primeira menção de entidade ambígua: nome + categoria + origem/contexto | AVISO |
