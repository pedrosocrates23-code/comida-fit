# Task: QA Conceitual — Língua Portuguesa

**Task ID:** qa-conceitual-pt
**Version:** 1.0.0
**Execution Type:** Agent (autônomo, bloqueante)
**Purpose:** Verificar precisão conceitual, terminológica, factual e de exemplos em artigos sobre Língua Portuguesa antes da entrega ao packager
**Executor:** analista-conceitual-pt
**Elicit:** false
**Gate:** RS-003.5
**Precondition:** Gate RS-003-QA PASS (qa-content aprovado)

---

## Inputs

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|------------|-----------|
| `html_artigo` | string (HTML) | SIM | Artigo completo gerado pelo seo-writer |
| `keyword` | string | SIM | Keyword principal do artigo |
| `tipo_artigo` | string | SIM | Tipo de artigo (educacional, tutorial, etc.) |
| `contexto_cliente` | object | SIM | Contexto estruturado do cliente (do pre-check) |

---

## Preconditions

- [ ] Gate RS-003-QA PASS (qa-content liberou o artigo)
- [ ] html_artigo disponível e completo
- [ ] keyword definida

---

## Execution Steps

### Step 1: Extrair Claims do Artigo

```yaml
action: >
  Ler o artigo completo e extrair uma lista de todas as afirmações técnicas
  sobre Língua Portuguesa presentes no texto. Para cada afirmação, registrar:
    - Trecho exato (citação)
    - Localização (H2/H3/FAQ em que aparece)
    - Tipo de claim (regra gramatical / exemplo / data / definição / exceção)
output: claims_list
```

### Step 2: Carregar Checklist

```yaml
action: "Carregar checklists/qa-conceitual-pt.md"
apply_to: claims_list
categories:
  - C1: Precisão Factual
  - C2: Precisão Terminológica
  - C3: Coerência de Exemplos
  - C4: Completude Crítica
  - C5: Consistência Interna
  - C6: Precisão Semântica
```

### Step 3: Verificar Precisão Factual (C1)

```yaml
action: "Verificar datas, anos, nomes, acordos e vigências citados no artigo"
checks:
  - "Datas de acordos, reformas ortográficas, decretos — verificar precisão"
  - "Nomes de gramáticos, autores, instituições"
  - "Datas de vigência (assinatura vs. entrada em vigor vs. obrigatoriedade)"
  - "Referências a concursos, bancas, provas — verificar se não são inventadas"
severity_if_wrong: 🔴 (crítico)
fonte_referencia: "AO/1990, VOLP, histórico legislativo"
```

### Step 4: Verificar Precisão Terminológica (C2)

```yaml
action: "Verificar uso correto dos termos técnicos gramaticais"
checks:
  - "Nomenclatura gramatical (NGB e termos correntes)"
  - "Classificação de palavras (paroxítona, proparoxítona, etc.)"
  - "Definições de funções sintáticas (predicativo, adjunto, etc.)"
  - "Distinção entre conceitos próximos (acento vs. diacrítico vs. sinal gráfico)"
  - "Uso correto de 'sentido literal', 'sentido figurado', 'conotativo', 'denotativo'"
  - "Classificação de tipos de verbos (estado, ligação, processo, ação)"
  - "Distinção entre ditongo crescente, decrescente, hiato"
severity_if_wrong: 🔴 se induz ao erro em prova | 🟡 se é imprecisão sem consequência de prova
fonte_referencia: "Bechara (Moderna Gramática Portuguesa), Cunha & Cintra (Nova Gramática), VOLP"
```

### Step 5: Verificar Coerência de Exemplos (C3)

```yaml
action: "Para cada regra enunciada, verificar se os exemplos a confirmam"
checks:
  - "O exemplo ilustra exatamente a regra descrita no mesmo parágrafo?"
  - "O exemplo não contradiz alguma exceção mencionada em outra seção?"
  - "Os exemplos são canônicos (usados em gramáticas de referência ou bancas)?"
  - "Exemplos negativos (o que NÃO é) estão claramente marcados?"
  - "A palavra usada como exemplo pertence à categoria afirmada?"
severity_if_wrong: 🔴 se o exemplo contradiz a regra | 🟡 se é exemplo fraco ou não canônico
fonte_referencia: "Gramáticas de referência + banco de questões de concursos"
```

### Step 6: Verificar Completude Crítica (C4)

```yaml
action: >
  Verificar se exceções fundamentais para concursos estão presentes
  quando a regra principal é ensinada
checks:
  - "Regra ensinada tem exceção clássica de banca → está mencionada?"
  - "Ausência da exceção cria ambiguidade no artigo?"
  - "Ausência induziria o aluno a marcar errado em prova?"
note: >
  Omissão de conteúdo NÃO é erro conceitual por padrão.
  Reportar apenas quando a omissão cria risco direto de erro em prova.
severity_if_missing: 🟡 (imprecisão por incompletude com risco de prova)
```

