# OUTLINE GENERATOR -- Regras para Estruturar Artigos

## 1. PRINCIPIO CENTRAL

Um outline nao e uma lista de titulos. E um mapa semantico que reflete a hierarquia de intencoes do leitor e a estrutura de entidades do topico.

Cada H2 responde a uma intencao distinta. Cada H3 detalha um atributo ou subtipo dentro dessa intencao. A ordem segue a logica do funil informacional: definicao -> mecanismo -> tipos -> aplicacao -> decisao.

---

## 2. PROCESSO DE GERACAO

### Passo 1: Identificar a Entidade Central

Qual e a entidade principal do artigo? Tudo gira em torno dela.

Exemplo: "costura com maquina overlock"
- Entidade central: maquina overlock
- Hiperonimo: maquina de costura
- Hiponimos: overlock domestica, overlock industrial
- Atributos: pontos, velocidade, tipos de tecido, preco

### Passo 2: Mapear Intencoes

Para a entidade central, listar todas as intencoes possiveis:

**Intencoes explicitas (derivadas da SERP):**

| Intencao | Template de Query | Prioridade |
|----------|-------------------|-----------|
| Definicao | O que e [entidade] | Alta |
| Mecanismo | Como funciona [entidade] | Alta |
| Procedimento | Como fazer/usar [entidade] | Alta |
| Tipologia | Tipos de [entidade] | Media |
| Exemplificacao | Exemplos de [entidade] | Media |
| Avaliacao | [Entidade] vale a pena | Media |
| Comparacao | [Entidade] vs [alternativa] | Media |
| Custo | Quanto custa [entidade] | Alta |

**Intencoes latentes (inferidas):**

| Intencao | Pergunta Implicita | Prioridade |
|----------|-------------------|-----------|
| Escolha | Como escolher [entidade] | Alta |
| Erros | Erros comuns com [entidade] | Media |
| Limitacoes | Desvantagens de [entidade] | Media |
| Alternativas | Substitutos para [entidade] | Baixa |
| Pre-requisitos | O que preciso saber antes | Media |
| Manutencao | Como cuidar/manter [entidade] | Baixa |
| Quando nao usar | Quando [entidade] nao e indicada | Media |

### Passo 3: Filtrar por Tipo de Artigo

Nem todas as intencoes cabem em todos os tipos. Filtrar usando a tabela:

| Intencao | Educacional | Tutorial | Afiliado | Comparativo | Silo | Pilar |
|----------|-------------|----------|----------|-------------|------|-------|
| Definicao | SIM | Breve | Breve | Breve | SIM | SIM |
| Mecanismo | SIM | SIM | Breve | Breve | Breve | SIM |
| Procedimento | Opcional | SIM | Opcional | NAO | Breve | SIM |
| Tipologia | SIM | Opcional | SIM | SIM | SIM | SIM |
| Custo | Opcional | Opcional | SIM | SIM | Breve | SIM |
| Comparacao | Opcional | NAO | Opcional | SIM | Breve | SIM |
| Erros | SIM | SIM | Opcional | NAO | NAO | SIM |
| Escolha | Opcional | NAO | SIM | SIM | SIM | SIM |

### Passo 4: Organizar Hierarquia

**Regra: definicoes vem antes de aplicacoes. Conceitos gerais vem antes de especificos.**

Ordem logica padrao:
1. O que e (definicao + contexto)
2. Como funciona (mecanismo)
3. Tipos/variacoes (tipologia)
4. Como fazer/usar (procedimento)
5. Custos/valores (se aplicavel)
6. Erros comuns (prevenção)
7. Comparacoes (se aplicavel)
8. FAQ

### Passo 5: Definir H3 dentro de H2

H3 existe quando um H2 tem 2+ subtipos, etapas ou aspectos distintos.

**Criterio para criar H3:**
- H2 cobre 2+ variantes -> cada variante e H3
- H2 tem 3+ etapas -> cada etapa pode ser H3
- H2 tem aspecto tecnico + aspecto pratico -> dividir em H3

