# KNOWLEDGE BASE -- Fundamentos Tecnicos e Frameworks

## 1. FRAMEWORK E.E.A.T.S. (Entity-Encoded Article Topical Structure)

Framework de 7 camadas semanticas ponderadas. Modela o que o Google faz internamente: detectar entidades, identificar relacoes, avaliar completude, gerar embeddings, comparar com o subgrafo ideal do topico.

### Camada 1: Entity Lock-in (peso 25%)

Cria o embedding inicial que fixa a entidade-alvo de forma inequivoca.

**Checklist:**
- Entidade principal nomeada nos primeiros 100 palavras
- Definicao curta e precisa (1-2 frases)
- Escopo delimitado (o que e / o que nao e)
- Intencao primaria estabelecida
- Problema central identificado

**Erros comuns:** Misturar temas na mesma pagina. Secoes genericas listando multiplos assuntos. Abrir blocos sobre outros procedimentos.

**Impacto:** Responsavel por ~50% da coerencia do embedding final. Sem Entity Lock-in claro, o modelo seleciona vetor base incorreto.

### Camada 2: Essential Entity Set (peso 15%)

Introduz subentidades obrigatorias que o espaco vetorial espera.

**Categorias de entidades essenciais:**
- **Partes:** componentes estruturais da entidade principal
- **Categorias:** classificacoes e taxonomias
- **Contextos:** ambientes onde a entidade opera
- **Mecanismos:** como a entidade funciona
- **Atributos fundamentais:** propriedades definidoras

**Impacto:** Ausencia de entidades essenciais indica ao Google que o conteudo carece de "semantic depth".

### Camada 3: Attribute Coverage (peso 15%)

Preenche o vetor com atributos internos da entidade usando modelo EAV.

**Tipos de atributos:**
- Caracteristicas fundamentais (qualidades intrinsecas)
- Classificacoes e tipos (categorizacao formal)
- Parametros tecnicos (especificacoes)
- Variantes conhecidas (diferentes formas)
- Propriedades mensuraveis (dados quantificaveis)
- Requisitos e restricoes (regras, limites)

**Impacto:** Atributos sao nos importantes no subgrafo. Densidade de atributos = precisao do embedding.

### Camada 4: Relational Semantics (peso 10%)

Posiciona a entidade no espaco taxonomico.

**Relacoes:**
- **Hiperonimo:** categoria superior (IS-A parent) -- ex: poodle -> cachorro
- **Hiponimos:** subtipos (IS-A children) -- ex: cachorro -> poodle, labrador
- **Co-hiponimos:** irmaos na mesma categoria -- ex: poodle, labrador (ambos cachorros)
- **Analogos:** entidades comparaveis -- ex: gato (animal domestico como cachorro)
- **Antonimos/Contrastes:** opostos -- ex: animal domestico vs animal selvagem

**Impacto:** Embeddings do Google sao relacionais. Relacoes explicitas fortalecem posicionamento no Knowledge Graph.

### Camada 5: Intent Completeness (peso 15%)

Responde todas as intencoes, explicitas e latentes.

**Intencoes explicitas (SERP-derived):**
- O que e X (definicao)
- Como funciona X (mecanismo)
- Como fazer X (procedimento)
- Tipos de X (tipologia)
- Exemplos de X (exemplificacao)
- Vale a pena X (avaliacao)
- X vs Y (comparacao)
- Quanto custa X (custo)

**Intencoes latentes (inferidas):**
- Como escolher
- Erros comuns
- Limitacoes
- Alternativas
- Requisitos previos
- Quando nao usar

**Impacto:** Responder intencoes latentes separa conteudos genericos de conteudos com topical authority real.

### Camada 6: Contextual Embedding (peso 10%)

Cria densidade contextual que estabiliza o embedding.

**Elementos:** exemplos praticos, cenarios de aplicacao, erros comuns, boas praticas, passo a passo, referencias legitimas.

**Verbalizacao:** cobrir a taxonomia de frases do nicho sem repetir. Usar sinonimos, reformulacoes e padroes de frase distribuidos em headings, paragrafos e FAQ.

**Impacto:** Contexto aumenta similaridade semantica, completude e chance de Featured Snippet.

### Camada 7: Entity Loop Closure (peso 10%)

Fechamento que reforca a entidade principal e cria coerencia vetorial.

**Checklist:**
- Entidade principal reafirmada
- Atributos principais sintetizados
- Conexao com intencao inicial explicita
- Direcao para acao (quando aplicavel)
- Nao introduz entidades novas no fechamento

**Impacto:** Fechamento coerente diminui divergencias semanticas e consolida o vetor final.

### Score E.E.A.T.S. Benchmarks

