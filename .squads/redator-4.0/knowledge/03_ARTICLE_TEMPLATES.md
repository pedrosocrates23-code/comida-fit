# ARTICLE TEMPLATES -- Templates por Tipo de Artigo

Cada tipo de artigo tem estrutura, tom, elementos obrigatorios e estrategia de linking propria. Identificar o tipo ANTES de comecar a reescrita e seguir o template correspondente.

---

## COMO USAR ESTE ARQUIVO

1. Identificar o tipo de artigo (pelo conteudo ou pelo comando do usuario)
2. Consultar o template correspondente
3. Aplicar a estrutura, elementos obrigatorios e estrategia de linking
4. Combinar com as regras do STYLE_GUIDE.md para formato HTML

---

## TIPO 1: EDUCACIONAL / BLOG

**Comando:** /educacional
**Objetivo:** Ensinar conceito, processo ou habilidade ao leitor
**Funil:** Topo (awareness, descoberta)
**Tom:** Didatico, acessivel, sem jargao desnecessario

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: o que vai aprender + principal beneficio + para quem

H1 - INTRODUCAO (100-200 palavras)
  P1: Lead com definicao + contexto + dados
  P2: Por que isso importa (problema que resolve)
  P3: O que o leitor vai encontrar neste artigo

H2 - O que e [entidade] (300-350 palavras)
  Definicao formal + definicao pratica
  Contexto de uso
  Diferenca do que NAO e (desambiguacao)

H2 - Como funciona [entidade] (300-350 palavras)
  Mecanismo explicado passo a passo
  Exemplos praticos

H2 - Tipos / Variacoes de [entidade] (300-350 palavras)
  Classificacao com tabela comparativa
  Quando usar cada tipo

H2 - Como fazer / aplicar [entidade] (300-350 palavras)
  Passo a passo numerado
  Materiais/ferramentas necessarias
  Erros comuns a evitar

H2 - [Aspecto complementar relevante] (300-350 palavras)
  Aprofunda um angulo especifico

H2 - FAQ (4-6 perguntas)
  Intencoes latentes nao cobertas nas secoes
```

### Elementos Obrigatorios
- Definicao no primeiro H2
- Pelo menos 1 tabela comparativa
- Pelo menos 1 lista de passo a passo
- Exemplos praticos em cada secao
- Bold em termos-chave e dados

### Estrategia de Linking
- Link para artigos de definicao base (o que e X)
- Link para tutoriais relacionados (como fazer Y)
- Link para comparativos (X vs Z)
- Nao linkar para conteudo comercial no corpo (preservar intencao informacional)

### Exemplo de Lead Educacional
RUIM: "Existem muitas formas de costurar tecidos diferentes."
BOM: "A **costura com tecido de algodao** exige agulha 80/12 e linha de poliester, produzindo acabamentos que resistem **15 a 20 lavagens** sem deformar. Esse tipo de costura atende **78% dos projetos de iniciantes**, segundo dados de escolas de corte e costura."

---

## TIPO 2: TUTORIAL / GUIA PRATICO

**Comando:** /tutorial
**Objetivo:** Guiar o leitor na execucao de uma tarefa
**Funil:** Meio (consideracao, aplicacao)
**Tom:** Instrucional, direto, orientado a acao

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: o que vai fazer + quantas etapas + tempo estimado + resultado

H1 - INTRODUCAO (100-200 palavras)
  P1: Lead com resultado + tempo + nivel de dificuldade
  P2: O que precisa ter/saber antes
  P3: O que vai conseguir ao final

[TABELA-RESUMO se 4+ dados estruturaveis]
  Tempo | Dificuldade | Materiais | Custo | Resultado

H2 - Materiais e ferramentas necessarias (300-350 palavras)
  Lista completa com especificacoes
  Alternativas quando possivel
  Onde encontrar

H2 - Passo 1: [Acao especifica] (300-350 palavras)
  Instrucao clara e unica
  Foto/diagrama descrito
  Erro comum neste passo + como evitar

H2 - Passo 2: [Acao especifica] (300-350 palavras)
  [mesmo padrao]

H2 - Passo N: [Acao especifica] (300-350 palavras)
  [mesmo padrao]

H2 - Erros comuns e como evitar (300-350 palavras)
  Lista dos 3-5 erros mais frequentes
  Solucao para cada um

H2 - FAQ (4-6 perguntas)
  Duvidas praticas de execucao
```

