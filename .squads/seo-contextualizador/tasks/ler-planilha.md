# Task: Ler Planilha XLSX

**Command:** `*ler-planilha {xlsx_path}`
**Execution Type:** Auto
**Script:** `scripts/xlsx-manager.py --action=read`
**Executor:** @maestro

## Propósito

Ler o arquivo XLSX fornecido pelo usuário, identificar as linhas que contêm
"Palavra-chave Foco" + "Título" preenchidos, e retornar uma lista estruturada
com: número da linha, keyword, título, idioma, e status atual de "Prompt Adicional".

## Estrutura Esperada da Planilha

| Coluna | Header | Papel |
|--------|--------|-------|
| A | Idioma | Contexto de idioma (ex: "Português (Brasil)") |
| B | Palavra-chave Foco | **INPUT — keyword do artigo** |
| C | Título | **INPUT — título proposto do artigo** |
| D | Slug (URL amigável) | Metadado opcional |
| E | Post Type | Metadado opcional |
| F | Categoria | Contexto adicional |
| G | Tags | Contexto adicional |
| ... | ... | ... |
| T | Prompt Adicional | **OUTPUT — briefing E.E.A.T.S. gerado** |
| U | Termos LSI | **OUTPUT — termos LSI gerados** |

## Workflow

### Fase 1: Validar Arquivo

1. Verificar se o arquivo existe no path fornecido
2. Verificar se é um arquivo .xlsx válido
3. Verificar se a linha 1 contém os headers esperados
4. Se header "Palavra-chave Foco" não encontrado → PARAR e alertar usuário

#### >>> CHECKPOINT: Validação de arquivo <<<

```yaml
checkpoint_arquivo:
  question: "O arquivo existe e tem os headers esperados?"
  if_sim: "Prosseguir para leitura de linhas"
  if_nao: "PARAR — informar usuário: 'Arquivo não encontrado ou headers incorretos. 
            Esperado: Palavra-chave Foco (col B), Título (col C)'"
  bloqueante: true
```

### Fase 2: Ler Linhas

**Executar:**
```bash
python scripts/xlsx-manager.py --action=read --file="{xlsx_path}"
```

**Critério de inclusão:** Linha é processável se:
- `Palavra-chave Foco` (col B) está preenchida (não vazia)
- `Título` (col C) está preenchido (não vazio)
- `Prompt Adicional` (col T) está VAZIO (linha ainda não processada)

**Critério de re-processamento:** Incluir linha mesmo com Prompt Adicional preenchido
se usuário usou flag `--forcar-reprocessamento`

### Fase 3: Apresentar Resumo ao Usuário

```
📋 Planilha: {xlsx_path}
Total de linhas: {N}
Linhas processáveis (keyword + título preenchidos, prompt vazio): {X}
Linhas já processadas (prompt preenchido): {Y}
Linhas incompletas (sem keyword ou título): {Z}

Linhas a processar:
  Linha 2: "palavra-chave foco" | "Título do artigo"
  Linha 3: "palavra-chave foco 2" | "Título do artigo 2"
  ...

Deseja processar todas as {X} linhas? [S/N] ou especifique: --linhas=2,3,5
```

#### >>> CHECKPOINT: Confirmação do usuário <<<

```yaml
checkpoint_confirmacao:
  question: "Usuário confirmou quais linhas processar?"
  if_confirmado: "Passar lista de linhas para *processar-lote"
  if_aguardando: "HALT — esperar input"
  elicit: true
```

### Fase 4: Retornar Estrutura de Dados

Retornar para @maestro uma lista estruturada:

```yaml
linhas_para_processar:
  - numero: 2
    keyword: "o que é sorteio comercial"
    titulo: "O que é Sorteio Comercial: como funciona e o que exige a lei"
    idioma: "Português (Brasil)"
    categoria: "Promoções Comerciais"
    prompt_adicional_atual: null
  - numero: 3
    keyword: "..."
    titulo: "..."
    ...
```

## Validação de Saída

- [ ] Arquivo lido sem erros
- [ ] Headers identificados corretamente
- [ ] Lista de linhas processáveis retornada
- [ ] Usuário confirmou linhas a processar
- [ ] Estrutura de dados pronta para *processar-lote
