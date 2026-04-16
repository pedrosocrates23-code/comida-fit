# E.E.A.T.S. Framework — Referência Completa

> Framework de contextualização semântica para artigos SEO.
> 7 camadas que cobrem o espaço vetorial esperado por algoritmos modernos e LLMs (GEO/RAG).

---

## O que é o E.E.A.T.S.

O **E.E.A.T.S.** é um framework de construção de contexto para artigos SEO baseado em
**camadas semânticas** progressivas. Cada camada endereça um aspecto diferente da
compreensão algorítmica e humana de um tópico:

| Sigla | Camada | Peso | Função |
|-------|--------|------|--------|
| **E** | Entity Lock-in | 25% | Fixar a entidade principal de forma inequívoca |
| **E** | Essential Entity Set | 15% | Garantir presença das sub-entidades obrigatórias |
| **A** | Attribute Coverage | 15% | Cobrir atributos internos da entidade |
| **T** | Taxonomic/Relational Semantics | 10% | Posicionar a entidade no espaço semântico |
| **S** | Search Intent Completeness | 15% | Cobrir intenções explícitas e latentes |
| **+** | Contextual Embedding | 10% | Criar densidade contextual e citabilidade |
| **+** | Entity Loop Closure | 10% | Fechar o loop semântico e direcionar ação |

---

## Camada 1 — ENTITY LOCK-IN (25%)

### Propósito
Estabelecer a identidade inequívoca da entidade principal nos primeiros 100 palavras do artigo.
O algoritmo precisa reconhecer o que é o artigo antes de qualquer coisa.

### O que deve ter

**Definição-base:**
- Sentença definitória completa: quem/o que é + finalidade + mecanismo central + requisitos + restrições
- Deve ser factualmente correta e verificável
- Evitar linguagem vaga ("pode ser", "às vezes")

**Escopo delimitado:**
- **É:** lista de características definitórias afirmativas
- **Não é:** lista de contrastes críticos (os erros de classificação mais frequentes)

**Diretrizes de implementação:**
- H1 deve conter a entidade principal e delimitar escopo imediatamente
- Primeiro parágrafo: definição + problema central (por que é importante saber)
- Nenhuma seção pode "puxar" o contexto para outro assunto sem retornar à entidade central
- Regra GEO: nomear a entidade explicitamente em parágrafos-chave — nunca pronome vago isolado

### Como gerar
1. Buscar definição nas fontes mais autoritativas do nicho (gov.br, órgãos reguladores, associações)
2. Cruzar com como os top resultados SERP definem a entidade
3. Sintetizar em 2-3 frases densas que capturam: o que é + finalidade + restrição principal

---

## Camada 2 — ESSENTIAL ENTITY SET (15%)

### Propósito
Mapear as sub-entidades que o espaço vetorial **espera encontrar** neste artigo.
Se o melhor artigo sobre "sorteio comercial" menciona "Loteria Federal", "SPA" e "número da sorte",
o seu artigo também precisa — senão ele é semanticamente incompleto.

### Categorias de sub-entidades

| Categoria | Descrição | Profundidade padrão |
|-----------|-----------|-------------------|
| Mecanismo central | Como o processo funciona | Alta |
| Regulador/Órgão competente | Quem autoriza e fiscaliza | Alta |
| Contexto institucional | Onde o regulador se insere | Média |
| Base legal | Lei, decreto, portaria | Alta |
| Co-hipônimo | Modalidade irmã (mesma categoria, diferente tipo) | Média |
| Contexto técnico | Onde/como é executado digitalmente | Média |
| Atributo definidor | Característica que define a entidade | Alta |
| Restrição de elegibilidade | Quem pode ou não usar/realizar | Alta |
| Instrumento de participação | Meio pelo qual o participante interage | Média |

### Como gerar
1. Usar entidades mapeadas por @nebula (frequência ≥3 no SERP)
2. Completar com entidades implícitas conhecidas do domínio
3. Atribuir profundidade com base em centralidade para a keyword

---

## Camada 3 — ATTRIBUTE COVERAGE (15%)

### Propósito
Cobrir os atributos internos da entidade em estrutura de árvore. O algoritmo usa
co-ocorrência de atributos para medir a profundidade e completude do conteúdo.

### Estrutura padrão

