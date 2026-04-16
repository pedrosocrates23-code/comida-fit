# Task: Processar Lote de Linhas

**Command:** `*processar-lote {xlsx_path} [--linhas=2,3,5] [--modo=rapido|completo]`
**Execution Type:** Hybrid (Auto por linha, confirmação ao final)
**Executor:** @maestro (orquestra @nebula + @atlas por linha)
**Load:** `tasks/ler-planilha.md`, `tasks/pesquisar-topico.md`, `tasks/gerar-briefing-eatss.md`, `tasks/escrever-planilha.md`

## Propósito

Orquestrar o pipeline completo de contextualização para múltiplas linhas da planilha:
ler → pesquisar (por linha) → gerar briefing (por linha) → escrever → salvar.

## Modos de Execução

| Modo | Pesquisa | Briefing | Uso |
|------|----------|---------|-----|
| `completo` (default) | 5 queries + 6 fases @nebula | 7 camadas completas + saídas | Produção |
| `rapido` | 2 queries principais | 7 camadas compactas | Preview/teste |

## Workflow

### Fase 0: Pre-Flight

1. Verificar se `data/contexto-empresa-ativo.md` está preenchido
2. Executar `*ler-planilha {xlsx_path}` → obter lista de linhas processáveis
3. Confirmar com usuário quais linhas processar

#### >>> CHECKPOINT: Pre-flight obrigatório <<<

```yaml
checkpoint_preflight:
  checks:
    - id: empresa
      verify: "data/contexto-empresa-ativo.md tem conteúdo > 100 palavras"
      if_falha: "PARAR — solicitar: 'Use *set-empresa para definir o contexto da empresa'"
      bloqueante: true
    - id: planilha
      verify: "xlsx_path existe e tem linhas processáveis"
      if_falha: "PARAR — arquivo não encontrado ou sem linhas válidas"
      bloqueante: true
    - id: confirmacao
      verify: "Usuário confirmou linhas a processar"
      if_falha: "HALT — aguardar confirmação"
      elicit: true
```

### Fase 1: Loop de Processamento por Linha

Para cada linha confirmada, executar sequencialmente:

```
┌─────────────────────────────────────────────────────┐
│ LINHA {N}: "{keyword}" | "{titulo}"                  │
├─────────────────────────────────────────────────────┤
│ STEP 1: @nebula *pesquisar-topico "{keyword}"        │
│         → aguardar research_findings                 │
│                                                      │
│ STEP 2: @atlas *gerar-briefing "{keyword}" "{titulo}"│
│         → aguardar briefing_completo                 │
│                                                      │
│ STEP 3: @maestro → armazenar em results[linha]       │
│         → reportar progresso: "Linha {N} concluída"  │
└─────────────────────────────────────────────────────┘
```

**Reporte de progresso a cada linha:**
```
✅ Linha {N}/{ total}: "{keyword}" — briefing gerado ({tamanho} palavras)
```

**Tratamento de erro por linha:**
- Se @nebula falhar → registrar erro, pular para próxima linha, reportar ao final
- Se @atlas falhar → registrar erro, pular para próxima linha, reportar ao final
- NÃO parar o lote inteiro por falha em uma linha

#### >>> CHECKPOINT: Qualidade por linha <<<

```yaml
checkpoint_qualidade_linha:
  question: "Briefing gerado para linha {N} tem todas as 7 camadas + ≥25 termos LSI?"
  if_sim: "Armazenar e prosseguir"
  if_nao: "Tentar regenerar — se falhar 2x, registrar como 'incompleto' e prosseguir"
  max_retries: 2
```

### Fase 2: Escrever na Planilha

Após processar todas as linhas (ou as selecionadas):

1. Executar `*escrever-planilha {xlsx_path} {output_path}` com todos os results
2. Para cada linha com resultado:
   - Coluna T ("Prompt Adicional"): briefing completo E.E.A.T.S.
   - Coluna U ("Termos LSI"): termos LSI em formato de texto/lista
3. Salvar como `{xlsx_nome}_contextualizado.xlsx` no mesmo diretório
4. NÃO sobrescrever o original — sempre salvar com novo nome

### Fase 3: Relatório Final

Apresentar ao usuário:

```
📊 RELATÓRIO DE PROCESSAMENTO
═══════════════════════════════════════
Planilha: {xlsx_path}
Processamento: {data_hora}

✅ Concluídas com sucesso: {N} linhas
⚠️  Com alertas: {M} linhas (detalhes abaixo)
❌ Falhas: {K} linhas (detalhes abaixo)

SAÍDA SALVA: {output_path}

DETALHES POR LINHA:
  Linha 2: ✅ "{keyword}" — {tamanho} palavras, {N_lsi} termos LSI
  Linha 3: ✅ "{keyword}" — {tamanho} palavras, {N_lsi} termos LSI
  ...

FALHAS (se houver):
  Linha {N}: ❌ Motivo: {erro}
═══════════════════════════════════════
```

### Fase 4: Confirmação Final

Perguntar ao usuário:
```
Deseja revisar algum briefing específico antes de finalizar?
  [S] Sim — qual linha?
  [N] Não — processamento concluído

Arquivo disponível em: {output_path}
```

#### >>> CHECKPOINT: Confirmação de conclusão <<<

```yaml
checkpoint_conclusao:
  elicit: true
  question: "Usuário quer revisar alguma linha?"
  if_sim: "Exibir briefing da linha solicitada para revisão"
  if_nao: "Reportar: 'Pipeline concluído. Planilha salva em {output_path}'"
```

## Validação Final do Lote

- [ ] Todas as linhas confirmadas foram processadas (ou registradas como erro)
- [ ] Planilha salva com novo nome (não sobrescreveu original)
- [ ] Colunas T e U preenchidas para cada linha de sucesso
- [ ] Relatório apresentado ao usuário
- [ ] Nenhuma linha processada sem pesquisa prévia de @nebula
