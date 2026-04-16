# Task: Auto-Onboarding de Cliente

**Command:** Ativado automaticamente quando usuário entrega xlsx + contexto de empresa
**Execution Type:** Interactive (confirmar apenas quando houver ambiguidade)
**Script:** `scripts/xlsx-manager.py --action=auto-onboard` + `--action=save-client`
**Executor:** @maestro

## Propósito

Detectar automaticamente se a empresa do contexto fornecido já está cadastrada,
criar o cadastro se for nova, e iniciar o pipeline sem precisar de comandos manuais.
O usuário entrega xlsx + contexto → o sistema resolve o resto.

## Gatilho

Esta task é acionada sempre que o usuário entregar **simultaneamente**:
- Um caminho de arquivo `.xlsx` (ou a planilha em si)
- Um texto de contexto de empresa (entre `<contexto-empresa>` ou como texto corrido)

**Sinais de que o usuário entregou os dois juntos:**
- "aqui está minha planilha e o contexto da empresa: ..."
- Mensagem com path de xlsx + bloco de texto de empresa
- Anexo xlsx + texto começando com nome de empresa + "é uma empresa..."

---

## Workflow

### Fase 1: Salvar Contexto em Arquivo Temporário

Salvar o texto do contexto em um arquivo temporário para uso no script:

```
Caminho temp: scripts/.context_temp.txt
```

Remover tags `<contexto-empresa>` / `</contexto-empresa>` se presentes antes de salvar.

### Fase 2: Executar Auto-Onboard

```bash
python scripts/xlsx-manager.py \
  --action=auto-onboard \
  --file="{xlsx_path}" \
  --context="scripts/.context_temp.txt"
```

### Fase 3: Interpretar Resultado e Agir

#### Caso A: `"acao": "use_existing"` — cliente já cadastrado

```
Mostrar ao usuário:
"✅ {nome} já está cadastrado (similaridade: {X}%).
 Contexto atual disponível: {Sim/Não}
 {mensagem}
 {pergunta}"

Se usuário responder [S] (confirmar, sem atualizar):
  → Carregar clients/{slug}.md como contexto ativo
  → Prosseguir direto para *processar-lote

Se usuário responder [N] (atualizar contexto):
  → Executar save-client com o novo texto (--slug={slug} existente)
  → Confirmar: "Contexto de {nome} atualizado."
  → Prosseguir para *processar-lote
```

#### >>> CHECKPOINT: Confirmação de cliente existente <<<

```yaml
checkpoint_existente:
  elicit: true
  pergunta: "Confirma que é {nome}? [S] Usa contexto atual / [A] Atualiza / [N] Cria novo"
  if_S: "carregar contexto existente → pipeline"
  if_A: "executar save-client com novo texto → pipeline"
  if_N: "tratar como create_new com nome diferente → pedir nome correto"
```

---

#### Caso B: `"acao": "confirm_match"` — nome similar encontrado

```
Mostrar ao usuário:
"⚠️ Encontrei '{cliente_similar.nome}' já cadastrado (similaridade: {X}%).
   Nome extraído do contexto: '{nome_extraido}'
   {pergunta}"

Se usuário responder [S] (é o mesmo):
  → Usar clients/{slug_similar}.md
  → Perguntar se quer atualizar o contexto

Se usuário responder [N] (é empresa diferente):
  → Usar nome_extraido como nome da nova empresa
  → Prosseguir para Caso C (create_new)
```

#### >>> CHECKPOINT: Confirmar match parcial <<<

```yaml
checkpoint_similar:
  elicit: true
  pergunta: "[S] Mesmo cliente / [N] Empresa diferente"
  timeout_padrao: "S"  # Se não responder, assumir empresa diferente por segurança
```

---

#### Caso C: `"acao": "create_new"` — empresa nova

```
Mostrar ao usuário:
"📋 Empresa nova detectada: '{nome_extraido}' (confiança: {alta/media/baixa})
   Slug sugerido: {slug_sugerido}
   Aliases gerados: {aliases_sugeridos}"

Perguntar (somente se confiança for 'baixa' ou 'nenhuma'):
  "Confirma o nome '{nome_extraido}'? [S/N — se N, qual é o nome correto?]"

Se confiança for 'alta' ou 'media':
  Prosseguir automaticamente sem perguntar o nome.

Executar criação:
```

```bash
python scripts/xlsx-manager.py \
  --action=save-client \
  --slug="{slug_sugerido}" \
  --nome="{nome_extraido}" \
  --setor="{setor_se_disponivel}" \
  --context="scripts/.context_temp.txt"
```

```
Confirmar ao usuário:
"✅ '{nome}' cadastrado com sucesso!
   Arquivo: clients/{slug}.md
   Aliases para detecção automática: {aliases}

   💡 Nomeie seus xlsx como '{slug}_posts.xlsx' para detecção automática futura."

→ Prosseguir para *processar-lote
```

#### >>> CHECKPOINT: Criação automática de nome de alta confiança <<<

```yaml
checkpoint_auto_criar:
  question: "Confiança da extração do nome é alta ou media?"
  if_alta_ou_media: "Criar automaticamente sem confirmar o nome"
  if_baixa: "Mostrar nome extraído e confirmar com usuário antes de criar"
  rationale: "Alta confiança = nome claro no texto. Baixa = nome ambíguo ou ausente."
```

---

### Fase 4: Limpar Arquivo Temporário

Após cadastro realizado (ou confirmado):

```bash
# Remover arquivo temporário de contexto
# (o contexto permanente está em clients/{slug}.md)
```

Não deixar `scripts/.context_temp.txt` com dados de cliente.

### Fase 5: Transição para Pipeline

Após resolver o cliente, executar automaticamente:

```
*processar-lote {xlsx_path}
```

O contexto correto já está em `clients/{slug}.md` e será carregado pelo `--action=read`.

---

## Casos Especiais

### Contexto sem nome identificável

Se `nome_extraido = null` e `confianca = nenhuma`:

```
Mostrar: "Não consegui identificar o nome da empresa no texto fornecido.
          Qual é o nome da empresa?"
→ Aguardar resposta
→ Usar o nome fornecido como {nome_extraido}
→ Continuar Caso C
```

### Múltiplos clientes com o mesmo alias

Improvável, mas se ocorrer:

```
Mostrar lista dos clientes com conflito
→ Pedir escolha manual
```

### Usuário entrega só o xlsx (sem contexto)

Se não houver texto de contexto:

```
→ Executar detecção normal pelo nome do arquivo (detect-client)
→ Se não detectado: *listar-clientes → pedir escolha
→ Se não há clientes: "Nenhum cliente cadastrado. Cole o contexto da empresa para cadastrar."
```

---

## Resumo dos 3 Casos

| Caso | Condição | Ação automática | Confirmação necessária |
|------|----------|----------------|----------------------|
| A | Cliente já existe (similaridade ≥ 70%) | Usar existente | Só se usuário quiser atualizar |
| B | Similar encontrado (30–69%) | Pergunta | Sim — [S/N] |
| C | Empresa nova (< 30% ou nenhum match) | Criar automaticamente | Só se confiança do nome for baixa |

## Validação Final

- [ ] Cliente identificado (existente ou criado)
- [ ] `clients/{slug}.md` tem conteúdo > 50 palavras
- [ ] `clients/_index.yaml` tem a entrada do cliente
- [ ] Arquivo temporário removido
- [ ] Pipeline `*processar-lote` iniciado