| Score | Classificacao | Significado |
|-------|-------------|-------------|
| 9-10 | Exemplar | Modela o subgrafo ideal do topico |
| 7-8 | Avancado | Poucos gaps, alta probabilidade de ranking |
| 5-6 | Intermediario | Gaps identificaveis, otimizacao necessaria |
| 3-4 | Basico | Estrutura semantica fraca, requer reescrita |
| 1-2 | Critico | Nao atende requisitos minimos |

---

## 2. LSE (Latent Semantic Entities)

### O que e

Abstracao conceitual representando embeddings de entidades, passagens, atributos, topicos e intencoes no espaco vetorial.

### Onde atua

Embutido dentro de BERT, RoBERTa, MUM, RankBrain, Passage Ranking, Knowledge Graph embeddings e modelos de similaridade semantica.

O LSE explica como o Google:
- Entende o topico de um conteudo
- Identifica entidades centrais e secundarias
- Mede cobertura semantica
- Detecta lacunas de topicos
- Mapeia relacoes conceituais

### Onde termina

LSE NAO avalia: qualidade humana (camada 4), reputacao/autoridade (camada 5), comportamento do usuario (camada 6), estrutura do site (sinal externo). Boa arquitetura de site amplifica o impacto do LSE.

### Pipeline de 7 Camadas do Google

| Camada | Funcao | Tecnologia |
|--------|--------|-----------|
| 1. Processamento semantico | Embeddings, entidades, desambiguacao | LSE, BERT, MUM |
| 2. Classificacao de intencao | Informacional, comercial, navegacional | Classificadores |
| 3. Avaliacao de completude | Cobertura do topico | Modelos de cobertura |
| 4. Qualidade editorial | Helpful Content, E-E-A-T | Quality rating |
| 5. Autoridade | Links, reputacao, historico | Sinais linkograficos |
| 6. Sinais comportamentais | CTR, dwell time | Dados de uso |
| 7. Ranking final hibrido | Consolidacao | Modelo hibrido |

### Triade SERP

**Layer 1 -- Document Ranking:** BERT decompoe query em agrupamentos semanticos. MUM processa sinais multimodais. Resultado: Top-K documentos.

**Layer 2 -- Passage Ranking:** Extracao de trechos via sliding window. BERT re-ranking por similaridade. Resultado: Top-M passagens.

**Layer 3 -- Passage Generation:** SGE seleciona entre LLMs (Patent US11769017B1). RAG garante grounding factual. Resultado: resumo gerado + links + perguntas.

Se voce nao se posicionar no Layer 1, nao ficara entre as respostas do LLM.

---

## 3. GEO (Generative Engine Optimization)

### Citabilidade por LLMs

- Resumo inicial apos H1 (2-3 frases, a summarization)
- Definicoes curtas e citaveis
- Frases com condicoes explicitas ("se X, entao Y")
- Numeros com contexto
- Listas/tabelas estruturadas
- Entity Loop Closure

**Para RAG:** nao usar pronomes vagos em paragrafos-chave. Repetir entidade nomeada para que, se o paragrafo for extraido isoladamente (chunking), mantenha sentido.

### Compressibilidade

Conteudo condensavel sem perder nuances. Minimo de implicitos. Terminologia consistente. Estrutura modular com blocos reutilizaveis.

### Evidencia e Rastreabilidade

Referencias/fontes citadas. Metodologia explicita. Data de atualizacao. Escopo delimitado.

---

## 4. MTT (Meaning-Text Theory) e Lexical Functions

### Principio

Patent US2016/0147878A1: a linguagem e definida pela forma como seus elementos se combinam. Foco no lexico. Analise semantica baseada em lexico detecta frases com o mesmo significado, mesmo que formalmente diferentes.

### Lexical Functions

| LF | Nome | SAF | Exemplo |
|----|------|-----|---------|
| -- | Match exato | 1.00 | viagem = viagem |
| Syn0 | Sinonimo direto | 0.99 | viagem -> jornada |
| Syn1 | Sinonimo proximo | 0.75 | viagem -> excursao |
| Syn2 | Sinonimo distante | 0.50 | viagem -> travessia |
| Oper | Verbo operacional | -- | viagem -> fazer/realizar |
| Vo | Verbalizacao | -- | viagem -> viajar |
| Ao | Adjetivacao | 0.60 | viagem -> viajante |

**Aplicacao pratica:** usar vocabulario variado com Lexical Functions naturais fortalece o embedding. "Fazer uma viagem" (Oper), "viajar" (Vo), "viajante" (Ao) reforçam o mesmo conceito sem repeticao.

### FSW (Frequency-balanced Semantic Weight)

```
FSW = SWC / (1 + log2(FREQ))
```

