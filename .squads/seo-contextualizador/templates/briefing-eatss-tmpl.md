# Template: Briefing E.E.A.T.S.

> Template usado por @atlas para formatar o output final que vai para a coluna
> "Prompt Adicional" da planilha XLSX.

---

## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** {{keyword}}
**Tipo de artigo:** {{tipo_artigo}} (ex: Educacional/Blog, Landing Page, Pilar)
**Funil:** {{funil}} (Topo — intenção informacional | Meio | Fundo)
**Objetivo estratégico:** {{objetivo_estrategico}}

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

**Definição-base para o Entity Lock-in:**
{{definicao_base}}
*(Incluir: finalidade + mecanismo central + requisito legal/principal + quem pode usar)*

**Escopo a delimitar (o que é / o que não é):**
- É: {{e_lista}} *(promoção com finalidade X, autorizada por Y, com Z como mecanismo)*
- Não é: {{nao_e_lista}} *(diferença de rifa, jogo de azar, confusão comum 1, confusão comum 2)*

**Diretrizes de implementação:**
- H1 deve conter a entidade principal e delimitar escopo imediatamente
- Primeiro parágrafo: definição + problema central (maioria das empresas/pessoas não sabe que X)
- Nenhuma seção pode "puxar" o contexto para outro assunto sem retornar à entidade central
- Nomear "{{keyword}}" explicitamente em parágrafos-chave (sem pronomes vagos isolados)

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

Subentidades obrigatórias que o espaço vetorial espera encontrar neste artigo:

| Subentidade | Categoria | Profundidade esperada |
|------------|-----------|----------------------|
| {{subentidade_1}} | {{categoria_1}} | {{profundidade_1}} |
| {{subentidade_2}} | {{categoria_2}} | {{profundidade_2}} |
| {{subentidade_3}} | {{categoria_3}} | {{profundidade_3}} |
| {{subentidade_4}} | {{categoria_4}} | {{profundidade_4}} |
| {{subentidade_5}} | {{categoria_5}} | {{profundidade_5}} |
| {{subentidade_6}} | {{categoria_6}} | {{profundidade_6}} |
| {{subentidade_7}} | {{categoria_7}} | {{profundidade_7}} |
| {{subentidade_8}} | {{categoria_8}} | {{profundidade_8}} |
*(Adicionar mais linhas conforme necessário — mínimo 8)*

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Atributos internos de {{keyword}} que o artigo deve cobrir:
```
Entidade: {{keyword_principal}}
├── Finalidade → {{finalidade}}
├── Autorização → {{autorizacao}}
├── Mecânica → {{mecanica}}
├── Gratuidade/Custo → {{gratuidade}}
├── Elegibilidade → {{elegibilidade}}
├── Base legal → {{base_legal}}
├── Modalidades relacionadas → {{modalidades}}
├── Riscos da ausência → {{riscos}}
├── Prazo de execução → {{prazo}}
├── Canais → {{canais}}
├── Segmentos usuários → {{segmentos}}
└── Dados mensuráveis → {{dados_mensuraveis}}
```

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

Posicionamento taxonômico da entidade no espaço semântico:

| Relação | Entidade | Como trabalhar no artigo |
|---------|----------|------------------------|
| Hiperônimo | {{hiperonimo}} | "{{keyword}} é uma das modalidades de {{hiperonimo}}" |
| Hipônimos | {{hiponimos}} | Explicar o mecanismo específico |
| Co-hipônimos | {{co_hiponimos}} | Seção dedicada às diferenças entre modalidades |
| Análogos | {{analogos}} | Termos intercambiáveis com precisão |
| Contraste direto | {{contraste_1}} | {{como_contrastar_1}} |
| Contraste direto 2 | {{contraste_2}} | {{como_contrastar_2}} |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

**Intenções explícitas a cobrir (SERP-derived):**

| Intenção | Template | Seção sugerida |
|----------|---------|---------------|
| Definição | O que é {{keyword}} | H2 de abertura, primeiro bloco |
| Mecanismo | Como funciona {{keyword}} | H2 explicando {{mecanismo_central}} |
| Tipologia | Tipos / modalidades de {{categoria}} | H2 comparando modalidades |
| Base legal | Lei do {{keyword}} / regulamentação | H2 dedicado à legislação |
| Procedimento | Como fazer {{keyword}} | H2/H3 — etapas |
| Risco | O que acontece sem {{requisito}} | H2/H3 — consequências |
| Diferenciação | {{keyword}} vs {{contraste_1}} | Seção de contraste semântico |
| Elegibilidade | Quem pode realizar {{keyword}} | H3 dentro de mecânica |

**Intenções latentes a cobrir (inferidas):**