```
Entidade: {keyword_principal}
├── Finalidade → marketing, engajamento, vendas, etc.
├── Autorização → obrigatória/opcional, por quem, quando
├── Mecânica → como funciona na prática
├── Gratuidade/Custo → acesso gratuito? venda permitida?
├── Elegibilidade do promotor → PJ, PF, restrições setoriais
├── Elegibilidade do participante → critérios, restrições
├── Base legal → leis, decretos, portarias vigentes
├── Modalidades relacionadas → variantes e sub-tipos
├── Riscos da ausência → multa, suspensão, dano de marca
├── Prazo de execução → timeline típico
├── Canais de execução → digital, PDV, nacional, regional
├── Segmentos usuários → quais setores usam mais
└── Dados mensuráveis → o que pode ser monitorado
```

### Como gerar
- Adaptar galhos ao nicho específico (remover irrelevantes, adicionar específicos)
- Cada galho deve ter ≥1 valor real (não ficar vazio)
- Para nichos regulados: priorizar Autorização, Base legal, Riscos

---

## Camada 4 — RELATIONAL SEMANTICS (10%)

### Propósito
Posicionar a entidade corretamente no espaço taxonômico. Algoritmos e LLMs entendem
entidades por seus relacionamentos — hiperônimo errado = categoria errada.

### Relações obrigatórias

| Relação | Definição | Exemplo aplicado |
|---------|-----------|-----------------|
| **Hiperônimo** | Categoria superior ("é um tipo de...") | Sorteio comercial → promoção comercial |
| **Hipônimos** | Sub-tipos específicos dentro da entidade | Sorteio via Loteria Federal |
| **Co-hipônimos** | Entidades irmãs (mesma categoria, diferente) | Vale-brinde, Concurso comercial |
| **Análogos** | Sinônimos precisos (intercambiáveis) | Campanha promocional, ação regulamentada |
| **Contraste direto** | O que definitivamente não é (erro comum) | Rifa beneficente |
| **Contraste direto 2** | Outra confusão frequente no mercado | Sorteio em redes sociais sem regulamentação |

### Como gerar
1. Identificar a categoria superior (hiperônimo) olhando como o SERP classifica
2. Buscar co-hipônimos: "quais são os tipos de {hiperônimo}?"
3. Identificar contrastes diretos: o que as pessoas confundem com a entidade?

---

## Camada 5 — SEARCH INTENT COMPLETENESS (15%)

### Propósito
Garantir que o artigo responde todas as intenções relevantes — as explícitas (visíveis no SERP)
e as latentes (inferidas, mas presentes na jornada do leitor).

### Tipos de intenção

**Intenções Explícitas (SERP-derived):**
Aparecem como queries frequentes ou PAA (People Also Ask) no SERP.

| Template | Seção típica |
|----------|-------------|
| O que é X | H2 de abertura |
| Como funciona X | H2 explicativo |
| Tipos de X | H2 comparativo |
| Lei/regulamentação de X | H2 legal |
| Como fazer X | H2 passo a passo |
| O que acontece sem X | H2/H3 de risco |
| X vs Y | Seção de contraste |
| Quem pode fazer X | H3 dentro de mecânica |

**Intenções Latentes (inferidas):**
Não aparecem como query explícita, mas estão implícitas na jornada de pesquisa.

| Intenção Latente | Sinal | Como cobrir |
|-----------------|-------|------------|
| Custo | "quanto custa" | Orientar para contato, mencionar variáveis |
| Prazo | "quanto tempo leva" | Mencionar prazo típico do processo |
| Segmento | "meu setor pode" | Exemplos por segmento |
| Exemplos reais | "quem já fez" | Cases documentados |
| Como escolher | "fornecedor", "empresa" | Seção CTA natural |
| Posso fazer em redes sociais | Pergunta comum | Nota de cuidado |

---

## Camada 6 — CONTEXTUAL EMBEDDING (10%)

### Propósito
Criar a densidade contextual que distingue conteúdo profundo de conteúdo raso.
Maximiza citabilidade por LLMs (GEO/RAG) através de frases com entidade nomeada.

### Elementos obrigatórios

**Exemplos práticos documentados:**
- Empresas reais que usam/usaram a entidade (com nomes quando possível)
- Cases específicos com números (quando disponíveis e verificáveis)
- Fonte ou referência para cada case

**Cenários de aplicação por segmento:**
- Como a entidade se aplica em cada setor relevante do cliente
- Formato: "No segmento [setor], [entidade] funciona assim: [cenário]"

**Erros comuns:**
- Erros frequentes identificados no SERP e no mercado
- Consequências de cada erro
- Como evitar

**Boas práticas:**
- Recomendações verificáveis e aplicáveis
- Conectar com diferenciais do cliente quando relevante

