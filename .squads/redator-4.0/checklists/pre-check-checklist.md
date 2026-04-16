# Pre-Check Checklist

**ID:** pre-check-checklist
**Gate:** SP-000
**Executor:** client-validator
**Blocking:** Sim — pipeline não avança se qualquer item crítico falhar

---

## Checklist de Validação

### Identificação do Cliente

- [ ] **[CRÍTICO]** `cliente_slug` fornecido e não vazio
- [ ] **[CRÍTICO]** `cliente_slug` não contém espaços (usar hífen se necessário)

### Arquivo de Contexto

- [ ] **[CRÍTICO]** Arquivo `redator-2.0/knowledge/clients/{slug}-marketing.md` existe
- [ ] **[CRÍTICO]** Arquivo não está vazio (word_count > 0)
- [ ] **[AVISO]** Arquivo tem >= 300 palavras (recomendado para qualidade)
- [ ] **[AVISO]** Arquivo contém dados financeiros (valores, %, prazos)
- [ ] **[AVISO]** Arquivo descreve o público-alvo

### Entidades Extraídas

- [ ] **[CRÍTICO]** `nome_empresa` identificado
- [ ] **[CRÍTICO]** `modelo_negocio` identificado
- [ ] **[RECOMENDADO]** `dados_financeiros` identificados
- [ ] **[RECOMENDADO]** `diferenciais` identificados (pelo menos 1)
- [ ] **[RECOMENDADO]** `publico_alvo` identificado

### Planilha de Keywords

- [ ] **[AVISO]** Arquivo da planilha existe no caminho informado
- [ ] *Se não existe: modo fallback manual habilitado*

---

## Resultados Possíveis

| Resultado | Condição | Ação |
|-----------|----------|------|
| ✅ PASS | Todos os itens CRÍTICOS aprovados | Pipeline continua |
| ⚠️ PASS COM AVISO | Críticos OK + alguns AVISOS | Continuar + informar usuário |
| ❌ BLOCK | Qualquer item CRÍTICO falhou | Pausar + solicitar ação |

---

## Mensagens de Bloqueio

```
[SLUG VAZIO]
❌ PRE-CHECK BLOQUEADO
Slug do cliente não fornecido.
Use: *produce {slug} {caminho_planilha}
Exemplo: *produce peggo "redator-2.0/knowledge/clients/Peggo março 2026.xlsx"

[ARQUIVO NÃO EXISTE]
❌ PRE-CHECK BLOQUEADO
Contexto do cliente não encontrado.
Esperado: redator-2.0/knowledge/clients/{slug}-marketing.md
Crie o arquivo com as informações do cliente antes de continuar.

[ARQUIVO VAZIO]
❌ PRE-CHECK BLOQUEADO
Arquivo de contexto existe mas está vazio.
Adicione as informações do cliente em: redator-2.0/knowledge/clients/{slug}-marketing.md

[CONTEXTO INSUFICIENTE]
⚠️ AVISO: Contexto com apenas {N} palavras (recomendado: 300+)
O conteúdo produzido pode ser genérico por falta de dados específicos do cliente.
Continuar mesmo assim? (s/n)
```