| Intenção Latente | Gap se ausente | Seção sugerida |
|-----------------|---------------|---------------|
| Quanto custa {{keyword}} | Perde intenção comercial de fundo | Menção ao investimento, orientar para contato |
| Quanto tempo leva | Intenção prática — quem quer planejar | H3 dentro de procedimento |
| Quais segmentos podem fazer | Intenção investigativa | Exemplos reais: {{segmento_1}}, {{segmento_2}} |
| Exemplos de {{keyword}} reais | Prova social + contextual embedding | Exemplos como {{exemplo_case}} |
| Como escolher empresa para executar | Intenção de conversão | Seção final com CTA para {{empresa_cliente}} |
| {{intencao_latente_especifica}} | {{gap_especifico}} | {{secao_sugerida}} |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

Elementos para criar densidade contextual e maximizar citabilidade GEO:

- **Exemplos práticos documentados:** {{cases_reais}}
- **Cenários de aplicação por segmento:**
  - {{segmento_1}}: {{cenario_1}}
  - {{segmento_2}}: {{cenario_2}}
  - {{segmento_3}}: {{cenario_3}}
- **Erros comuns:** {{erros_comuns}}
- **Boas práticas:** {{boas_praticas}}
- **Referências legítimas:** {{referencias_legitimas}}
- **Frases GEO-citáveis (entidade nomeada, sem pronome vago):**
  - "{{frase_geo_1}}"
  - "{{frase_geo_2}}"
  - "{{frase_geo_3}}"

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

O fechamento deve:
- Reafirmar a entidade: {{keyword}} como {{posicionamento_estrategico}}
- Sintetizar os atributos principais: {{atributos_principais_bullet}}
- Conectar com a intenção inicial: o leitor que chegou querendo entender {{intent_inicial}} agora sabe {{resultado_esperado}}
- Direção para ação: CTA natural para {{empresa_cliente}} — empresa especializada em {{especialidade}}
- Não introduzir entidades novas no fechamento

---

## TERMOS LSI OBRIGATÓRIOS

**Cluster {{cluster_1_nome}} ({{cluster_1_prioridade}} prioridade):**
{{cluster_1_termos}}

**Cluster {{cluster_2_nome}} ({{cluster_2_prioridade}} prioridade):**
{{cluster_2_termos}}

**Cluster {{cluster_3_nome}} ({{cluster_3_prioridade}} prioridade):**
{{cluster_3_termos}}

**Cluster {{cluster_4_nome}} ({{cluster_4_prioridade}} prioridade):**
{{cluster_4_termos}}

*(Adicionar cluster 5 se relevante)*

---

## POWER KEYWORDS APLICÁVEIS

- **H1 / título:** {{power_h1}}
- **H2 de risco/conformidade:** {{power_h2_risco}}
- **H2 de diferenciação:** {{power_h2_diferenciacao}}
- **H2 de procedimento:** {{power_h2_procedimento}}
- **Seção de intenção latente:** {{power_latente}}
- **CTA/fechamento:** {{power_cta}}

---

## ESTRUTURA DE OUTLINE SUGERIDA

```
H1: {{h1_otimizado}}
[Lead GEO — 2-3 frases citáveis com definição, {{requisito_principal}} e mecanismo]

H2: {{h2_definicao}}
  H3: {{h3_diferenciacao_critica}}

H2: {{h2_mecanismo}}
  H3: {{h3_mecanismo_1}}
  H3: {{h3_mecanismo_2}}
  H3: {{h3_elegibilidade}}

H2: {{h2_comparativo}}
  [Tabela comparativa das modalidades]

H2: {{h2_legal}}
  H3: {{h3_legislacao}}
  H3: {{h3_orgao_regulador}}
  H3: {{h3_risco_sem_autorizacao}}

H2: {{h2_procedimento}}
  H3: {{h3_passo_1}}
  H3: {{h3_passo_2}}
  H3: {{h3_passo_3}}

H2: {{h2_exemplos}}
  [{{segmento_1}}, {{segmento_2}}, {{segmento_3}}]

H2: {{h2_erros_comuns}}

H2: {{h2_cta_empresa}}
  [<cta> ver seção CTA abaixo </cta>]

FAQ (mínimo 5 perguntas)
```

---

## RESTRIÇÕES E DIRETRIZES EDITORIAIS

**SEMPRE fazer:**
{{sempre_fazer_lista}}

**NUNCA fazer:**
{{nunca_fazer_lista}}

**Aviso legal obrigatório** (incluir no rodapé ou nota do artigo):
> {{aviso_legal_cliente}}

---

## SEÇÃO DE CTA

```
URL do silo: {{url_silo}}
Posição: H2 final do artigo, antes do FAQ

Título da seção: {{titulo_cta_secao}}

Conteúdo: {{conteudo_cta}}
*(Mencionar especialização, infraestrutura própria, parceria com agências se aplicável)*

Frase de fechamento sugerida:
"{{frase_fechamento_cta}}"

CTA final: {{link_formulario}}
Texto do botão/link: Fale com nosso time

Tom: {{tom_cliente}}
Aviso legal: {{aviso_legal_cta}}
```
