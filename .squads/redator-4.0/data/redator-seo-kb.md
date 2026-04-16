# SEO Producer Knowledge Base

**Squad:** redator-seo
**Versão:** 1.0.0
**Propósito:** Resumo dos frameworks e regras essenciais para consulta rápida dos agentes

> Para referência completa, consultar os arquivos em `redator-2.0/knowledge/`

---

## 1. Frameworks Centrais

### E.E.A.T.S. (Entity-Encoded Article Topical Structure)

7 camadas semânticas ponderadas que modelam como o Google avalia conteúdo:

| Camada | Peso | O que avalia |
|--------|------|-------------|
| Entity Lock-in | 25% | Entidade principal fixada nos primeiros 100 palavras |
| Essential Entity Set | 15% | Subentidades obrigatórias do espaço vetorial |
| Attribute Coverage | 15% | Atributos internos da entidade (modelo EAV) |
| Relational Semantics | 10% | Posição no espaço taxonômico (hiperônimos, hipônimos) |
| Intent Completeness | 15% | Intenções explícitas e latentes respondidas |
| Contextual Embedding | 10% | Densidade contextual (exemplos, cenários, erros) |
| Entity Loop Closure | 10% | Fechamento que reforça a entidade principal |

**Referência completa:** `redator-2.0/knowledge/02_KNOWLEDGE_BASE.md`

---

### GEO (Generative Engine Optimization)

Otimização para citação por LLMs (ChatGPT, Perplexity, AI Overviews):

- Summarization de 50-60 palavras após H1
- Cada parágrafo-chave autossuficiente (chunk independente)
- Entidade nomeada (sem pronomes vagos)
- Dados quantificados com contexto
- Listas e tabelas estruturadas

---

### PMR19 — 18 Premissas de Produção Semântica

Referência: `redator-2.0/knowledge/Premissas.md`

Destaques críticos:
1. Estrutura lógica do macro ao micro
4. Escaneabilidade: títulos claros, listas, **parágrafos de 2-3 linhas** (não 3-4)
9. Frases enxutas, sem redundância
17. Primeiro parágrafo resume o tema e o propósito da seção
18. Cada subtítulo inicia com frase-resumo clara do bloco

**Regras de estrutura atualizadas:**
- H3 é **obrigatório no corpo** — o artigo deve ter ao menos 1 H3 fora do FAQ. Seções com tipologia, etapas ou componentes usam H3. Máximo **3 H3** por H2. Artigo sem nenhum H3 no corpo = violação bloqueante.
- Títulos H2/H3 em **sentence case**: apenas primeira letra + nomes próprios em maiúscula
- GEO: entidade nomeada explicitamente no **lead** de cada H2/H3; pronomes contextuais ("a rede", "o modelo") são aceitáveis no corpo da seção para evitar repetição

---

## 2. Regras de Estilo — Proibições Absolutas

Referência: `redator-2.0/knowledge/restricao.md`

### Conectores Banidos

```
Além disso | Portanto | Dessa forma | Assim sendo | Em suma
Logo | Por fim | Ou seja | Nesse sentido | Vale ressaltar
É importante destacar | Saiba mais | Confira
```

### Formatação Proibida

- Títulos em CAIXA ALTA
- Travessões como conectores
- Emojis no texto
- Frases inteiras em bold
- Tags: section, div, article, aside, span, br, hr, img, h4+

---

## 3. Tipos de Artigo

| Tipo | Comando | Funil | Word Count |
|------|---------|-------|------------|
| Educacional | /educacional | Topo | 1.500-2.500 |
| Tutorial | /tutorial | Meio | 1.800-3.000 |
| Afiliado | /afiliado | Fundo | 1.500-2.500 |
| Comparativo | /comparativo | Meio/Fundo | 1.500-2.000 |
| Silo Page | /silo | Topo/Meio | 2.000-3.000 |
| Científico | /cientifico | Meio | 2.000-3.500 |
| Listicle | /listicle | Topo/Meio | 1.800-3.500 |
| News | /news | Topo | 1.200-2.000 |
| Pilar | /pilar | Todos | 2.500-4.000 |

**Referência completa:** `redator-2.0/knowledge/03_ARTICLE_TEMPLATES.md`

---

## 4. Lead GEO — Fórmula

```
[SUJEITO ESPECÍFICO] + [VERBO DE AÇÃO] + [QUANTIFICAÇÃO] + [CONTEXTO] + [RELEVÂNCIA]
```

**BOM:** "A franquia Peggô Market opera mais de 350 unidades em 12 estados, com faturamento médio de R$ 25.000 por loja e payback entre 8 e 12 meses."

**RUIM:** "Existem muitas opções de franchising no mercado."

---

## 5. HTML — Tags Permitidas

```
h1, h2, h3, p, ul, ol, li, strong,
table, thead, tbody, tr, th, td, a
```

Classe permitida: apenas `summarization`

---

## 6. Deliverables — Regras Rápidas

| Deliverable | Formato | Regra Crítica |
|-------------|---------|---------------|
| Meta Description | plain text | 18-22 palavras, keyword-first |
| H1 | plain text | máx. 70 chars, keyword presente |
| Slug | kebab-case | máx. 60 chars, sem acentos |
| FAQ | HTML (h2/h3/p) | 4-8 perguntas, respostas autossuficientes |
| HTML Content | HTML limpo | sem wrappers, com summarization |

---

## 7. Gates de Qualidade

| Gate | Fase | Blocking | Critério Principal |
|------|------|----------|--------------------|
| SP-000 | Pre-check | SIM | Cliente + contexto existem |
| SP-001 | Keyword intake | SIM | Keywords classificadas |
| SP-002 | Outline | SIM | 4+ H2, distância ≤ 3 |
| SP-003 | Conteúdo | SIM | HTML + zero conectores proibidos |
| SP-004 | Pacote | SIM | 5 deliverables completos |

---

## 8. Clientes Configurados

| Slug | Arquivo | Empresa |
|------|---------|---------|
| peggo | `redator-2.0/knowledge/peggo-marketing.md` | Peggô Market |

Para adicionar novo cliente: criar `{slug}-marketing.md` em `redator-2.0/knowledge/`