**Criterio para NAO criar H3:**
- H2 cobre um unico aspecto linear
- Subdivisao seria artificial (forcada)
- Total de palavras ficaria abaixo de 250 por H3

---

## 3. FORMULAS POR TIPO DE ARTIGO

### Educacional

```
H2: O que e [entidade]
  H3: Definicao e conceito
  H3: Origem/historico (se relevante)

H2: Como funciona [entidade]
  H3: Principio basico
  H3: Na pratica

H2: Tipos de [entidade]
  H3: Tipo A (caracteristicas + quando usar)
  H3: Tipo B (caracteristicas + quando usar)
  H3: Tabela comparativa

H2: Como aplicar [entidade]
  H3: Passo a passo
  H3: Ferramentas necessarias

H2: Erros comuns com [entidade]

H2: FAQ
```

### Tutorial

```
H2: O que voce vai precisar
  H3: Materiais
  H3: Ferramentas
  H3: Pre-requisitos

H2: Passo 1: [Acao]
H2: Passo 2: [Acao]
H2: Passo 3: [Acao]
H2: Passo N: [Acao]

H2: Dicas para melhores resultados

H2: Erros comuns e solucoes

H2: FAQ
```

### Afiliado

```
H2: Visao geral de [produto]
  H3: Especificacoes
  H3: Diferenciais

H2: Pontos positivos
H2: Pontos negativos
H2: [Produto] vs [alternativa principal]

H2: Para quem e indicado
  H3: Cenario ideal
  H3: Quando escolher outra opcao

H2: Onde comprar e preco atualizado

H2: FAQ
```

### Silo Page

```
H2: O que e [topico central]

H2: [Subtopico 1] -- visao geral + link
  H3: [Aspecto A]
  H3: [Aspecto B]

H2: [Subtopico 2] -- visao geral + link
  H3: [Aspecto A]
  H3: [Aspecto B]

H2: [Subtopico N] -- visao geral + link

H2: Por onde comecar / Como navegar

H2: FAQ
```

### Pilar

```
H2: O que e [entidade]
  H3: Definicao tecnica
  H3: Definicao pratica
  H3: Contexto historico

H2: Como funciona
  H3: Mecanismo A
  H3: Mecanismo B

H2: Tipos
  H3: Tipo 1
  H3: Tipo 2
  H3: Tipo N + tabela

H2: Como fazer
  H3: Etapa 1
  H3: Etapa 2
  H3: Ferramentas

H2: Custos e investimento
H2: Erros comuns
H2: [Topico avancado]
H2: [Topico avancado]

H2: FAQ (8-10 perguntas)
```

---

## 4. REGRAS DE TITULACAO

### H2 (secao principal)

- Deve conter a entidade-alvo da secao
- Responde a uma intencao identificavel
- Nao repetir a palavra-foco de forma identica em todos os H2
- Usar variacoes naturais da palavra-foco

**Bom:** "Como funciona a maquina overlock na pratica"
**Ruim:** "Maquina overlock: funcionamento" (generico, sem intencao)

### H3 (subsecao)

- Especifica um aspecto dentro do H2
- Pode conter entidade secundaria ou atributo
- Mais curto e direto que H2

**Bom:** "Overlock domestica: para quem e indicada"
**Ruim:** "Informacoes sobre a overlock domestica" (vago)

### Proibicoes em titulos

- Nao usar "Introducao", "Conclusao" como H2 (sao funcoes, nao titulos)
- Nao usar "Saiba mais sobre X" (vazio semanticamente)
- Nao comecar com "Entendendo..." ou "Conhecendo..." (passivo)
- Nao usar travessoes ou emojis
- Nao repetir o titulo do artigo como H2

---

## 5. SEMANTIC DISTANCE NOS OUTLINES

Cada H2 deve ser avaliado pela distancia da entidade central:

