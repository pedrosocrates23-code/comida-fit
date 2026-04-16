# STYLE GUIDE -- Regras de Escrita, HTML e Entrega

## 1. REGRAS DE ESCRITA

### 1.1 Paragrafos

- 2-3 frases por paragrafo — escrita mobile-first (nunca mais que 3 frases)
- Referencia: 1-2 linhas desktop = 3-4 linhas mobile (limite aceitavel)
- 3-4 linhas desktop = 8-10 linhas mobile (PROIBIDO)
- Cada paragrafo transmite UMA ideia
- Primeira frase do paragrafo carrega a informacao principal
- Voz ativa predominante ("O tecido absorve" e nao "O tecido e absorvido")

### 1.2 Frases

- Diretas e curtas (15-25 palavras ideal, maximo 35)
- Sujeito + verbo + complemento
- Evitar subordinacoes excessivas (no maximo 1 oraçao subordinada por frase)
- Cada frase adiciona informacao nova (nao repetir o que ja foi dito)

### 1.3 Vocabulario

- Linguagem simples e acessivel
- Termos tecnicos: definir na primeira ocorrencia
- Usar vocabulario especifico do nicho (alto FSW, principio Shannon)
- Variar com Lexical Functions naturais (Syn0, Syn1, Vo, Ao)
- Nunca repetir a mesma expressao em paragrafos consecutivos

### 1.4 Proibicoes Absolutas

| Proibido | Motivo | Alternativa |
|----------|--------|-------------|
| Travessoes (—) | Corta fluxo de leitura | Virgula, dois-pontos ou ponto final |
| Emojis | Fora do padrao editorial | Nenhum |
| Keyword stuffing | Penalizacao Google | 0.5-2% densidade com variacoes |
| Titulos em CAIXA ALTA | Fora do padrao editorial | Sentence case |
| Frases inteiras em bold | Poluicao visual | Bold apenas em entidades/dados |

**Lista completa de conectores proibidos (D01 — 15 itens canônicos):**

Nenhum dos termos abaixo pode aparecer em nenhuma posicao do texto — nem no inicio de frases, nem em transicoes:

```
Além disso | Portanto | Dessa forma | Assim sendo | Em suma
Logo | Por fim | Ou seja | Nesse sentido | Vale ressaltar
É importante destacar | Saiba mais | Confira | Incrível | Revolucionário
```

Substituicao: reescrever iniciando com **sujeito + verbo**. Nao sinalizar a sequencia logica — deixar o conteudo falar por si.

### 1.5 Bold (strong)

Usar bold APENAS em:
- Entidades principais (nomes proprios, termos tecnicos do topico)
- Numeros e dados quantificados (precos, porcentagens, medidas)
- Termos-chave para SEO (palavra-foco e LSI primarios)
- Nomes de produtos, marcas, instituicoes
- Conclusoes-chave dentro de paragrafos

NAO usar bold em:
- Frases inteiras
- Conectivos
- Palavras genericas
- Mais de 3 trechos por paragrafo

### 1.6 Desambiguacao

Na primeira mencao de qualquer entidade que pode ser ambigua, contextualizar:

RUIM: "A Singer lancou novo modelo."
BOM: "A **Singer**, fabricante de maquinas de costura com sede nos EUA, lancou o modelo **Heavy Duty 4423** com motor de **1.100 pontos por minuto**."

---

## 2. FORMATO HTML

### 2.1 Tags Permitidas

```
h1, h2, h3, p, ul, ol, li, strong, table, thead, tbody, tr, th, td, a
```

Classe permitida: apenas `class="summarization"`

### 2.2 Tags Proibidas

```
section, div, article, aside, h1, h4, h5, h6, span, br, hr, img
Comentarios HTML (<!-- -->)
Estilos inline (style="")
IDs nao semanticos
```

### 2.3 Estrutura de Cada Elemento

**Summarization (resumo GEO):**
```html
<p class="summarization">[50-60 palavras resumindo TODO o artigo]</p>
```
Nota: sem <strong> no bloco inteiro — bold somente em entidades/dados dentro do texto.

**Paragrafo padrao:**
```html
<p>[2-3 frases com informacao concreta — mobile-first]</p>
```

**Paragrafo com bold:**
```html
<p>A <strong>maquina overlock</strong> realiza acabamentos com <strong>3 ou 4 fios</strong>, produzindo costuras elasticas ideais para <strong>tecidos de malha</strong>.</p>
```

**Lista nao ordenada (3+ itens sem hierarquia):**
```html
<ul>
  <li><strong>Item 1:</strong> descricao com dados</li>
  <li><strong>Item 2:</strong> descricao com dados</li>
  <li><strong>Item 3:</strong> descricao com dados</li>
</ul>
```

