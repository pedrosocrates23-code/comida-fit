# Task: Gerar Briefing E.E.A.T.S.

**Command:** `*gerar-briefing {keyword} {titulo} [--empresa=path] [--research=findings]`
**Execution Type:** Hybrid (Atlas executa, humano valida saída)
**Load:** `data/eatss-framework.md`, `data/lsi-taxonomy.md`, `templates/briefing-eatss-tmpl.md`
**Executor:** @atlas

## Propósito

Gerar o briefing contextual E.E.A.T.S. completo para um artigo SEO, combinando:
- Keyword + Título fornecidos pela planilha
- Contexto da empresa cliente (data/contexto-empresa-ativo.md)
- Research findings de @nebula
- Framework E.E.A.T.S. (7 camadas)

O output vai diretamente para a coluna "Prompt Adicional" da planilha.

## Inputs Necessários

```yaml
inputs:
  obrigatorios:
    keyword: "Palavra-chave foco (da planilha, col B)"
    titulo: "Título proposto do artigo (da planilha, col C)"
    contexto_empresa: "Conteúdo de data/contexto-empresa-ativo.md"
    research_findings: "Output de *pesquisar-topico (de @nebula)"
  opcionais:
    idioma: "Idioma do artigo (default: Português Brasil)"
    categoria: "Categoria do post (para contextualizar CTA)"
    url_silo: "URL da página de silo do cliente (para CTA)"
```

## Workflow

### Fase 0: Análise de Inputs

1. Ler `data/contexto-empresa-ativo.md` — extrair:
   - Nome da empresa
   - Especialização e posicionamento
   - Tom de comunicação
   - Segmentos atendidos
   - Aviso legal obrigatório
   - URL do site (para CTA)
2. Revisar research findings de @nebula — extrair:
   - Entidades mapeadas (para C2)
   - LSI terms por cluster (para saída final)
   - Dados recentes (para C6)
   - Intenções latentes (para C5)
   - Frases GEO-citáveis (para C6)

#### >>> CHECKPOINT: Inputs completos <<<

```yaml
checkpoint_inputs:
  question: "Contexto empresa E research findings disponíveis?"
  if_sim: "Prosseguir com geração das 7 camadas"
  if_nao: "PARAR — identificar o que falta e solicitar ao usuário/orchestrador"
  bloqueante: true
```

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

**Gerar:**

1. **Definição-base precisa** da entidade principal (keyword):
   - Incluir: finalidade, mecanismo central, restrições legais, quem pode usar
   - Estrutura: "[Entidade] é [definição completa com atributos essenciais]"

2. **Escopo delimitado:**
   - É (lista de características definitórias)
   - Não é (lista de contrastes críticos — erros comuns de confusão)

3. **Diretrizes de implementação:**
   - H1: deve conter entidade principal + delimitar escopo
   - Primeiro parágrafo: definição + problema central (por que importa saber isso)
   - Regra de referência: nomear entidade explicitamente em parágrafos-chave

#### >>> CHECKPOINT: Precisão da definição <<<

```yaml
checkpoint_definicao:
  question: "A definição captura com precisão O QUE É e O QUE NÃO É a entidade?"
  if_precisa: "Prosseguir para C2"
  if_vaga: "Refinar — usar fontes das research findings para especificar"
  rationale: "Entity lock-in fraco = artigo que não ranqueia para a keyword"
```

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

**Gerar tabela com sub-entidades obrigatórias:**

Usar como base as entidades de @nebula + complementar com conhecimento do domínio.

```markdown
| Sub-entidade | Categoria | Profundidade esperada |
|-------------|-----------|----------------------|
| [nome]      | [tipo]    | Alta/Média/Baixa     |
```

**Regras:**
- Mínimo 8 sub-entidades
- Cada sub-entidade deve ter categoria clara
- Profundidade reflete importância semântica para a keyword
- Justificar brevemente por que cada uma é obrigatória

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

**Gerar árvore hierárquica de atributos:**

