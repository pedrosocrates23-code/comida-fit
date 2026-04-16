# SEO Contextualizador Squad

> Squad especializado em gerar briefings contextuais E.E.A.T.S. para artigos SEO,
> preenchendo automaticamente a coluna **"Prompt Adicional"** de planilhas XLSX.

---

## O que faz

1. **Lê** sua planilha XLSX com título + palavra-chave preenchidos
2. **Pesquisa** a internet (dados mais recentes — 2025/2026) para cada keyword
3. **Gera** um briefing E.E.A.T.S. completo (7 camadas semânticas)
4. **Escreve** o briefing nas colunas `Prompt Adicional` (col T) e `Termos LSI` (col U)

---

## Estrutura da Planilha Esperada

| Coluna | Campo | Papel |
|--------|-------|-------|
| B | Palavra-chave Foco | **INPUT** — você preenche |
| C | Título | **INPUT** — você preenche |
| T | Prompt Adicional | **OUTPUT** — squad preenche |
| U | Termos LSI | **OUTPUT** — squad preenche |

---

## Agentes

| Agente | Ícone | Especialidade |
|--------|-------|--------------|
| `@maestro` | 🎯 | Orquestrador — lê planilha, coordena, escreve resultados |
| `@nebula` | 🔭 | Pesquisa web — SERP, entidades, LSI, dados recentes |
| `@atlas` | 🗺️ | Briefing — gera as 7 camadas E.E.A.T.S. completas |

---

## Como usar

### Pré-requisitos

```bash
pip install openpyxl
```

### Setup do contexto da empresa

1. Abra `data/contexto-empresa-ativo.md`
2. Cole o texto `<contexto-empresa>` do seu cliente
3. Salve

### Ativar e processar

```
@maestro
*processar-lote C:/caminho/para/Template.xlsx
```

O squad vai:
1. Verificar o contexto da empresa
2. Ler as linhas com keyword + título preenchidos
3. Pedir sua confirmação das linhas a processar
4. Para cada linha: pesquisar → gerar briefing → armazenar
5. Salvar `Template_contextualizado.xlsx` no mesmo diretório
6. Apresentar relatório de progresso

### Comandos principais

| Comando | Descrição |
|---------|-----------|
| `@maestro *processar-lote {xlsx}` | Pipeline completo |
| `@maestro *ler-planilha {xlsx}` | Ver linhas disponíveis |
| `@maestro *set-empresa` | Definir contexto da empresa |
| `@nebula *pesquisar-topico {keyword}` | Pesquisa manual de uma keyword |
| `@atlas *gerar-briefing {keyword} {titulo}` | Gerar briefing manual |

---

## Framework E.E.A.T.S.

O briefing gerado segue 7 camadas semânticas:

| Camada | Peso | Função |
|--------|------|--------|
| 1. Entity Lock-in | 25% | Fixar entidade principal |
| 2. Essential Entity Set | 15% | Sub-entidades obrigatórias |
| 3. Attribute Coverage | 15% | Atributos internos |
| 4. Relational Semantics | 10% | Posicionamento taxonômico |
| 5. Intent Completeness | 15% | Intenções explícitas + latentes |
| 6. Contextual Embedding | 10% | Exemplos, cases, frases GEO |
| 7. Entity Loop Closure | 10% | Síntese + CTA |

---

## Estrutura de Arquivos

```
seo-contextualizador/
├── agents/
│   ├── maestro.md       # Orquestrador principal
│   ├── nebula.md        # Pesquisa web e SERP
│   └── atlas.md         # Arquiteto E.E.A.T.S.
├── tasks/
│   ├── ler-planilha.md
│   ├── pesquisar-topico.md
│   ├── gerar-briefing-eatss.md
│   ├── escrever-planilha.md
│   └── processar-lote.md
├── workflows/
│   └── wf-contextualizacao.yaml
├── data/
│   ├── eatss-framework.md          # Referência do framework
│   ├── lsi-taxonomy.md             # Guia de clusters LSI
│   └── contexto-empresa-ativo.md   # ← COLE O CONTEXTO DO CLIENTE AQUI
├── templates/
│   └── briefing-eatss-tmpl.md     # Template de output
├── scripts/
│   └── xlsx-manager.py            # Script Python para I/O do xlsx
├── checklists/
│   └── briefing-quality-gate.md   # Quality gate do briefing
└── config.yaml
```

---

## Sobre o Framework E.E.A.T.S.

Desenvolvido para maximizar cobertura semântica e citabilidade GEO/RAG.
Cada camada endereça um aspecto da compreensão algorítmica moderna:
entidade, sub-entidades, atributos, taxonomia, intenção, contexto e closure.

O modelo base está em `data/eatss-framework.md`.

---

*SEO Contextualizador Squad v1.0 — Synkra AIOX*
