# Task: Cadastrar Cliente

**Command:** `*cadastrar-cliente`
**Execution Type:** Interactive (elicitation obrigatória)
**Executor:** @maestro

## Propósito

Cadastrar um novo cliente no sistema de contextos, criando o arquivo
`clients/{slug}.md` e adicionando a entrada em `clients/_index.yaml`.
Após cadastrado, o cliente é detectado automaticamente pelo nome do xlsx.

## Workflow

### Fase 1: Coletar Dados do Cliente

Perguntar ao usuário em sequência:

```
1. Nome da empresa:
   → Ex: "Mand Digital" ou "Empresa XYZ"

2. Slug (identificador único, gerado automaticamente com sugestão):
   → Sugestão: {nome_em_lowercase_com_hifens}
   → Ex: "mand-digital"
   → Confirmar ou alterar

3. Setor / Nicho:
   → Ex: "Promoções Comerciais Regulamentadas"
   → Ex: "E-commerce de moda"

4. Aliases para detecção no nome do arquivo xlsx:
   → Sugestão automática baseada no slug (3-4 variações)
   → Ex: mand, mand-digital, manddigital, mand_digital
   → Confirmar ou adicionar mais

5. Contexto da empresa:
   → "Cole o texto completo do <contexto-empresa> da empresa."
   → Aceitar texto multilinhas
   → Confirmar quando terminar (sinal: linha vazia + Enter, ou "FIM")
```

#### >>> CHECKPOINT: Dados mínimos <<<

```yaml
checkpoint_dados:
  obrigatorios:
    - nome: "não vazio"
    - slug: "só letras, números e hífens"
    - contexto: "pelo menos 100 palavras"
  se_incompleto: "Solicitar os campos faltantes antes de prosseguir"
  bloqueante: true
```

### Fase 2: Criar Arquivo de Contexto

Criar `clients/{slug}.md` com o seguinte conteúdo:

```markdown
# Contexto da Empresa — {Nome da Empresa}

{contexto_fornecido_pelo_usuario}
```

### Fase 3: Atualizar _index.yaml

Adicionar ao final da lista `clientes:` em `clients/_index.yaml`:

```yaml
  - slug: {slug}
    nome: "{Nome da Empresa}"
    arquivo: "clients/{slug}.md"
    aliases:
      - {alias_1}
      - {alias_2}
      - {alias_3}
    setor: "{setor}"
    ativo: true
```

#### >>> CHECKPOINT: Verificar criação <<<

```yaml
checkpoint_criacao:
  verificar:
    - "clients/{slug}.md existe e tem conteúdo"
    - "clients/_index.yaml tem a nova entrada"
    - "detect-client funciona com um nome de arquivo de teste"
  se_falha: "Reportar erro específico e tentar novamente"
```

### Fase 4: Testar Detecção

Executar teste de detecção com o novo slug:

```bash
python scripts/xlsx-manager.py --action=detect-client \
  --file="{slug}_test.xlsx"
```

Esperado: `"detectado": true, "confianca": "alta"`

### Fase 5: Confirmar ao Usuário

```
✅ Cliente cadastrado com sucesso!

  Nome: {Nome da Empresa}
  Slug: {slug}
  Arquivo: clients/{slug}.md
  Aliases: {lista}

💡 Para detecção automática, nomeie seus xlsx com o slug:
   Ex: {slug}_posts-abril-2026.xlsx

Para processar: *processar-lote {slug}_posts.xlsx
```

## Validação de Saída

- [ ] `clients/{slug}.md` criado com contexto ≥ 100 palavras
- [ ] `clients/_index.yaml` atualizado com nova entrada
- [ ] Teste de detecção automática passou
- [ ] Usuário informado sobre convenção de nome de arquivo