```
Entidade: {keyword_principal}
├── Finalidade → [valores possíveis]
├── Autorização → [quem autoriza, como, quando]
├── Mecânica → [como funciona na prática]
├── Gratuidade/Custo → [estrutura de acesso]
├── Elegibilidade → [quem pode realizar/usar]
├── Base legal → [leis, decretos, portarias]
├── Modalidades relacionadas → [variantes/sub-tipos]
├── Riscos da ausência → [consequências de não cumprir]
├── Prazo de execução → [timing típico]
├── Canais de execução → [onde acontece]
├── Segmentos usuários → [quais setores usam]
└── Dados mensuráveis → [o que pode ser medido]
```

Adaptar os galhos para o nicho específico da keyword.

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

**Gerar tabela de posicionamento taxonômico:**

```markdown
| Relação | Entidade | Como trabalhar no artigo |
|---------|----------|------------------------|
| Hiperônimo | [categoria superior] | "X é uma das modalidades de Y" |
| Hipônimos | [sub-tipos] | Explicar mecanismo específico |
| Co-hipônimos | [entidades irmãs] | Seção dedicada às diferenças |
| Análogos | [sinônimos precisos] | Termos intercambiáveis com precisão |
| Contraste direto | [o que NÃO é] | Distinção legal e de finalidade |
| Contraste direto 2 | [confusão frequente] | Alto risco para o leitor |
```

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

**Gerar tabela de intenções explícitas (SERP-derived):**

Usar PAA e queries de @nebula para preencher:

```markdown
| Intenção | Template de query | Seção sugerida |
|----------|------------------|---------------|
| Definição | O que é {keyword} | H2 de abertura |
| Mecanismo | Como funciona {keyword} | H2 explicativo |
| Tipologia | Tipos de {keyword} | H2 comparativo |
| Base legal | Lei do {keyword} | H2 regulatório |
| Procedimento | Como fazer {keyword} | H2 passo a passo |
| Risco | O que acontece sem {atributo obrigatório} | H2/H3 de risco |
| Diferenciação | {keyword} vs {co-hipônimo} | Seção de contraste |
| Elegibilidade | Quem pode fazer {keyword} | H3 dentro de mecânica |
```

**Gerar tabela de intenções latentes (inferidas):**

```markdown
| Intenção Latente | Gap se ausente | Seção sugerida |
|-----------------|---------------|---------------|
| Quanto custa {keyword} | Perde conversão de fundo de funil | Menção ao investimento, orientar contato |
| Quanto tempo leva | Intenção prática — planejamento | H3 dentro de procedimento |
| Quais segmentos podem | Intenção investigativa | Exemplos por setor |
| Exemplos reais | Prova social | Seção de cases |
| Como escolher fornecedor | Intenção de conversão | Seção final com CTA |
```

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

Usar cases e dados de @nebula + contexto da empresa:

**Gerar:**
- Exemplos práticos documentados (empresas/casos reais do nicho)
- Cenários de aplicação por segmento (usando segmentos do contexto empresa)
- Erros comuns (extraídos de SERP + conhecimento do domínio)
- Boas práticas (do contexto empresa + SERP)
- Referências legítimas (fontes autoritativas identificadas por @nebula)
- 3-5 frases GEO-citáveis (entidade nomeada, sem pronome vago)

**Estrutura das frases GEO:**
```
"[Entidade principal nomeada] [verbo/relação] [atributo/fato verificável]."
```

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

**Gerar instruções de fechamento:**

1. Reafirmar a entidade: "[keyword] como [posicionamento estratégico]"
2. Sintetizar atributos principais (lista dos mais críticos de C3)
3. Conectar com intenção inicial: leitor que chegou com [intenção] agora sabe [resultado]
4. Direção para ação: CTA natural para a empresa cliente
5. Regra: não introduzir entidades novas no fechamento

---

### Fase Final: Saídas Complementares

**TERMOS LSI OBRIGATÓRIOS** (para coluna "Termos LSI" da planilha):

Usar os clusters de @nebula + completar:

```
Cluster [nome] (alta/média/baixa prioridade):
[termo1, termo2, termo3, ...]
```

Mínimo 4 clusters, mínimo 25 termos totais.

**POWER KEYWORDS:**

```
H1/título: [sugestões de power words para o H1]
H2 de risco/conformidade: [palavras de impacto para seções de risco]
H2 de diferenciação: [palavras para seções comparativas]
H2 de procedimento: [palavras para seções de passo a passo]
Seção de intenção latente: [palavras para seções de valor latente]
CTA/fechamento: [palavras para conversão e confiança]
```