### Elementos Obrigatorios
- Tabela-resumo no inicio (tempo, dificuldade, materiais, custo)
- Cada passo como H2 ou H3 separado
- Bold no verbo de acao de cada passo
- Lista de erros comuns obrigatoria
- Resultado esperado descrito no H1

### Estrategia de Linking
- Link para definicao dos termos tecnicos usados
- Link para tutoriais pre-requisito ("antes de fazer X, aprenda Y")
- Link para tutoriais de nivel superior ("proximo passo: Z")
- Links de materiais para paginas de produto (se aplicavel)

---

## TIPO 3: AFILIADO / REVIEW

**Comando:** /afiliado
**Objetivo:** Analisar produto/servico e direcionar para conversao
**Funil:** Fundo (decisao, compra)
**Tom:** Analitico, transparente, baseado em evidencia

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: produto + nota geral + principal vantagem + para quem e indicado

H1 - INTRODUCAO (100-200 palavras)
  P1: Lead com nome do produto + nota + principal diferencial
  P2: Para quem e indicado vs para quem NAO e
  P3: O que foi testado/avaliado

[TABELA-RESUMO]
  Produto | Preco | Nota | Destaque | Indicacao

H2 - Especificacoes tecnicas de [produto] (300-350 palavras)
  Tabela completa de specs
  Contexto de cada especificacao (o que significa na pratica)

H2 - Pontos positivos de [produto] (300-350 palavras)
  Lista com evidencia factual para cada ponto
  Comparacao implicita com concorrentes (sem nomear, ou nomeando se /comparativo)

H2 - Pontos negativos e limitacoes (300-350 palavras)
  Transparencia total
  Para quem isso NAO e problema
  Alternativas quando a limitacao e grave

H2 - [Produto] vale a pena? Para quem e indicado (300-350 palavras)
  Perfil ideal de comprador
  Cenarios de uso otimo
  Cenarios onde outra opcao e melhor
  CTA natural (nao agressivo)

H2 - FAQ (4-6 perguntas)
  Duvidas de compra: garantia, entrega, suporte, custo-beneficio
```

### Elementos Obrigatorios
- Tabela de especificacoes
- Pontos positivos E negativos (credibilidade)
- Secao "Para quem e indicado"
- CTA integrado naturalmente (nunca secao separada so de CTA)
- Bold em precos, notas, diferenciais

### Estrategia de Linking
- Link para comparativos relacionados (X vs Y)
- Link para tutoriais de uso do produto
- Link para pagina de categoria (hub de produtos)
- Links de afiliado nos CTAs e nome do produto (conforme regras do programa)

### Tom Especifico
- Transparente: "O ponto fraco e [X], que impacta quem [cenario]"
- Sem exagero: nao usar "melhor do mundo", "incrivel", "revolucionario"
- Baseado em uso: "Ao testar durante 30 dias, o resultado foi [dados]"

---

## TIPO 4: COMPARATIVO

**Comando:** /comparativo
**Objetivo:** Comparar duas ou mais opcoes para ajudar na decisao
**Funil:** Meio/Fundo (avaliacao, decisao)
**Tom:** Objetivo, equilibrado, sem favoritismo obvio

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: o que esta sendo comparado + principal diferenca + veredicto resumido

H1 - INTRODUCAO (100-200 palavras)
  P1: Lead com as opcoes + criterio principal de comparacao
  P2: Para quem cada opcao funciona melhor
  P3: Criterios usados na comparacao

[TABELA COMPARATIVA GERAL]
  Criterio | Opcao A | Opcao B | Vencedor

H2 - [Criterio 1]: [Opcao A] vs [Opcao B] (300-350 palavras)
  Dados de cada um
  Diferenca pratica
  Veredicto do criterio

H2 - [Criterio 2]: [Opcao A] vs [Opcao B] (300-350 palavras)
  [mesmo padrao]

H2 - [Criterio N]: [Opcao A] vs [Opcao B] (300-350 palavras)
  [mesmo padrao]

H2 - Veredicto: qual escolher (300-350 palavras)
  Cenario 1: escolha A se [condicao]
  Cenario 2: escolha B se [condicao]
  Cenario 3: alternativa C se [condicao]

H2 - FAQ (4-6 perguntas)
  "Qual e melhor para [cenario especifico]?"
```