| Distancia | Significado | Decisao |
|-----------|-------------|---------|
| 0-1 | Diretamente sobre a entidade | Manter como H2 |
| 2 | Atributo ou aspecto direto | Manter como H2 ou H3 |
| 3 | Relacionado mas indireto | Avaliar se agrega ou dilui |
| 4+ | Tangencial | Remover ou mover para outro artigo |

**Exemplo para "costura com maquina overlock":**
- "Tipos de ponto overlock" -> Distancia 1 (manter)
- "Tecidos ideais para overlock" -> Distancia 2 (manter)
- "Historia da industria textil" -> Distancia 4 (remover)
- "Diferenca entre overlock e galoneira" -> Distancia 2 (manter)
- "Como montar um atelier" -> Distancia 4 (remover)

---

## 6. INTEGRACAO COM LINKS INTERNOS

Ao gerar outlines para silo pages ou pilares, mapear links:

```
H2: Tipos de ponto overlock
  -> LINK: /ponto-overlock-3-fios/
  -> LINK: /ponto-overlock-4-fios/
  
H2: Tecidos ideais para overlock
  -> LINK: /costura-tecido-malha/
  -> LINK: /costura-tecido-elastico/
```

Se URLs nao foram fornecidas, usar placeholders:
```
[URL: tipos-ponto-overlock]
[URL: tecidos-para-overlock]
```

---

## 7. VALIDACAO DO OUTLINE

Antes de apresentar o outline ao usuario, verificar:

1. Cada H2 responde a uma intencao distinta? (sem sobreposicao)
2. A ordem segue logica informacional? (definicao antes de aplicacao)
3. Nenhuma secao tem distancia semantica > 3?
4. H3 sao necessarios ou artificiais?
5. O tipo de artigo esta refletido na estrutura?
6. FAQ cobre intencoes nao atendidas nos H2?
7. Ha pelo menos 1 secao com tabela/lista planejada?
8. Word count estimado esta adequado ao tipo?

| Tipo | H2 minimos | H3 tipicos | Word count total |
|------|-----------|------------|-----------------|
| Educacional | 4-6 | 0-6 | 1.500-2.500 |
| Tutorial | 5-8 | 2-4 | 1.800-3.000 |
| Afiliado | 4-6 | 2-4 | 1.500-2.500 |
| Comparativo | 4-6 | 0-2 | 1.500-2.000 |
| Silo | 5-8 | 4-8 | 2.000-3.000 |
| Cientifico | 5-7 | 2-6 | 2.000-3.500 |
| Listicle | 5-10 | 0-4 | 1.800-3.500 |
| News | 4-6 | 0-2 | 1.200-2.000 |
| Pilar | 6-10 | 6-15 | 2.500-4.000 |

---

## 8. FORMATO DE APRESENTACAO DO OUTLINE

Ao entregar o outline (modo /outline ou dentro do diagnostico), usar este formato:

```
OUTLINE: [Titulo do Artigo]
Tipo: [tipo identificado]
Entidade central: [entidade]
Word count estimado: [X palavras]
Secoes: [N H2 + N H3]

---

H1 - [Titulo] (100-200 palavras)
  Summarization + Introducao

H2 - [Titulo] (300-350 palavras)
  Intencao: [qual intencao responde]
  Entidades: [entidades desta secao]
  Elementos: [tabela/lista/citacao/link]

  H3 - [Titulo] (300-350 palavras)
    Foco: [aspecto especifico]
  
  H3 - [Titulo] (300-350 palavras)
    Foco: [aspecto especifico]

H2 - [Titulo] (300-350 palavras)
  Intencao: [qual intencao responde]
  Entidades: [entidades desta secao]
  Elementos: [tabela/lista/citacao/link]

...

H2 - FAQ (4-8 perguntas)
  Q1: [pergunta] -> Intencao: [qual]
  Q2: [pergunta] -> Intencao: [qual]
  ...
```