**ESTRUTURA DE OUTLINE SUGERIDA:**

```
H1: {titulo_otimizado}
[Lead GEO — 2-3 frases citáveis]
H2: [H2 de definição]
  H3: [diferenciação crítica]
H2: [H2 de mecanismo]
  H3: [sub-aspecto 1]
  H3: [sub-aspecto 2]
  H3: [quem pode realizar]
H2: [H2 comparativo de modalidades]
  [Tabela comparativa]
H2: [H2 de base legal]
  H3: [legislação base]
  H3: [órgão regulador]
  H3: [risco sem autorização]
H2: [H2 de procedimento/passo a passo]
  H3: [passo 1]
  H3: [passo 2]
  H3: [passo 3]
H2: [H2 de exemplos por segmento]
H2: [H2 de erros comuns]
H2: [H2 de CTA — empresa cliente]
FAQ (mínimo 5 perguntas)
```

**RESTRIÇÕES E DIRETRIZES EDITORIAIS:**

```
SEMPRE fazer:
- [lista de obrigações específicas para esta keyword/nicho]

NUNCA fazer:
- [lista de proibições — incluindo termos proibidos, afirmações incorretas]

Aviso legal obrigatório:
- [extraído do contexto da empresa]
```

**SEÇÃO DE CTA** (usando dados do contexto empresa):

```
URL do silo: {url_pagina_cliente}
Posição: H2 final do artigo, antes do FAQ
Título da seção: {titulo_cta}
Conteúdo: {o que mencionar — especialização, diferenciais}
Frase de fechamento sugerida: {frase}
CTA final: {link âncora para formulário}
Texto do botão/link: Fale com nosso time
Tom: {extraído do contexto empresa}
Aviso legal: {aviso obrigatório do cliente}
```

---

#### >>> CHECKPOINT: Completude do briefing <<<

```yaml
checkpoint_completude:
  question: "Todas as 7 camadas estão preenchidas com conteúdo substantivo e específico?"
  checklist:
    - "C1: Definição-base + escopo + diretrizes"
    - "C2: Tabela com ≥8 sub-entidades"
    - "C3: Árvore com ≥10 atributos"
    - "C4: Tabela relacional com ≥5 relações"
    - "C5: Tabela explícita (≥7) + latente (≥5)"
    - "C6: Exemplos + erros + boas práticas + frases GEO"
    - "C7: Síntese + CTA + aviso"
    - "LSI: ≥25 termos em ≥4 clusters"
    - "Outline: H1 + ≥6 H2s com H3s"
    - "Restrições: SEMPRE/NUNCA + aviso legal"
  if_completo: "Formatar output final para planilha"
  if_incompleto: "Completar camadas faltantes antes de finalizar"
```

## Formatação Final

O output final deve ser formatado como:

```markdown
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** {keyword}
**Tipo de artigo:** {tipo baseado no Post Type da planilha}
**Funil:** {topo/meio/fundo baseado na intenção}
**Objetivo estratégico:** {objetivo baseado no contexto empresa}

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)
[conteúdo gerado]

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)
[conteúdo gerado]

...

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)
[conteúdo gerado]

---

## TERMOS LSI OBRIGATÓRIOS
[clusters]

## POWER KEYWORDS APLICÁVEIS
[por posição]

## ESTRUTURA DE OUTLINE SUGERIDA
[H1 → H2s → H3s → FAQ]

## RESTRIÇÕES E DIRETRIZES EDITORIAIS
[SEMPRE/NUNCA/Aviso legal]
```

## Validação de Saída

- [ ] 7 camadas E.E.A.T.S. presentes
- [ ] Contexto da empresa integrado (tom + segmentos + aviso legal)
- [ ] Research findings de @nebula referenciados
- [ ] ≥25 termos LSI em ≥4 clusters (para coluna "Termos LSI")
- [ ] Outline com H1/H2s/H3s/FAQ
- [ ] Restrições SEMPRE/NUNCA preenchidas
- [ ] Aviso legal do cliente incluído
- [ ] CTA com URL e dados da empresa
- [ ] Pronto para escrever na planilha via *escrever-planilha