### Elementos Obrigatorios
- Tabela comparativa geral logo apos H1
- Cada criterio como secao separada
- Veredicto por criterio + veredicto geral
- Bold nos numeros e diferenciais
- Cenarios de uso no veredicto (nao apenas "A e melhor")

### Estrategia de Linking
- Link para review individual de cada opcao
- Link para guia "como escolher [categoria]"
- Link para pagina de categoria

---

## TIPO 5: SILO PAGE (HUB)

**Comando:** /silo
**Objetivo:** Ser a pagina central que distribui autoridade para child pages
**Funil:** Topo/Meio (visao geral + navegacao)
**Tom:** Abrangente, organizacional, autoritativo

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: o que e o topico + quantos subtopicos cobertos + para quem

H1 - INTRODUCAO (150-200 palavras)
  P1: Lead com definicao ampla da entidade central
  P2: Escopo do que sera coberto
  P3: Como navegar este guia (direciona para secoes)

H2 - O que e [entidade central] (300-350 palavras)
  Definicao completa
  Contexto historico/evolutivo breve
  Por que e relevante
  [LINK INTERNO para artigo de definicao detalhada se existir]

H2 - [Subtopico 1] (300-350 palavras)
  Visao geral do subtopico
  Principais aspectos cobertos
  [LINK INTERNO: "Leia o guia completo sobre [subtopico 1]"]

H2 - [Subtopico 2] (300-350 palavras)
  [mesmo padrao]
  [LINK INTERNO para child page]

H2 - [Subtopico N] (300-350 palavras)
  [mesmo padrao]
  [LINK INTERNO para child page]

H2 - Como escolher / por onde comecar (300-350 palavras)
  Fluxo de decisao
  Link para cada caminho

H2 - FAQ (6-8 perguntas)
  Perguntas amplas do topico
  Cada resposta pode direcionar para child page
```

### Elementos Obrigatorios
- Definicao ampla da entidade central no H1
- Cada H2 cobre um subtopico com LINK INTERNO para pagina filha
- Tabela de navegacao (opcional mas recomendada):

```html
<table>
  <thead>
    <tr>
      <th>Topico</th>
      <th>O que voce vai aprender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>[Subtopico 1]</strong></td>
      <td>[descricao curta]</td>
    </tr>
  </tbody>
</table>
```

- Visao geral de cada subtopico (NAO aprofundar, isso e funcao da child page)
- Bold nos nomes dos subtopicos e links

### Estrategia de Linking (CRITICA para silo)

**Regras de linking da silo page:**
1. Cada H2 DEVE ter pelo menos 1 link para child page do subtopico
2. Links usam anchor text descritivo (nao "clique aqui")
3. Formato de link no HTML:

```html
<p>Para entender cada tecnica em detalhes, consulte o <strong><a href="[URL]">guia completo sobre [subtopico]</a></strong>.</p>
```

4. Se o usuario forneceu URLs em <urls-internas>, usar as URLs reais
5. Se nao forneceu, usar placeholder: [URL: guia-sobre-subtopico]
6. Links de child pages NUNCA apontam para fora do silo (apenas dentro)
7. FAQ pode ter links para child pages especificas

### Tom Especifico
- Amplo: cobrir visao geral sem mergulhar em detalhes
- Organizacional: o leitor deve entender a estrutura do topico
- Direcional: cada secao direciona para conteudo mais profundo

---

## TIPO 6: ARTIGO COM CITACAO

**Comando:** /citacao
**Objetivo:** Apresentar conteudo enriquecido com citacoes de especialistas, fontes ou estudos
**Funil:** Qualquer (depende do contexto)
**Tom:** Autoritativo, referenciado, academico-acessivel

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: tema + principal insight + fonte/especialista citado

H1 - INTRODUCAO (100-200 palavras)
  P1: Lead com dado ou afirmacao de impacto
  P2: Contexto da discussao
  P3: Quem foi ouvido / que fontes embasam

H2 - [Aspecto 1 do tema] (300-350 palavras)
  Desenvolvimento com dados
  CITACAO integrada no fluxo
  Analise/contexto apos a citacao

H2 - [Aspecto 2 do tema] (300-350 palavras)
  [mesmo padrao com citacao quando aplicavel]

H2 - [Aspecto N] (300-350 palavras)

H2 - FAQ (4-6 perguntas)
```