### Step 7: Verificar Consistência Interna (C5)

```yaml
action: >
  Verificar se o mesmo conceito é explicado de forma uniforme
  em todas as seções do artigo
checks:
  - "A definição do conceito em H2-1 é compatível com o uso em H2-3?"
  - "Exemplos usados em seções diferentes são coerentes entre si?"
  - "FAQ repete/confirma a explicação das seções principais?"
  - "Não há contradição entre o critério ensinado e o exemplo resolvido?"
severity_if_wrong: 🔴 (contradição interna é sempre crítica — ver QA_CPT_005)
```

### Step 8: Verificar Precisão Semântica (C6)

```yaml
action: "Verificar se as definições capturam o conceito com precisão suficiente"
checks:
  - "A definição não simplifica a ponto de criar erro conceitual?"
  - "Termos próximos são distinguidos quando a distinção tem relevância de prova?"
  - "O mecanismo explicado (ex: transferência semântica) está correto?"
  - "Não há equivalências falsas (A = B quando A ≠ B)"
severity_if_wrong: 🔴 se cria erro de prova | 🟡 se é simplificação aceitável
```

### Step 9: Montar Relatório

```yaml
action: "Consolidar todos os itens identificados em relatório estruturado"
output_format: |
  ## RELATÓRIO QA CONCEITUAL — {keyword}
  Gate: RS-003.5
  Executor: analista-conceitual-pt

  ### Resumo Executivo
  | Severidade | Quantidade |
  |------------|-----------|
  | 🔴 Crítico | {n} |
  | 🟡 Médio   | {n} |
  | ⚪ Menor   | {n} |

  **Veredito: PASS / FAIL**

  ---

  ### Itens Identificados

  **🔴 {ID} — {Título do Problema}**
  Trecho atual: "{citação exata}"
  Problema: {explicação técnica}
  Fonte: ({gramática ou norma})
  Correção: "{texto correto sugerido}"

  **🟡 {ID} — {Título}**
  [mesma estrutura]

  **⚪ {ID} — {Título}**
  [mesma estrutura]

  ---

  ### Itens Corretos
  | Conceito | Avaliação |
  |----------|-----------|
  | {conceito} | Correto |

  ---
  GATE RS-003.5: {PASS / FAIL}
  Motivo do FAIL (se aplicável): {lista de IDs críticos}
```

### Step 10: Emitir Veredito

```yaml
PASS:
  condition: "zero itens 🔴"
  action: >
    Emitir relatório com PASS.
    Enviar lista de itens 🟡/⚪ ao seo-writer para correção opcional.
    Liberar artigo para sub_phase_2c (output-packager).

FAIL:
  condition: "um ou mais itens 🔴"
  action: >
    Emitir relatório com FAIL.
    Enviar relatório completo ao seo-writer com todos os itens 🔴 e 🟡.
    Bloquear passagem para sub_phase_2c até nova rodada de análise.
    O seo-writer corrige os itens críticos e resubmete o artigo.
```

---

## Outputs

### PASS

```
✅ RS-003.5 PASS — QA Conceitual aprovado

Keyword: {keyword}
Erros críticos (🔴): 0
Imprecisões médias (🟡): {n}
Avisos menores (⚪): {n}

[relatório completo com todos os itens]

Pipeline liberado → sub_phase_2c (output-packager)
```

### FAIL

```
❌ RS-003.5 FAIL — QA Conceitual bloqueado

Keyword: {keyword}
Erros críticos (🔴): {n} — CORREÇÃO OBRIGATÓRIA

[relatório completo com todos os itens]

Pipeline pausado → seo-writer deve corrigir os itens 🔴 e resubmeter
```

---

## Validation Criteria (Gate RS-003.5)

- [ ] Todos os claims do artigo foram verificados
- [ ] Zero erros 🔴 para emitir PASS
- [ ] Relatório emitido com veredito explícito (PASS ou FAIL)
- [ ] Cada item do relatório tem citação exata + problema + fonte + correção
- [ ] Itens corretos documentados na tabela de confirmação

---

## Error Handling

| Situação | Ação |
|----------|------|
| Artigo sem afirmações técnicas verificáveis | PASS automático com nota "conteúdo não-técnico" |
| Erro crítico com correção ambígua | FAIL + solicitar especialista externo |
| Contradição interna sem resolução clara | FAIL + marcar como 🔴 conflito interno |

---

_Task Version: 1.0.0_
_Executor: analista-conceitual-pt_
_Gate: RS-003.5_