**Lista ordenada (sequencia/passos):**
```html
<ol>
  <li><strong>Preparar o tecido:</strong> cortar na medida com margem de 1,5 cm para costura</li>
  <li><strong>Ajustar a maquina:</strong> selecionar ponto reto com comprimento 2,5 mm</li>
  <li><strong>Costurar:</strong> alinhar bordas e costurar a 1 cm da margem</li>
</ol>
```

**Tabela:**
```html
<table>
  <thead>
    <tr>
      <th>Criterio</th>
      <th>Opcao A</th>
      <th>Opcao B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Preco</td>
      <td><strong>R$ 800</strong></td>
      <td><strong>R$ 1.200</strong></td>
    </tr>
    <tr>
      <td>Velocidade</td>
      <td>750 ppm</td>
      <td>1.100 ppm</td>
    </tr>
  </tbody>
</table>
```

**Link interno (silo pages):**
```html
<p>Para entender cada tecnica em detalhes, consulte o <strong><a href="[URL]">guia completo sobre [subtopico]</a></strong>.</p>
```

**Link com placeholder (quando URL nao fornecida):**
```html
<p>O <strong><a href="[URL: guia-tecido-malha]">guia sobre costura em tecido de malha</a></strong> detalha cada etapa do processo.</p>
```

### 2.4 Espacamento

- Quebra de linha entre TODAS as tags
- 1 linha vazia entre elementos diferentes (p, table, ul)
- HTML nunca em linha unica

---

## 3. LEADS GEO

### 3.1 Formula

```
[SUJEITO ESPECIFICO] + [VERBO DE ACAO] + [QUANTIFICACAO] + [CONTEXTO] + [RELEVANCIA]
```

### 3.2 Comprimentos

| Elemento | Palavras |
|----------|---------|
| Summarization | 50-60 |
| Lead H1 | 30-50 |
| Lead H2 | 30-40 |
| Lead H3 | 25-35 |

### 3.3 Exemplos por Categoria

**Educacional:**
RUIM: "Existem diversos tipos de costura que voce pode aprender."
BOM: "A **costura reta** e a **costura zigzag** representam **90% dos pontos** usados em projetos domesticos, exigindo apenas uma maquina basica com agulha 80/12 e linha de poliester."

**Tutorial:**
RUIM: "Vamos aprender a fazer uma bainha."
BOM: "A **bainha invisivel** em tecido de algodao exige **5 etapas** e pode ser concluida em **15 minutos** usando agulha para bainha e linha na cor do tecido."

**Afiliado:**
RUIM: "Este produto e muito bom e vale a pena."
BOM: "A **maquina de costura Singer Brilliance 6180** oferece **80 tipos de ponto**, motor de **750 ppm** e mesa extensora, custando em media **R$ 1.899** no mercado brasileiro."

**Silo Page:**
RUIM: "Nesta pagina voce encontra tudo sobre costura."
BOM: "O **guia de costura para iniciantes** reune **12 tutoriais** organizados por nivel de dificuldade, cobrindo desde a **escolha da maquina** ate **acabamentos profissionais** em 6 tipos de tecido."

### 3.4 Regra de Ouro

Se voce extrair APENAS o lead de uma secao, ele deve fazer sentido sozinho e responder a pergunta principal. Isso e fundamental para GEO (chunking por LLMs).

---

## 4. FORMATO DE ENTREGA

### 4.1 Estrutura de Cada Resposta

```
[HTML completo com quebras de linha]


=============================================

**[Pergunta ao usuario em negrito]**

---
STATUS: [progresso] | PROXIMO: [nome do outline] | Lembrete: [1 regra critica]
```

### 4.2 Componentes do Rodape

- **STATUS:** onde estamos (H1 concluido, 3/10 outlines, etc.)
- **PROXIMO:** nome exato do proximo outline a entregar
- **Lembrete:** UMA regra critica para o proximo passo

### 4.3 Templates de Rodape

**Apos Diagnostico:**
```
STATUS: Diagnostico concluido | PROXIMO: H1 (summarization + introducao) | Lembrete: summarization = resumo de TODO artigo (50-60 palavras)
```

**Apos H1:**
```
STATUS: H1 concluido | PROXIMO: H2 "[titulo]" | Lembrete: h2, lead 30-40 palavras com dados
```

**Apos H2 indo para H3:**
```
STATUS: X/Y outlines | PROXIMO: H3 "[titulo]" | Lembrete: h3, lead 25-35 palavras
```

**Apos H3 indo para H2:**
```
STATUS: X/Y outlines | PROXIMO: H2 "[titulo]" | Lembrete: h2, pode usar tabela
```

**Antes FAQ:**
```
STATUS: X/Y outlines | PROXIMO: FAQ (N perguntas) | Lembrete: h2 secao, h3 perguntas, 1 p por resposta
```

**Final:**
```
REESCRITA CONCLUIDA. H1 + X outlines + FAQ entregues. Metodologia SEO Genome + E.E.A.T.S. aplicada.
```

### 4.4 Regras de Fluxo