### Formato de Citacao no HTML

**Citacao curta (ate 3 linhas) -- inline:**
```html
<p>Segundo <strong>[Nome do Especialista]</strong>, [cargo/instituicao], "[texto da citacao exata]". Essa analise reforça que [contextualizacao propria do redator].</p>
```

**Citacao longa (4+ linhas) -- bloco:**
```html
<p><strong>[Nome do Especialista]</strong>, [cargo/instituicao], explica o cenario:</p>

<p><strong>"[Texto da citacao. Pode ter 2-3 frases. Sempre entre aspas e em bold.]"</strong></p>

<p>[Analise/contexto do redator sobre a citacao. Nunca deixar citacao solta.]</p>
```

**Citacao de estudo/fonte:**
```html
<p>De acordo com [estudo/relatorio] publicado pela <strong>[instituicao]</strong> em [ano], [dado ou conclusao parafraseada]. O levantamento analisou [escopo] e identificou que [insight principal].</p>
```

### Regras de Citacao
1. Toda citacao DEVE ter contexto antes e analise depois (nunca solta)
2. Identificar fonte: nome + cargo + instituicao
3. Citacao exata entre aspas e em bold
4. Parafrase nao leva aspas mas identifica a fonte
5. Maximo 1 citacao por H2 (nao sobrecarregar)
6. A analise do redator SEMPRE segue a citacao (valor editorial)
7. Se o texto original tem citacao sem fonte, sinalizar no diagnostico

### Elementos Obrigatorios
- Pelo menos 2 citacoes no artigo (se o tipo e /citacao)
- Fonte identificada em cada citacao
- Analise propria apos cada citacao
- Bold no nome da fonte e no texto citado

---

## TIPO 7: CIENTIFICO / TECNICO

**Comando:** /cientifico
**Objetivo:** Apresentar informacao tecnica com rigor metodologico
**Funil:** Meio (aprofundamento, validacao)
**Tom:** Tecnico, preciso, referenciado

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: tema + principal conclusao + metodologia resumida

H1 - INTRODUCAO (150-200 palavras)
  P1: Contexto do problema/questao
  P2: Relevancia do tema (dados)
  P3: Escopo e metodologia resumida

H2 - Contexto e fundamentacao (300-350 palavras)
  Estado atual do conhecimento
  Estudos anteriores relevantes
  Lacuna que o conteudo preenche

H2 - Metodologia / Abordagem (300-350 palavras)
  Como os dados foram obtidos
  Criterios de analise
  Limitacoes declaradas

H2 - Resultados / Analise (300-350 palavras)
  Dados apresentados com contexto
  Tabelas quando aplicavel
  Interpretacao objetiva

H2 - Discussao / Implicacoes (300-350 palavras)
  O que os resultados significam
  Comparacao com literatura existente
  Aplicacoes praticas

H2 - Conclusao (300-350 palavras)
  Sintese dos achados
  Limitacoes reafirmadas
  Direcoes futuras

H2 - FAQ (4-6 perguntas)
  Duvidas tecnicas acessiveis
```

### Elementos Obrigatorios
- Secao de metodologia/abordagem
- Dados com fonte identificada
- Limitacoes declaradas (credibilidade)
- Terminologia tecnica com definicao na primeira ocorrencia
- Bold em termos tecnicos, numeros, nomes de estudos

---

## TIPO 8: LISTICLE

**Comando:** /listicle
**Objetivo:** Lista estruturada (N melhores, N dicas, N erros)
**Funil:** Topo (descoberta) ou Meio (avaliacao)
**Tom:** Escaneavel, objetivo, util

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: o que e a lista + quantos itens + criterio de selecao

H1 - INTRODUCAO (100-150 palavras)
  P1: Lead com quantidade + criterio + para quem
  P2: Como a lista foi organizada
  P3: O que torna esta lista diferente

H2 - 1. [Item] (300-350 palavras)
  Lead com destaque principal do item
  Detalhamento com dados
  Para quem e indicado

H2 - 2. [Item] (300-350 palavras)
  [mesmo padrao]

H2 - N. [Item] (300-350 palavras)
  [mesmo padrao]

H2 - Como escolher entre as opcoes (300-350 palavras)
  Tabela comparativa resumo
  Criterios de decisao

H2 - FAQ (4-6 perguntas)
```