Termos raros no corpus tem maior peso informacional (principio Shannon). Vocabulario especifico do dominio (FREQ baixo) aumenta FSW.

### COINC Score

```
POS_SIM = soma(FSW x SAF) para todos os matches
NEG_SIM = soma(FSW) para termos nao correspondidos x penalty
COINC = POS_SIM - NEG_SIM (conteudo estruturado)
```

Conteudo tangencial aumenta NEG_SIM e reduz COINC.

---

## 5. KORAY'S FRAMEWORKS

### 5.1 Topical Authority

Autoridade vem de cobertura semantica completa, consistente e conectada. Nao de backlinks isolados.

**Topical Map:** entidade central -> subentidades -> atributos -> processos -> problemas -> comparacoes -> limites.

**Coverage:** Breadth (quantos aspectos) + Depth (quao profundo). Sites fracos: muitos artigos rasos. Sites fortes: poucos artigos extremamente conectados e profundos.

**Semantic Distance Control:** cada pagina deve estar semanticamente proxima da entidade central. Quanto mais distante, maior o risco de diluir autoridade.

### 5.2 Semantic Content Network

Google avalia redes semanticas de documentos, nao paginas isoladas. Um site e um grafo de significados.

- **Nodes:** cada pagina = no semantico
- **Edges:** links internos = relacoes semanticas
- **Directionality:** paginas fundamentais recebem links. Paginas especificas apontam para pilares.

### 5.3 Information Gain

O buscador favorece documentos que adicionam nova informacao ao indice.

| Dimensao | Descricao |
|----------|-----------|
| Novidade factual | Angulos nao obvios, dados proprios |
| Profundidade analitica | Framework original, relacoes causais |
| Aplicabilidade pratica | Exemplos unicos, passo a passo real |
| Diferenciacao vs SERP | O que este conteudo tem que os outros nao tem |

### 5.4 Contextual Relevance

Nao importa quantas vezes um termo aparece, mas onde, em que contexto e em relacao a quais entidades. Definicoes precedem usos. Exemplos reforcam conceitos. Comparacoes delimitam significado.

### 5.5 Entity-Oriented Content

Google pensa em entidades e fatos. Bom conteudo: introduz entidades -> define atributos -> explica relacoes -> conecta com entidades conhecidas.

---

## 6. RELACOES TAXONOMICAS (WordNet)

Patent US2023/0214412A1: palavras organizadas em synsets (grupos de sinonimos com ID unico).

| Relacao | Descricao | Exemplo | Uso SEO |
|---------|-----------|---------|---------|
| Synonymy | Mesmo significado | vermelho = escarlate | Variacao de vocabulario |
| Antonymy | Oposto | quente x frio | Contraste/comparacao |
| Hypernymy | Categoria superior | cachorro -> animal | Contextualizacao |
| Hyponymy | Subtipo | animal -> cachorro | Especificidade |
| Holonymy | Todo que contem | corpo -> braco | Estrutura de componentes |
| Meronymy | Parte de um todo | braco -> corpo | Detalhamento tecnico |
| Entailment | Implicacao logica | roncar -> dormir | Relacoes causais |
| Domain | Dominio de uso | bisturi -> medicina | Contexto profissional |

---

## 7. INFORMATION THEORY (Shannon)

```
I(x) = -log2(P(x))
```

Quanto menor a probabilidade de um termo, maior sua informacao. Conteudos genericos: baixo ganho informacional. Conteudos com angulos proprios, dados unicos, frameworks originais: alto ganho.

---

## 8. PATENTES DE REFERENCIA

| Patent | Area | Aplicacao |
|--------|------|-----------|
| US2016/0147878A1 (Inbenta) | MTT, Lexical Functions, COINC | Matching semantico, variacao lexical |
| US2023/0214412A1 (Exeter) | WordNet, Synsets | Indexacao por conceito |
| US20140032522A1 (Kikin) | Context Vectors, Rich Query | Desambiguacao, contexto |
| US2006/0242140A1 (Content Analyst) | Latent Semantic Clustering | Clusters semanticos |
| US11769017B1 (Google SGE) | Generative Summaries | Selecao de LLM para SERP |

---

## 9. MODELO EAV (Entity-Attribute-Value)

O Google organiza conhecimento como:

```
Entidade: Maquina de Costura Singer
  Atributo: Tipo -> Valor: domestica, industrial
  Atributo: Pontos -> Valor: reto, zigzag, overlock
  Atributo: Velocidade -> Valor: 750 ppm
  Atributo: Preco -> Valor: R$ 800 a R$ 3.500
```

Isso permite indexacao por conceito, nao por palavra. Preencher atributos com valores especificos aumenta precisao do embedding.