**Referências legítimas:**
- gov.br, órgãos reguladores, associações setoriais
- Publicações acadêmicas ou especializadas
- Leis e decretos (com número e ano)

**Frases GEO-citáveis:**
- Estrutura: "[Entidade nomeada] [verbo/relação] [fato/atributo]."
- Sem pronome vago isolado ("isso", "ele", "ela")
- Curtas o suficiente para ser extraída por LLM (≤30 palavras)
- Factualmente corretas e verificáveis

---

## Camada 7 — ENTITY LOOP CLOSURE (10%)

### Propósito
Fechar o loop semântico: o leitor que chegou com uma dúvida deve sair com
clareza + direção de ação. O algoritmo lê o fechamento para confirmar que
o artigo é sobre o que prometeu ser.

### O que deve ter

1. **Reafirmação da entidade:** nomear novamente a entidade com posicionamento estratégico
2. **Síntese dos atributos principais:** bullet points dos 4-6 atributos mais críticos
3. **Conexão com intenção inicial:** "quem chegou querendo [saber X] agora sabe [Y]"
4. **Direção para ação:** CTA natural para o cliente (sem pressão, sem urgência forçada)
5. **Regra:** NÃO introduzir entidades novas no fechamento

### CTA ideal
- Natural, não forçado
- Conectado ao expertise do cliente
- Com link para página específica (não homepage genérica)
- Com aviso legal quando aplicável

---

## Saídas Complementares

### Termos LSI Obrigatórios

**Clusters:**

| Cluster | Prioridade | O que contém |
|---------|-----------|-------------|
| Regulatório | Alta (nichos regulados) | Termos legais, normativos, de conformidade |
| Mecânico | Alta | Como funciona, processo, ferramentas |
| Risco/Conformidade | Média | Erros, penalidades, irregularidades |
| Execução | Média | Implementação, fornecedores, plataformas |
| Comercial | Baixa | Conversão, contratar, preço |

**Regra de inclusão:** Termo aparece em ≥2 resultados SERP relevantes OU é um
termo técnico do nicho com alta probabilidade semântica.

### Power Keywords por Posição

| Posição | Power Words | Propósito |
|---------|------------|-----------|
| H1/Título | "como funciona de verdade", "tudo o que você precisa saber" | Capturar intenção informacional |
| H2 Risco | "erros comuns", "o que evitar", "riscos reais" | Urgência e cautela |
| H2 Diferenciação | "diferença entre", "o que muda na prática" | Comparação e clareza |
| H2 Procedimento | "passo a passo", "processo estruturado" | Orientação prática |
| Intenção latente | "vale a pena", "quando usar" | Decisão e avaliação |
| CTA/Fechamento | "solução confiável", "casos reais", "método validado" | Confiança e conversão |

### Estrutura de Outline Padrão

```
H1: {titulo_otimizado_com_keyword}
[Lead GEO — 2-3 frases citáveis: definição + problema + mecanismo]

H2: O que é {keyword}
  H3: O que diferencia {keyword} de {co-hipônimo 1} e {co-hipônimo 2}

H2: Como funciona {keyword} na prática
  H3: O papel de {mecanismo central}
  H3: Como {atributo mecânico} funciona
  H3: Quem pode realizar {keyword}

H2: Modalidades de {categoria superior}: comparativo
  [Tabela comparativa das modalidades]

H2: Base legal de {keyword} no Brasil
  H3: {lei principal} e {decreto}
  H3: O papel de {órgão regulador}
  H3: O que acontece sem {requisito obrigatório}

H2: Como executar {keyword} passo a passo
  H3: {passo 1 — planejamento}
  H3: {passo 2 — estrutura técnica}
  H3: {passo 3 — lançamento}

H2: Exemplos reais de {keyword} por segmento
  [Varejo | Financeiro | Energia | Alimentício | etc.]

H2: Erros comuns em {keyword} (e como evitar)

H2: Como {empresa_cliente} estrutura {keyword}
  [CTA com aviso legal]

FAQ — mínimo 5 perguntas com respostas diretas
```

---

## Aviso Legal (Modelo)

Incluir no rodapé ou nota do artigo quando o cliente elabora estrutura técnica/regulatória,
mas a responsabilidade legal é do contratante:

```
"{Nome da empresa} é especializada no desenvolvimento de {produto/serviço}. 
Não promovemos, organizamos ou realizamos {entidade/campanha} próprias. 
Toda responsabilidade legal, execução e operação das campanhas é de 
responsabilidade do contratante."
```

---

*E.E.A.T.S. Framework v1.0 — SEO Contextualizador Squad*