### Elementos Obrigatorios
- Numero no titulo de cada H2 (1. Item, 2. Item...)
- Tabela comparativa ao final
- Bold no nome de cada item e principal diferencial
- Criterio de selecao explicito no H1

---

## TIPO 9: NEWS / ATUALIDADE

**Comando:** /news
**Objetivo:** Informar sobre evento recente com dados e contexto
**Funil:** Topo (awareness)
**Tom:** Factual, objetivo, atualizado

### Estrutura Obrigatoria

```
SUMMARIZATION (50-60 palavras)
  Resume: o que aconteceu + quando + numeros principais + impacto

H1 - INTRODUCAO (100-200 palavras)
  P1: Lead com fato principal + data + numeros
  P2: Contexto imediato
  P3: O que muda para o leitor

H2 - O que aconteceu (300-350 palavras)
  Fatos na ordem cronologica
  Dados especificos

H2 - Contexto e antecedentes (300-350 palavras)
  Historico relevante
  Por que agora

H2 - Impacto e consequencias (300-350 palavras)
  Quem e afetado
  O que muda na pratica
  Projecoes (com fonte)

H2 - Proximos passos / O que esperar (300-350 palavras)
  Timeline de eventos futuros
  O que o leitor deve fazer

H2 - FAQ (4-6 perguntas)
  Duvidas praticas sobre o evento
```

### Elementos Obrigatorios
- Data explicita em todas as secoes relevantes
- Numeros em bold
- Fontes identificadas
- Timeline quando houver sequencia de eventos

---

## TIPO 10: PILAR / CORNERSTONE

**Comando:** /pilar
**Objetivo:** Conteudo longo e abrangente, hub central do topico
**Funil:** Todos (referencia completa)
**Tom:** Enciclopedico, profundo, autoritativo

### Estrutura Obrigatoria

```
SUMMARIZATION (60 palavras)
  Resume: tema completo + escopo + para quem + principal entrega

H1 - INTRODUCAO (200 palavras)
  P1: Lead com definicao completa + contexto
  P2: Escopo do guia (o que cobre)
  P3: Para quem e e como navegar

[TABELA DE CONTEUDOS]
  Secao | O que cobre

H2 - O que e [entidade] (300-350 palavras)
H3 - Definicao tecnica
H3 - Definicao pratica
H3 - Historico/evolucao

H2 - Como funciona [entidade] (300-350 palavras)
H3 - Mecanismo principal
H3 - Variacoes

H2 - Tipos de [entidade] (300-350 palavras)
H3 - Tipo A
H3 - Tipo B
H3 - Tabela comparativa

H2 - Como fazer / aplicar (300-350 palavras)
H3 - Passo a passo
H3 - Ferramentas
H3 - Erros comuns

H2 - [Topico avancado 1] (300-350 palavras)
H2 - [Topico avancado 2] (300-350 palavras)

H2 - FAQ (8-10 perguntas)
```

### Elementos Obrigatorios
- Tabela de conteudos apos H1
- Minimo 6 H2 com H3 subordinados
- Links internos para TODOS os artigos relacionados do site
- Word count total: 2.500-4.000 palavras
- Cobre intencoes explicitas E latentes completamente

### Estrategia de Linking
- Link para CADA child page do topico
- Link para artigos comparativos
- Link para tutoriais
- Link para FAQ dedicada (se existir)
- Este artigo RECEBE links de todas as child pages

---

## TABELA DE DECISAO RAPIDA

| Pergunta | Tipo Indicado |
|----------|---------------|
| Ensina algo conceitual? | Educacional |
| Mostra como fazer passo a passo? | Tutorial |
| Analisa um produto para compra? | Afiliado |
| Compara duas opcoes? | Comparativo |
| E a pagina central de um topico? | Silo Page |
| Tem citacoes de especialistas? | Citacao |
| Exige rigor tecnico/cientifico? | Cientifico |
| E uma lista de N itens? | Listicle |
| Cobre um evento recente? | News |
| E o conteudo mais completo do site? | Pilar |
