# Task: Pesquisar Tópico

**Command:** `*pesquisar-topico {keyword} [{titulo}]`
**Execution Type:** Auto (WebSearch)
**Executor:** @nebula
**Ferramentas:** WebSearch, WebFetch

## Propósito

Executar pesquisa web completa sobre uma keyword SEO para coletar:
inteligência SERP, entidades co-ocorrentes, termos LSI, dados recentes (2025-2026),
intenções latentes, e frases GEO-citáveis. Output é usado diretamente por @atlas.

## Workflow

### Fase 1: Queries de SERP (5 buscas obrigatórias)

Executar as seguintes buscas em sequência usando WebSearch:

```
Query 1 (definição):     "{keyword}"
Query 2 (atual):         "{keyword} 2025 2026"
Query 3 (legal/nicho):   "{keyword} regulamentação lei decreto" (adaptar ao nicho)
Query 4 (como fazer):    "como {keyword} funciona passo a passo"
Query 5 (vs/diferença):  "{keyword} diferença {co-hipônimo provável}"
```

**Ação por resultado:**
- Registrar: título, URL, snippet
- Extrair entidades mencionadas no snippet
- Identificar intenção do resultado (informacional/transacional/comercial)

#### >>> CHECKPOINT: Volume de resultados <<<

```yaml
checkpoint_volume:
  question: "Encontrou ≥10 resultados relevantes no total das 5 queries?"
  if_sim: "Prosseguir para fase 2"
  if_nao: "Tentar queries alternativas com variações do keyword + reportar a @maestro"
  threshold: 10
```

### Fase 2: Extração de Entidades

Para cada resultado encontrado:

1. Ler o snippet completo
2. Identificar entidades nomeadas:
   - Organizações e órgãos (ex: "SPA", "Ministério da Fazenda")
   - Leis e decretos (ex: "Lei nº 5.768/1971")
   - Termos técnicos específicos do nicho
   - Modalidades e sub-categorias
3. Contar frequência: entidade aparece em quantos resultados?
4. Classificar categoria: regulador | base legal | mecanismo | co-hipônimo | etc

**Threshold de inclusão:** ≥3 aparições = sub-entidade obrigatória

#### >>> CHECKPOINT: Qualidade das entidades <<<

```yaml
checkpoint_entidades:
  question: "Extraiu ≥8 entidades distintas com frequência verificável?"
  if_sim: "Prosseguir"
  if_nao: "Buscar mais resultados ou usar WebFetch nos top 3 para análise profunda"
```

### Fase 3: Busca de Dados Recentes (Abril 2026)

Executar buscas específicas para atualidade:

```
Query A: "{keyword} novidades 2025 2026"
Query B: "{nicho do keyword} tendências 2026"
Query C: "{órgão regulador do nicho} portaria decreto 2025 2026" (se nicho regulado)
Query D: "estatísticas {keyword} Brasil 2025"
```

**Extrair:**
- Dados numéricos com fonte
- Mudanças regulatórias recentes
- Cases e exemplos novos
- Tendências emergentes

### Fase 4: Coleta de LSI Terms

Analisar os snippets dos top 10 resultados e extrair termos por cluster:

**Cluster Regulatório** (alta prioridade em nichos regulados):
- Termos legais, normativos, de conformidade
- Ex: "autorização prévia", "regulamentação vigente", "órgão competente"

**Cluster Mecânico** (alta prioridade):
- Como funciona, processo, ferramentas, plataformas
- Ex: "cadastro", "número da sorte", "extração", "hotsite"

**Cluster de Risco/Conformidade** (média prioridade):
- Erros, penalidades, cuidados
- Ex: "campanha suspensa", "multa", "ilegal", "sem autorização"

**Cluster de Execução** (média prioridade):
- Implementação, fornecedores, plataformas
- Ex: "estrutura técnica", "regulamento personalizado", "dashboard"

**Cluster Comercial** (baixa prioridade):
- Conversão, contratar, preço
- Ex: "como contratar", "empresa especializada", "fornecedor"

**Meta:** ≥5 termos por cluster, ≥25 termos no total

### Fase 5: Perguntas PAA e Intenções Latentes

Buscar:
```
Query: "perguntas sobre {keyword}"
Query: "dúvidas frequentes {keyword}"
```

Também analisar os snippets para identificar padrões de pergunta do tipo:
- "Quanto custa..."
- "Quanto tempo..."
- "Posso fazer..."
- "É obrigatório..."
- "Qual a diferença..."

**Classificar cada pergunta como:** intenção latente | intenção explícita

### Fase 6: Frases GEO-Citáveis

Extrair ou construir 3-5 frases que:
- Nomeiam a entidade principal explicitamente (sem pronome isolado)
- Contêm um atributo, ação ou fato verificável
- São curtas o suficiente para serem citadas por LLMs (< 30 palavras)

**Estrutura:** "[Entidade] é/exige/funciona [atributo/ação] [contexto]"

## Output Format

```markdown
## Research Findings: {keyword}
**Data da pesquisa:** {data}
**Título analisado:** {titulo}
**Total de resultados analisados:** {N}

### 1. Panorama SERP
- **Intenção dominante:** informacional
- **Top 3 resultados:**
  1. [{titulo}]({url}) — cobre: {o que cobre}
  2. ...
- **Gaps nos top resultados:** {o que falta}

### 2. Entidades Mapeadas
| Entidade | Categoria | Freq. SERP | Profundidade sugerida |
|----------|-----------|-----------|----------------------|
| ...      | ...       | {N}/10    | Alta/Média/Baixa     |

### 3. Termos LSI por Cluster
**Cluster Regulatório (alta prioridade):**
[lista separada por vírgulas]

**Cluster Mecânico (alta prioridade):**
[lista]

**Cluster Risco/Conformidade (média prioridade):**
[lista]

**Cluster Execução (média prioridade):**
[lista]

**Cluster Comercial (baixa prioridade):**
[lista]

### 4. Dados Recentes (2025-2026)
- {dado} — Fonte: [{fonte}]({url})
- {dado} — Fonte: [{fonte}]({url})

### 5. Perguntas e Intenções Latentes
| Pergunta/Intenção | Tipo | Seção sugerida |
|-------------------|------|---------------|
| Quanto custa fazer {keyword}? | Latente | Mencionar ticket médio, orientar contato |
| ...                           | ...     | ...                                       |

### 6. Frases GEO-Citáveis
- "[Entidade] [atributo/ação] [contexto]."
- "[Entidade] [atributo/ação] [contexto]."
- "[Entidade] [atributo/ação] [contexto]."
```

## Validação de Saída

- [ ] ≥5 queries executadas via WebSearch
- [ ] ≥10 resultados analisados no total
- [ ] ≥8 entidades identificadas com frequência
- [ ] ≥25 termos LSI em ≥4 clusters
- [ ] ≥2 dados recentes (2025-2026) com fonte
- [ ] ≥3 frases GEO-citáveis
- [ ] Output estruturado pronto para @atlas
