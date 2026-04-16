# Task: Escrever na Planilha XLSX

**Command:** `*escrever-planilha {xlsx_input} {output_path} {results_data}`
**Execution Type:** Auto
**Script:** `scripts/xlsx-manager.py --action=write`
**Executor:** @maestro

## Propósito

Escrever os briefings gerados de volta no arquivo XLSX, nas colunas corretas:
- Coluna T ("Prompt Adicional"): briefing E.E.A.T.S. completo
- Coluna U ("Termos LSI"): termos LSI estruturados

Sempre salvar como novo arquivo (nunca sobrescrever o original).

## Workflow

### Fase 1: Preparar Output

1. Carregar o arquivo XLSX original
2. Para cada linha processada, preparar:
   - `prompt_adicional`: briefing completo (texto Markdown)
   - `termos_lsi`: termos LSI em formato de texto separado por vírgulas ou quebra de linha

**Formatação dos Termos LSI para a planilha:**
```
[Cluster Regulatório]: termo1, termo2, termo3
[Cluster Mecânico]: termo1, termo2, termo3
[Cluster Risco/Conformidade]: termo1, termo2, termo3
[Cluster Execução]: termo1, termo2, termo3
```

### Fase 2: Executar Escrita

```bash
python scripts/xlsx-manager.py \
  --action=write \
  --input="{xlsx_input}" \
  --output="{output_path}" \
  --data="{results_json}"
```

O script vai:
1. Abrir o arquivo original
2. Para cada linha no results_data:
   - Localizar a linha pelo número
   - Escrever `prompt_adicional` na coluna T
   - Escrever `termos_lsi` na coluna U
3. Salvar no output_path (nunca sobrescrever input)
4. Reportar colunas e linhas escritas

### Fase 3: Validar Escrita

Após salvar, re-abrir o arquivo e verificar:
- Colunas T e U da linha processada têm conteúdo
- Conteúdo começa com "## BRIEFING DO ARTIGO" (verificação básica)
- Outras colunas não foram alteradas

#### >>> CHECKPOINT: Integridade da escrita <<<

```yaml
checkpoint_escrita:
  question: "Dados escritos corretamente nas colunas T e U?"
  if_sim: "Reportar sucesso"
  if_nao: "Tentar novamente — se falhar 2x, reportar erro com detalhes"
  verificacoes:
    - "Coluna T tem conteúdo > 500 caracteres"
    - "Coluna U tem conteúdo com clusters LSI"
    - "Outras colunas preservadas sem alteração"
```

### Fase 4: Confirmar Saída

Reportar ao usuário:
```
✅ Planilha salva: {output_path}
   Linhas escritas: {N}
   Colunas atualizadas: T (Prompt Adicional), U (Termos LSI)
```

## Validação de Saída

- [ ] Arquivo salvo no output_path (não sobrescreveu o original)
- [ ] Todas as linhas processadas têm dados nas colunas T e U
- [ ] Outras colunas da planilha preservadas sem modificação
- [ ] Path do arquivo salvo reportado ao usuário