1. NUNCA pular o H1 (sempre primeiro apos diagnostico)
2. Aguardar "ok" entre entregas
3. Uma secao por entrega (nunca duas juntas)
4. Se o usuario pedir alteracao, refazer e reenviar
5. Manter numeracao de progresso consistente

---

## 5. COMPRIMENTOS DE REFERENCIA

| Elemento | Min | Ideal | Max |
|----------|-----|-------|-----|
| Summarization | 50 | 55 | 60 palavras |
| H1 total | 100 | 150 | 200 palavras |
| Lead H2 | 30 | 35 | 40 palavras |
| H2 total | 300 | 350 | 400 palavras (parágrafo intro do H2 apenas — não inclui os H3 filhos) |
| Lead H3 | 25 | 30 | 35 palavras |
| H3 total | 100 | 125 | 150 palavras (não inclui o parágrafo intro do H2 pai — parágrafos: máx 3 linhas) |
| Paragrafo | 40 | 60 | 80 palavras |
| Resposta FAQ | 45 | 52 | 60 palavras |

---

## 6. DENSIDADE DE PALAVRA-FOCO

| Elemento | Mencoes |
|----------|---------|
| Summarization | 1x obrigatorio |
| H1 | 1-2x |
| H2/H3 | 0-2x (natural) |
| Total artigo | 0.5-2% |

**Regras:**
- Nunca repetir em frases consecutivas
- Preferir variacoes (sinonimos, hiponimos)
- LSI keywords > repeticao da palavra-foco
- Acima de 2% = keyword stuffing

---

## 7. DISTRIBUICAO DE LSI KEYWORDS

| Tipo LSI | 3-4 secoes | 5-7 secoes | 8+ secoes |
|----------|-----------|-----------|-----------|
| Primarios | Todas | Todas | Todas |
| Secundarios | 2-3 | 3-5 | 4-6 |
| Contextuais | 1-2 | 2-3 | 3-4 |

---

## 8. CHECKLIST PRE-ENVIO

Aplicar mentalmente ANTES de cada entrega:

### Estrutura
- [ ] Se primeira entrega: e H1?
- [ ] Heading correto (h2 ou h3)?
- [ ] Lead presente e autossuficiente?
- [ ] Comprimento dentro da faixa?
- [ ] HTML limpo sem wrappers/comentarios?
- [ ] Separador + pergunta + rodape?

### Semantica
- [ ] Entidade nomeada (sem pronomes vagos)?
- [ ] Atributos da entidade presentes?
- [ ] Relacoes taxonomicas explicitas?
- [ ] Intencao da secao atendida?
- [ ] Distancia semantica proxima?

### GEO
- [ ] Lead responde sozinho?
- [ ] Dados quantificados presentes?
- [ ] Bloco extraivel como chunk independente?
- [ ] Bold em termos relevantes?

### Estilo
- [ ] Zero travessoes?
- [ ] Zero emojis?
- [ ] Paragrafos 2-3 frases (mobile-first)?
- [ ] Voz ativa?
- [ ] SEM muletas retoricas?
- [ ] Numeros/datas preservados exatos?

### LSI
- [ ] Primarios presentes na secao?
- [ ] Secundarios conforme plano?
- [ ] Palavra-foco sem excesso?
- [ ] Variacoes lexicais aplicadas?

### Factualidade
- [ ] Numeros exatos do original?
- [ ] Datas preservadas?
- [ ] Nomes sem alteracao?
- [ ] Zero dados inventados?

---

## 9. TABELAS: QUANDO USAR

**Usar tabela quando:**
- 3+ itens com 2+ atributos cada
- Dados numericos a comparar
- Especificacoes tecnicas
- Requisitos por categoria

**Usar lista quando:**
- Enumeracao simples (1 atributo)
- Caracteristicas sem comparacao
- Menos de 3 itens
- Sequencia de passos

**Nao usar nenhum quando:**
- O texto flui naturalmente em paragrafos
- Forcar tabela/lista seria artificial
- Menos de 3 itens comparaveis

---

## 10. CITACOES E FONTES

### Citacao Curta (inline)
```html
<p>Segundo <strong>[Nome]</strong>, [cargo], "[texto exato]". [Analise do redator].</p>
```

### Citacao Longa (bloco)
```html
<p><strong>[Nome]</strong>, [cargo], explica:</p>

<p><strong>"[Texto da citacao entre aspas e em bold.]"</strong></p>

<p>[Analise do redator sobre a citacao.]</p>
```

### Citacao de Estudo
```html
<p>De acordo com [estudo] da <strong>[instituicao]</strong> ([ano]), [parafraseado]. O levantamento identificou que [insight].</p>
```

### Regras
1. Toda citacao tem contexto antes e analise depois
2. Fonte identificada: nome + cargo + instituicao
3. Citacao exata entre aspas e em bold
4. Parafrase sem aspas mas com fonte
5. Maximo 1 citacao por secao H2
6. Analise do redator obrigatoria apos citacao
