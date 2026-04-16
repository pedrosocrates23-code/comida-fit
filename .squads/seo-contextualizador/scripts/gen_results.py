#!/usr/bin/env python3
"""
Gera results_mand.json com os 10 briefings E.E.A.T.S. para Mand Digital.
Execução: python scripts/gen_results.py
"""
import json, os

SQUAD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Constantes reutilizadas em todos os briefings ────────────────────────────

AVISO_LEGAL = (
    "A Mand Digital elabora o regulamento e a estrutura técnica, mas a "
    "responsabilidade legal, execução e operação de cada campanha é "
    "integralmente do contratante."
)

ORGAOS = """\
ÓRGÃOS FISCALIZADORES (citar com link no artigo):
- SPA — Secretaria de Prêmios e Apostas / Ministério da Fazenda:
  https://www.gov.br/fazenda/pt-br/composicao/orgaos/secretaria-de-premios-e-apostas/promocao-comercial
- Lei nº 5.768/1971 (Planalto):
  https://www.planalto.gov.br/ccivil_03/leis/l5768.htm
- Decreto nº 70.951/1972 (Planalto):
  https://www.planalto.gov.br/ccivil_03/decreto/antigos/d70951.htm
- Portaria SEAE/ME nº 7.638/2022:
  https://www.normaslegais.com.br/legislacao/portaria-seae-me-7638-2022.htm
- SCPC — Sistema de Controle de Promoção Comercial:
  https://www.gov.br/fazenda/pt-br/composicao/orgaos/secretaria-de-premios-e-apostas/promocao-comercial/scpc"""

# ── Briefings ────────────────────────────────────────────────────────────────

B3_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** diferença entre sorteio e assemelhada a sorteio
**Tipo de artigo:** Informacional / Educativo
**Funil:** Topo (informacional de alta intenção — leitor quer entender a distinção antes de contratar)
**Objetivo estratégico:** Educar o mercado sobre as duas modalidades e posicionar a Mand Digital como especialista que domina ambas.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
- Sorteio é a modalidade de promoção comercial regulamentada em que a apuração dos ganhadores é feita exclusivamente por meio dos resultados da Loteria Federal. Cada participante recebe um número de série; o prêmio é entregue a quem tiver o número correspondente ao resultado sorteado.
- Promoção assemelhada a sorteio é a modalidade que simula a lógica do sorteio, mas utiliza algoritmos de aleatoriedade técnica validados — sem dependência da Loteria Federal. Permite múltiplas séries (acima de 100 mil números) e exige logs de auditoria independente.

ESCOPO DELIMITADO:
É sorteio: vinculado à Loteria Federal, 1 série de até 100 mil números, empresa não faz a apuração diretamente.
Não é sorteio: qualquer mecânica com sistema próprio de aleatoriedade, raspadinha digital com algoritmo próprio, campanhas com múltiplas séries simultâneas.
É assemelhada: sistema informatizado validado, múltiplas séries possíveis, auditoria técnica exigida, sem Loteria Federal.
Não é assemelhada: vale-brinde (premiação instantânea no envoltório), concurso (critério de habilidade).

DIRETRIZES DE IMPLEMENTAÇÃO:
- H1: deve nomear explicitamente ambas as entidades e o contexto regulatório.
  Ex.: "Sorteio ou assemelhada a sorteio: qual é a diferença e qual precisa de autorização?"
- Primeiro parágrafo: definir o problema (quem não entende a diferença pode errar na escolha da modalidade e ter a autorização negada).
- Regra de referência: nomear "sorteio" e "assemelhada a sorteio" explicitamente — nunca substituir por "eles" ou "as promoções".

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Loteria Federal | Mecanismo central de apuração (sorteio) | Alta — explicar dependência e limitação |
| SPA (Secretaria de Prêmios e Apostas) | Regulador/Órgão competente | Alta — citar com link oficial |
| Série de números sorteáveis | Atributo definidor | Alta — limite de 100 mil = critério técnico |
| Algoritmo de aleatoriedade técnica | Mecanismo central (assemelhada) | Alta — diferença técnica principal |
| Autorização prévia | Requisito legal (ambas) | Alta — obrigatório para as duas modalidades |
| Regulamento de promoção | Contexto institucional | Média — necessário para as duas |
| Auditoria/log independente | Atributo exclusivo da assemelhada | Média — exigido pela portaria |
| Raspadinha digital | Co-hipônimo (assemelhada na prática) | Média — exemplo mais comum |
| Lei 5.768/1971 | Base legal | Alta — citar com link |
| Portaria SEAE 7.638/2022 | Base legal complementar | Alta — citar com link |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Sorteio vs Assemelhada a Sorteio
├── Vínculo com Loteria Federal → Sorteio: obrigatório | Assemelhada: inexistente
├── Limite de números → Sorteio: 1 série de até 100 mil | Assemelhada: múltiplas séries (ilimitado)
├── Apuração → Sorteio: externa (Loteria Federal) | Assemelhada: sistema próprio validado
├── Auditoria técnica → Sorteio: desnecessária | Assemelhada: obrigatória (logs independentes)
├── Base legal → Lei 5.768/1971 + Decreto 70.951/1972 + Portaria SEAE 7.638/2022 (ambas)
├── Autorização → SPA/Ministério da Fazenda (obrigatória para ambas)
├── Prazo de pedido → Entre 120 e 40 dias antes do início da promoção
├── Escalonamento → Sorteio: limitado a 100 mil participantes por série | Assemelhada: sem limite prático
├── Uso digital → Sorteio: possível com NF + número vinculado | Assemelhada: nativa ao ambiente digital
├── Exemplos de uso → Sorteio: campanha de supermercado com cupons | Assemelhada: raspadinha digital com cadastro de NF
├── Segmentos usuários → Varejo, financeiro, alimentício, energia
└── Responsabilidade legal → integralmente do contratante (não da Mand Digital)

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar no artigo |
|---|---|---|
| Hiperônimo | Promoção comercial regulamentada | "Sorteio e assemelhada a sorteio são modalidades de promoção comercial regulamentada" |
| Hipônimos do sorteio | Sorteio simples, sorteio composto | Mencionar no contexto de limites de séries |
| Co-hipônimos | Vale-brinde, concurso, assemelhada a vale-brinde | Seção de comparação entre modalidades |
| Análogos populares | Rifa (incorreto juridicamente) | Corrigir explicitamente — rifa não tem autorização |
| Contraste direto | Loteria Federal × algoritmo técnico | H2 dedicado à diferença de apuração |
| Contraste direto 2 | Assemelhada a sorteio × assemelhada a vale-brinde | Distinção fina mas relevante para quem contrata |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template de query | Seção sugerida |
|---|---|---|
| Definição | O que é sorteio / o que é assemelhada a sorteio | H2 de abertura (dois blocos distintos) |
| Mecanismo | Como funciona o sorteio / como funciona a assemelhada | H2 explicativo com diagrama sugerido |
| Diferença principal | Diferença entre sorteio e assemelhada | H2 comparativo (tabela) |
| Base legal | Lei do sorteio / regulamentação da assemelhada | H2 regulatório com links SPA |
| Autorização | Como autorizar sorteio / como autorizar assemelhada | H3 dentro do regulatório |
| Qual escolher | Sorteio ou assemelhada — qual usar | H2 de decisão |
| Risco | O que acontece sem autorização | H2/H3 de risco |
| Elegibilidade | Quem pode fazer sorteio / assemelhada | H3 dentro de mecânica |

INTENÇÕES LATENTES:
| Intenção Latente | Gap se ausente | Seção sugerida |
|---|---|---|
| Quanto custa autorizar cada modalidade | Perde quem está avaliando orçamento | Mencionar processo, orientar contato com Mand |
| Quanto tempo leva a autorização | Intenção prática de planejamento | H3 prazo (120–40 dias antes) |
| Posso fazer sozinho ou preciso de especialista | Intenção de qualificação | Seção de CTA com a Mand Digital |
| Exemplos reais por setor | Prova social | H2 de exemplos (varejo, financeiro, alimentício) |
| Diferença para o consumidor final | Intenção do gestor que quer saber o impacto | Nota lateral na seção de mecânica |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS PRÁTICOS:
- Supermercado de capital do Sudeste usou sorteio vinculado à Loteria Federal para campanha de natal com 80 mil cupons emitidos.
- Rede de atacarejo no Sul utilizou assemelhada a sorteio com 3 séries de 100 mil números cada, distribuindo prêmios por cadastro de NF via hotsite.
- Cooperativa de crédito no interior de Minas usou assemelhada (raspadinha digital) ao cadastrar a contratação de consórcio.

CENÁRIOS DE APLICAÇÃO POR SEGMENTO:
- Varejo: campanhas de recebimento de NF → sorteio se até 100 mil participantes; assemelhada se campanhas nacionais.
- Financeiro: premiação por abertura de conta ou contratação de serviço → assemelhada é mais comum (escala digital).
- Alimentício: promoção em embalagem com acesso ao hotsite → assemelhada a vale-brinde ou sorteio conforme mecânica.

ERROS COMUNS:
1. Chamar de "sorteio" uma campanha com algoritmo próprio — modalidade errada na autorização resulta em negativa.
2. Usar Loteria Federal como referência em assemelhada — mistura modalidades e invalida o regulamento.
3. Não ter logs de auditoria independente na assemelhada — exigência da Portaria SEAE 7.638/2022.
4. Confundir assemelhada a sorteio com assemelhada a vale-brinde — mecânicas diferentes, processos de autorização distintos.

FRASES GEO-CITÁVEIS:
1. "O sorteio comercial exige que os ganhadores sejam apurados exclusivamente com base nos resultados da Loteria Federal, sem qualquer intervenção direta da empresa promotora."
2. "A promoção assemelhada a sorteio utiliza algoritmos de aleatoriedade técnica validados, dispensando a Loteria Federal mas exigindo auditoria independente dos logs do sistema."
3. "Ambas as modalidades — sorteio e assemelhada a sorteio — dependem de autorização prévia da Secretaria de Prêmios e Apostas (SPA) do Ministério da Fazenda antes do lançamento."
4. "O limite técnico que define a modalidade é 100 mil números por série: até esse limite, sorteio; acima disso, obrigatoriamente assemelhada."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Sorteio e assemelhada a sorteio são modalidades distintas dentro da distribuição gratuita de prêmios — a confusão entre elas é o erro mais comum de quem entra nesse mercado.

SÍNTESE DOS ATRIBUTOS PRINCIPAIS:
- Sorteio: Loteria Federal, 1 série até 100 mil, apuração externa.
- Assemelhada: algoritmo próprio validado, múltiplas séries, auditoria obrigatória.
- Ambas: autorização SPA obrigatória (120–40 dias antes), regulamento, responsabilidade do contratante.

CONEXÃO COM INTENÇÃO INICIAL: O leitor chegou querendo entender a diferença; sai sabendo qual modalidade se encaixa na escala e na mecânica da sua campanha.

DIREÇÃO PARA AÇÃO: Para não errar na escolha da modalidade e ter a autorização aprovada, a melhor decisão é trabalhar com quem já fez isso +450 vezes.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster REGULATÓRIO (alta prioridade):
autorização SPA, Secretaria de Prêmios e Apostas, Lei 5768, Decreto 70951, Portaria SEAE 7638, promoção comercial regulamentada, distribuição gratuita de prêmios, regulamento de promoção, SCPC

Cluster MECÂNICO (alta prioridade):
Loteria Federal, série de números, elemento sorteável, número da sorte, algoritmo de aleatoriedade, logs de auditoria, apuração de ganhadores, sistema informatizado

Cluster MODALIDADES (média prioridade):
vale-brinde, concurso comercial, assemelhada a vale-brinde, operação assemelhada, raspadinha digital, cartela digital, sorteio composto, sorteio simples

Cluster EXECUÇÃO/NEGÓCIO (média prioridade):
hotsite promocional, campanha regulamentada, prazo de autorização, regulamento de promoção, responsabilidade do promotor, fornecedor de promoção, estrutura técnica de campanha

Cluster RISCO/CONFORMIDADE (alta prioridade):
promoção irregular, ausência de autorização, penalidade SPA, campanha não regulamentada, infração promoção comercial

## POWER KEYWORDS APLICÁVEIS

H1/título: diferença, entenda, simples, escolha certa, sem erro
H2 regulatório: autorização obrigatória, antes do lançamento, penalidade, risco
H2 diferenciação: sorteio vs assemelhada, qual é qual, como distinguir
H2 mecanismo: como funciona na prática, passo a passo, Loteria Federal, algoritmo
Seção de intenção latente: quanto tempo leva, quanto custa, como fazer, especialista
CTA/fechamento: +450 campanhas, especialista, sem burocracia, fale agora

## ESTRUTURA DE OUTLINE SUGERIDA

H1: Diferença entre sorteio e promoção assemelhada: entenda de forma simples
[Lead GEO — 2–3 frases: nomear ambas as entidades + problema da confusão + consequência prática]
H2: O que é sorteio comercial (e como funciona a apuração)
  H3: O papel da Loteria Federal no sorteio
  H3: Limite de 100 mil números por série
H2: O que é promoção assemelhada a sorteio
  H3: Como funciona o algoritmo de aleatoriedade técnica
  H3: Por que não depende da Loteria Federal
  H3: Auditoria independente: por que é obrigatória
H2: Sorteio vs assemelhada: comparativo direto [tabela]
  H3: Quando usar sorteio
  H3: Quando usar assemelhada a sorteio
H2: Base legal e autorização (para as duas modalidades)
  H3: Lei 5.768/1971, Decreto 70.951/1972 e Portaria SEAE 7.638/2022 [links]
  H3: SPA — quem autoriza e como pedir [link oficial]
  H3: Prazo de 120 a 40 dias: o que acontece se perder
H2: Exemplos reais por setor (varejo, financeiro, alimentício)
H2: Erros que invalidam a autorização
H2: Como a Mand Digital estrutura sorteios e assemelhadas [CTA]
FAQ (mínimo 5 perguntas sobre diferença, autorização, prazo, risco, exemplos)

## RESTRIÇÕES E DIRETRIZES EDITORIAIS

SEMPRE fazer:
- Nomear SPA (Secretaria de Prêmios e Apostas) com link oficial em toda menção ao órgão regulador
- Citar Lei 5.768/1971 e Portaria SEAE 7.638/2022 com links do Planalto/NormasLegais
- Explicar o critério técnico de 100 mil números como divisor de modalidade
- Incluir o aviso legal da Mand Digital ao mencionar responsabilidades da campanha
- Usar tom direto e sem jargão corporativo (estilo Mand Digital)

NUNCA fazer:
- Chamar assemelhada de "sorteio digital" sem qualificação — são modalidades diferentes
- Dizer que a empresa pode fazer o sorteio sem Loteria Federal (isso é assemelhada)
- Omitir que ambas exigem autorização prévia obrigatória
- Usar frases genéricas como "plataforma robusta" ou "solução completa e integrada"
- Afirmar que a Mand Digital é responsável legal pela campanha (ela não é)

Aviso legal obrigatório: "{AVISO_LEGAL}"

## SEÇÃO DE CTA

URL do silo: https://manddigital.com.br/promocao-comercial-sorteio
Posição: H2 final, antes do FAQ
Título da seção: "Sorteio ou assemelhada? A Mand Digital resolve os dois sem dor de cabeça"
Conteúdo: especialização exclusiva em campanhas regulamentadas, +450 campanhas entregues, 30 dias de execução, dashboard em tempo real, leitura automática de QR Code/NF
Frase de fechamento: "A Mand não é agência generalista — é especialista em promoção regulamentada. E isso faz toda a diferença na hora da autorização."
CTA final: [Fale com nosso time](https://manddigital.com.br/promocao-comercial-sorteio)
Tom: direto, irreverente, sem frescura
Aviso legal: "{AVISO_LEGAL}"
"""

B3_LSI = """\
Cluster REGULATÓRIO (alta): autorização SPA, Secretaria de Prêmios e Apostas, Lei 5768/1971, Decreto 70951/1972, Portaria SEAE 7638/2022, promoção comercial regulamentada, distribuição gratuita de prêmios, SCPC
Cluster MECÂNICO (alta): Loteria Federal, série de números, elemento sorteável, algoritmo de aleatoriedade, logs de auditoria, apuração de ganhadores, sistema informatizado, número da sorte
Cluster MODALIDADES (média): vale-brinde, concurso comercial, assemelhada a vale-brinde, operação assemelhada, raspadinha digital, cartela digital
Cluster EXECUÇÃO (média): hotsite promocional, campanha regulamentada, prazo autorização, regulamento promoção, estrutura técnica campanha
Cluster RISCO (alta): promoção irregular, ausência autorização, penalidade SPA, campanha não regulamentada"""

# ─────────────────────────────────────────────────────────────────────────────

B4_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** assemelhada a sorteio exemplos
**Tipo de artigo:** Informacional com exemplos práticos
**Funil:** Topo/Meio (leitor já conhece o conceito, quer ver aplicações reais para decidir se essa modalidade serve para seu negócio)
**Objetivo estratégico:** Ilustrar casos reais de assemelhada a sorteio e converter gestores que buscam referência de execução.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Promoção assemelhada a sorteio é a modalidade de distribuição gratuita de prêmios que utiliza sistema informatizado com algoritmo de aleatoriedade técnica para apurar ganhadores — sem dependência dos resultados da Loteria Federal. Permite múltiplas séries simultâneas (acima de 100 mil números), exige validação técnica do algoritmo e auditoria independente dos logs.

ESCOPO DELIMITADO:
É assemelhada a sorteio: raspadinha digital com algoritmo próprio, distribuição de prêmio a cada N cadastros válidos, campanha digital massiva com múltiplas séries.
Não é assemelhada a sorteio: vale-brinde (premiação no envoltório físico), concurso (critério de habilidade), sorteio (vinculado à Loteria Federal).

DIRETRIZES:
- H1: nomear a entidade com o contexto de "exemplos" — leitor quer ver na prática.
  Ex.: "Assemelhada a sorteio: 5 exemplos reais e como aplicar na sua campanha"
- Primeiro parágrafo: contextualizar que assemelhada é a modalidade preferida para campanhas digitais de escala.

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Algoritmo de aleatoriedade técnica | Mecanismo central | Alta — como funciona a definição do ganhador |
| SPA (Secretaria de Prêmios e Apostas) | Regulador | Alta — link oficial obrigatório |
| Hotsite promocional | Contexto técnico de execução | Alta — onde a campanha ocorre |
| Cadastro de nota fiscal | Mecânica de participação | Alta — entrada mais comum no Brasil |
| Prova de posse de prêmios | Atributo regulatório | Alta — exigência: 8 dias antes da apuração |
| Raspadinha digital | Co-hipônimo (modalidade prática) | Alta — exemplo mais reconhecível |
| Cartela digital / roleta | Co-hipônimo (gamificação) | Média |
| Log de auditoria independente | Requisito técnico | Média |
| Múltiplas séries de 100 mil | Atributo definidor | Média |
| Regulamento de promoção | Contexto institucional | Média |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Assemelhada a Sorteio
├── Finalidade → Distribuir prêmios de forma escalável em ambiente digital
├── Apuração → Algoritmo de aleatoriedade técnica validado (sem Loteria Federal)
├── Escala → Múltiplas séries simultâneas, ilimitado em número de participantes
├── Autorização → SPA/Ministério da Fazenda obrigatória (120–40 dias antes)
├── Prova de prêmios → Exigida até 8 dias antes de cada data de apuração
├── Auditoria → Logs independentes obrigatórios; resultado auditável
├── Mecânicas comuns → Raspadinha digital, cartela, roleta, caixa premiada, prêmio a cada X cadastros
├── Canal de participação → Hotsite no domínio do cliente, cadastro de NF via QR Code
├── Base legal → Lei 5.768/1971, Decreto 70.951/1972, Portaria SEAE 7.638/2022
├── Segmentos usuários → Varejo (supermercados, atacarejo), financeiro, alimentício, energia
├── Dashboard → Métricas em tempo real: idade, localização, ticket médio, NF por usuário
└── Responsabilidade legal → Integralmente do contratante

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar no artigo |
|---|---|---|
| Hiperônimo | Operação assemelhada / Promoção comercial regulamentada | "Assemelhada a sorteio é uma operação assemelhada..." |
| Co-hipônimos | Sorteio, vale-brinde, concurso, assemelhada a vale-brinde | Seção de comparação: quando cada modalidade é indicada |
| Análogo popular | Sorteio digital | Corrigir: tecnicamente é assemelhada, não sorteio |
| Contraste direto | Sorteio (Loteria Federal) | Diferença de apuração: externo × interno |
| Contraste direto 2 | Assemelhada a vale-brinde | Assemelhada a sorteio tem data de apuração; vale-brinde é instantâneo |
| Hipônimos práticos | Raspadinha digital, cartela digital, caixa premiada | Cada um é uma implementação específica da assemelhada |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção sugerida |
|---|---|---|
| Exemplos concretos | Exemplos de assemelhada a sorteio | H2 com pelo menos 4 exemplos por segmento |
| Definição de suporte | O que é assemelhada a sorteio | H2 de abertura (breve — leitor já sabe) |
| Mecânica | Como funciona assemelhada a sorteio | H2 com diagrama de participação |
| Diferença modalidades | Assemelhada vs sorteio vs vale-brinde | H2 comparativo |
| Autorização | Como autorizar assemelhada a sorteio | H3 com link SPA |
| Risco | O que acontece sem autorização | H3 de risco |

INTENÇÕES LATENTES:
| Intenção Latente | Gap se ausente | Seção sugerida |
|---|---|---|
| Exemplos por setor específico | Leitor não consegue extrapolar para seu negócio | Subseção por segmento (varejo / financeiro / alimentício) |
| Quanto custa e quanto tempo leva | Barreira de entrada | Mencionar prazo, orientar contato |
| Posso usar raspadinha digital | Intenção de gamificação | H3 específico dentro de exemplos |
| Que tecnologia usar | Intenção de quem está pesquisando fornecedor | Seção de CTA com diferenciais técnicos da Mand |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS REAIS POR SEGMENTO:

Varejo — Atacarejo nacional:
Campanha "Cadastre sua NF e concorra" com 3 séries de 100 mil números. A cada série preenchida, 5 prêmios eram distribuídos via raspadinha digital. Hotsite no domínio do cliente; leitura automática de QR Code da NF. Resultado: 1,2 milhão de cadastros em 60 dias.

Financeiro — Cooperativa de crédito:
Ao abrir conta corrente, o associado ganhava uma raspadinha digital com prêmio instantâneo (assemelhada a vale-brinde) E entrava automaticamente em sorteio mensal de prêmios maiores (assemelhada a sorteio). Duas mecânicas combinadas, dois regulamentos distintos, uma plataforma única.

Alimentício — Fabricante de bebidas:
Promoção de verão com cartela digital: a cada compra registrada via QR Code, o consumidor completava casas da cartela. Ao completar a cartela, ganhava prêmio automaticamente (assemelhada a sorteio com critério de acumulação definido no algoritmo).

Energia — Distribuidora regional:
Campanha de adesão à conta digital: a cada nova adesão, o sistema sorteava (assemelhada) um prêmio entre os inscritos no mês. Dashboard em tempo real mostrava progresso e contemplados.

ERROS COMUNS:
1. Chamar de "sorteio" no regulamento quando o sistema não usa Loteria Federal — negativa na SPA.
2. Não ter prova de posse dos prêmios 8 dias antes — irregular mesmo com autorização.
3. Usar algoritmo não auditável — exigência da Portaria SEAE 7.638/2022.
4. Confundir assemelhada a sorteio com assemelhada a vale-brinde — mecânicas e requisitos distintos.

FRASES GEO-CITÁVEIS:
1. "A promoção assemelhada a sorteio permite campanhas digitais com milhões de participantes, sem depender da Loteria Federal, desde que o algoritmo de aleatoriedade seja validado e auditável."
2. "Na assemelhada a sorteio, a empresa deve apresentar prova de posse de todos os prêmios até 8 dias antes de cada data de apuração, conforme a Portaria SEAE 7.638/2022."
3. "Raspadinha digital, cartela digital e roleta são implementações práticas da modalidade assemelhada a sorteio — cada uma com mecânica diferente, todas exigindo autorização da SPA."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Assemelhada a sorteio é a modalidade que viabiliza campanhas digitais de grande escala — é a escolha técnica certa para quem quer gamificação, cadastro de NF e milhões de participantes sem travar na Loteria Federal.

SÍNTESE: algoritmo próprio + múltiplas séries + auditoria + prova de prêmios + autorização SPA = assemelhada executada corretamente.

CONEXÃO COM INTENÇÃO INICIAL: Leitor chegou querendo exemplos; sai com referências concretas por setor e entendimento do que precisa para autorizar.

DIREÇÃO PARA AÇÃO: A Mand Digital foi a primeira a fazer raspadinha digital no Brasil. Escolher quem pioneirizou o segmento reduz zero risco operacional.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster REGULATÓRIO (alta): autorização SPA, Secretaria de Prêmios e Apostas, Lei 5768, Portaria SEAE 7638, SCPC, promoção comercial regulamentada, regulamento de promoção
Cluster MECÂNICO (alta): algoritmo aleatoriedade, raspadinha digital, cartela digital, roleta premiada, caixa premiada, prêmio a cada X cadastros, log de auditoria, múltiplas séries
Cluster PARTICIPAÇÃO (média): cadastro nota fiscal, QR Code NF, hotsite promocional, domínio do cliente, dashboard tempo real, leitura automática NF
Cluster SEGMENTOS (média): campanha varejo, promoção supermercado, campanha financeiro, promoção atacarejo, campanha alimentícia
Cluster COMPARATIVO (alta): diferença sorteio assemelhada, quando usar assemelhada, sorteio vs assemelhada, vale-brinde vs assemelhada

## POWER KEYWORDS APLICÁVEIS

H1/título: exemplos reais, na prática, como aplicar, segmento, escolha certa
H2 regulatório: autorização obrigatória, prazo, como pedir, SPA
H2 exemplos: varejo, financeiro, alimentício, caso real, campanha que funcionou
H2 mecânica: como funciona, algoritmo, raspadinha, cartela, passo a passo
Seção latente: quanto custa, quanto tempo, fornecedor, quem faz
CTA: pioneiro, +450 campanhas, sem burocracia

## ESTRUTURA DE OUTLINE SUGERIDA

H1: Assemelhada a sorteio: 5 exemplos reais e como aplicar na sua campanha
[Lead GEO]
H2: O que é promoção assemelhada a sorteio (resumo rápido)
H2: Como funciona na prática
  H3: O papel do algoritmo de aleatoriedade
  H3: Raspadinha digital, cartela e roleta como implementações
  H3: Prova de prêmios e auditoria obrigatória
H2: 5 exemplos reais de assemelhada a sorteio
  H3: Varejo / atacarejo
  H3: Financeiro / cooperativa de crédito
  H3: Alimentício / bebidas
  H3: Energia / distribuidora
  H3: Redes sociais + hotsite
H2: Assemelhada x sorteio x vale-brinde: comparativo
H2: Como autorizar: SPA, prazos, documentação [links oficiais]
  H3: Lei 5.768/1971 e Portaria SEAE 7.638/2022
  H3: O que acontece sem autorização
H2: A Mand Digital e a assemelhada a sorteio [CTA]
FAQ (5 perguntas)

## RESTRIÇÕES E DIRETRIZES EDITORIAIS

SEMPRE fazer:
- Nomear SPA com link oficial em toda menção ao órgão
- Citar Lei 5.768/1971, Portaria SEAE 7.638/2022 com links
- Incluir exemplos concretos por setor (varejo, financeiro, alimentício, energia)
- Mencionar a exigência de prova de prêmios (8 dias antes)
- Mencionar auditoria de logs como requisito técnico

NUNCA fazer:
- Usar "sorteio" e "assemelhada" como sinônimos
- Afirmar que não precisa de autorização em nenhum caso
- Inventar exemplos sem correspondência real
- Atribuir responsabilidade legal à Mand Digital

Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/assemelhada-a-vale-brinde
Título: "Precisa de assemelhada a sorteio? Vem falar com quem fez a primeira raspadinha digital do Brasil."
CTA: [Ver como funciona](https://manddigital.com.br/assemelhada-a-vale-brinde)
Tom: direto, pioneiro, sem frescura
Aviso legal: "{AVISO_LEGAL}"
"""

B4_LSI = """\
Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, Lei 5768, Portaria SEAE 7638, SCPC, regulamento promoção comercial
Cluster MECÂNICO (alta): algoritmo aleatoriedade, raspadinha digital, cartela digital, roleta, caixa premiada, log auditoria, múltiplas séries 100 mil
Cluster PARTICIPAÇÃO (média): cadastro NF, QR Code nota fiscal, hotsite promocional, domínio cliente, dashboard tempo real
Cluster SEGMENTOS (média): campanha varejo, promoção supermercado, campanha financeiro, promoção alimentícia, cooperativa crédito
Cluster COMPARATIVO (alta): diferença sorteio assemelhada, quando usar assemelhada, sorteio vs assemelhada"""

# ─────────────────────────────────────────────────────────────────────────────

B5_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** o que é vale-brinde
**Tipo de artigo:** Informacional puro (definição + mecanismo)
**Funil:** Topo (busca definitória — leitor quer entender o conceito antes de avaliar a modalidade)
**Objetivo estratégico:** Ser a referência definitória de vale-brinde e converter quem está avaliando a modalidade para sua campanha.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE (fonte: SPA/Ministério da Fazenda):
Vale-brinde é a modalidade de promoção comercial regulamentada em que a contemplação é instantânea: o brinde é colocado no interior do produto ou dentro do respectivo envoltório — ou, quando isso for impraticável, em elemento identificador trocável em postos de resgate. É a única modalidade em que TODOS os participantes que cumprirem os requisitos recebem o prêmio. A quantidade de prêmios é fixa, limitada ao estoque definido na autorização, e o valor máximo por prêmio é R$ 703,00 (Portaria SEAE 7.638/2022).

ESCOPO DELIMITADO:
É vale-brinde: prêmio instantâneo, quantidade fixa, sem sorteio, todos os aptos ganham.
Não é vale-brinde: sorteio (data futura, Loteria Federal), concurso (habilidade), assemelhada (algoritmo técnico), "compre e ganhe" não regulamentado (sem autorização SPA).

DIRETRIZES:
- H1: nomear entidade + delimitar escopo ("prêmio instantâneo")
  Ex.: "O que é vale-brinde: o prêmio que todos ganham — e como funciona de verdade"
- Primeiro parágrafo: definir + diferencial (todos ganham, não há sorte)

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Contemplação instantânea | Atributo definidor | Alta — é o que diferencia do sorteio |
| SPA / Ministério da Fazenda | Regulador | Alta — link oficial obrigatório |
| Envoltório do produto | Mecanismo central (físico) | Alta — como o brinde chega ao participante |
| Elemento identificador | Mecanismo alternativo (digital) | Alta — quando envoltório não é viável |
| Posto de troca | Contexto de execução | Média |
| Estoque fixo de prêmios | Atributo definidor | Alta — quantidade fechada na autorização |
| Valor máximo R$ 703 | Atributo regulatório | Alta — limite legal vigente |
| Autorização SPA | Requisito legal | Alta |
| Lei 5.768/1971 | Base legal | Alta — link obrigatório |
| Assemelhada a vale-brinde | Co-hipônimo digital | Média — quando a mecânica vai para o hotsite |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Vale-brinde
├── Finalidade → Distribuir prêmios garantidos a todos os participantes aptos (foco em conversão)
├── Mecânica de contemplação → Instantânea (no ato da abertura do produto ou do cadastro)
├── Suporte físico → Brinde no interior do produto / envoltório
├── Suporte digital → Elemento identificador → troca em posto físico ou hotsite (assemelhada a vale-brinde)
├── Estoque → Fixo e declarado na autorização — quando esgota, campanha encerra
├── Valor máximo do prêmio → R$ 703,00 (Portaria SEAE 7.638/2022)
├── Elegibilidade → Apenas PJ regularmente constituída pode promover
├── Autorização → SPA/Ministério da Fazenda (pedido 120–40 dias antes)
├── Base legal → Lei 5.768/1971 + Decreto 70.951/1972 + Portaria SEAE 7.638/2022
├── Restrição de conversão → Proibido converter prêmio em dinheiro
├── Segmentos usuários → Varejo alimentício, indústria de bens de consumo, financeiro
└── Responsabilidade legal → Integralmente do contratante

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar no artigo |
|---|---|---|
| Hiperônimo | Distribuição gratuita de prêmios / Promoção comercial regulamentada | "Vale-brinde é uma das modalidades de distribuição gratuita de prêmios" |
| Co-hipônimos | Sorteio, concurso, assemelhada a sorteio | Seção comparativa: o que diferencia cada um |
| Análogo popular | "Compre e ganhe" | Nota: nem todo "compre e ganhe" é vale-brinde regulamentado |
| Hipônimo digital | Assemelhada a vale-brinde | Quando a mecânica vai para hotsite/QR Code |
| Contraste direto | Sorteio | Vale-brinde = todos ganham (estoque fixo); sorteio = poucos ganham (sorte) |
| Contraste direto 2 | Promoção não regulamentada | Risco legal de campanha sem autorização SPA |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Definição | O que é vale-brinde | H2 de abertura |
| Mecanismo | Como funciona o vale-brinde | H2 explicativo |
| Diferença | Vale-brinde vs sorteio | H2 comparativo |
| Base legal | Lei do vale-brinde | H2 regulatório com links |
| Autorização | Como autorizar vale-brinde | H3 dentro do regulatório |
| Elegibilidade | Quem pode fazer vale-brinde | H3 dentro de mecanismo |

INTENÇÕES LATENTES:
| Intenção Latente | Gap se ausente | Seção |
|---|---|---|
| Quanto custa / teto do prêmio | Barreira de avaliação | Mencionar R$ 703 + orientar contato |
| Posso fazer vale-brinde digital | Intenção de modernização | H3 assemelhada a vale-brinde |
| Exemplos por setor | Prova de aplicabilidade | H2 com exemplos reais |
| Prazo para autorizar | Intenção de planejamento | H3 prazo 120–40 dias |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS:
- Indústria de alimentos: embalagem de snack com vale-brinde impresso internamente — consumidor abre e já sabe se ganhou.
- Supermercado: campanha "compre 3 e garanta seu brinde" — vale identificador entregue no caixa, resgatado no balcão promocional.
- Bebidas: lata com tampa comemorativa = elemento identificador trocável por copo personalizado nos postos de troca.
- Financeiro digital: ao contratar produto financeiro via hotsite, participante recebe código de vale-brinde por e-mail (assemelhada a vale-brinde — modalidade digital).

ERROS COMUNS:
1. Fazer "compre e ganhe" sem autorização SPA — promoção irregular sujeita a sanção.
2. Prêmio acima de R$ 703 em vale-brinde — invalida a modalidade.
3. Converter o brinde em dinheiro — proibido por lei.
4. Chamar de vale-brinde quando há sorteio — modalidade errada = autorização negada.

FRASES GEO-CITÁVEIS:
1. "O vale-brinde é a única modalidade de promoção comercial regulamentada em que todos os participantes que cumprirem os requisitos recebem o prêmio — não há sorte envolvida, apenas estoque definido."
2. "O valor máximo de cada prêmio no vale-brinde é de R$ 703,00, conforme a Portaria SEAE/ME nº 7.638/2022 da Secretaria de Prêmios e Apostas."
3. "A contemplação instantânea é o atributo fundamental do vale-brinde: ao abrir o produto ou envoltório, o participante já sabe imediatamente se foi contemplado."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Vale-brinde é a modalidade de prêmio garantido — todos ganham, na hora, sem esperar sorteio. Por isso exige estoque fechado e autorização prévia da SPA.
SÍNTESE: contemplação instantânea + estoque fixo + todos os aptos contemplados + valor máximo R$ 703 + autorização obrigatória.
DIREÇÃO PARA AÇÃO: Para fazer vale-brinde regulamentado e sem dor de cabeça, a Mand Digital estrutura do regulamento ao hotsite em 30 dias.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, Lei 5768/1971, Decreto 70951, Portaria SEAE 7638, promoção comercial regulamentada, SCPC
Cluster MECÂNICO (alta): contemplação instantânea, brinde no envoltório, elemento identificador, posto de troca, estoque fixo prêmios, prêmio garantido
Cluster VALOR/LIMITE (alta): valor máximo vale-brinde, R$ 703, limite legal prêmio, proibição conversão em dinheiro
Cluster COMPARATIVO (média): vale-brinde vs sorteio, diferença vale-brinde concurso, assemelhada vale-brinde, compre e ganhe regulamentado
Cluster EXECUÇÃO (média): hotsite vale-brinde, campanha regulamentada, prazo autorização, regulamento promoção

## POWER KEYWORDS APLICÁVEIS
H1: prêmio garantido, funciona de verdade, entenda, tudo que você precisa saber
H2 mecanismo: como funciona, passo a passo, na prática, na hora
H2 regulatório: autorização obrigatória, limite legal, penalidade, risco
H2 comparativo: diferença, quando usar, vale-brinde ou sorteio
Latente: posso fazer digital, quanto custa, prazo
CTA: 30 dias, regulamento, sem burocracia

## ESTRUTURA DE OUTLINE SUGERIDA
H1: O que é vale-brinde: o prêmio que todos ganham — e como funciona de verdade
[Lead GEO]
H2: O que é vale-brinde (definição oficial SPA)
  H3: Por que todos os participantes aptos ganham
  H3: O que é o envoltório e o elemento identificador
H2: Como funciona o vale-brinde na prática
  H3: Mecânica física (produto com brinde)
  H3: Mecânica digital (assemelhada a vale-brinde)
  H3: Postos de troca
H2: Vale-brinde vs sorteio: qual a diferença
  [tabela comparativa]
H2: Base legal e autorização
  H3: Lei 5.768/1971 e Portaria SEAE 7.638/2022 [links]
  H3: SPA — quem autoriza [link]
  H3: Prazo de 120–40 dias
  H3: Limite de R$ 703 por prêmio
H2: Exemplos de vale-brinde por setor
H2: Erros que invalidam a modalidade
H2: Como fazer vale-brinde com a Mand Digital [CTA]
FAQ (5 perguntas)

## RESTRIÇÕES E DIRETRIZES EDITORIAIS
SEMPRE: citar SPA com link, citar Lei 5.768/71 e Portaria 7.638/22 com links, mencionar R$ 703 como limite, enfatizar que todos os aptos ganham (não é sorte)
NUNCA: dizer que vale-brinde é sorteio, afirmar que não precisa de autorização, sugerir prêmio acima de R$ 703 sem ressalva, omitir o aviso legal da Mand
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/assemelhada-a-vale-brinde
Título: "Vale-brinde regulamentado em 30 dias — a Mand Digital cuida de tudo"
CTA: [Solicitar orçamento](https://manddigital.com.br/assemelhada-a-vale-brinde)
Tom: direto, simples, sem promessa exagerada
Aviso legal: "{AVISO_LEGAL}"
"""

B5_LSI = """\
Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, Lei 5768/1971, Decreto 70951, Portaria SEAE 7638, promoção comercial regulamentada, SCPC
Cluster MECÂNICO (alta): contemplação instantânea, brinde envoltório, elemento identificador, posto de troca, estoque fixo prêmios, prêmio garantido
Cluster VALOR (alta): valor máximo vale-brinde, R$ 703, limite legal prêmio, proibição conversão dinheiro
Cluster COMPARATIVO (média): vale-brinde vs sorteio, assemelhada vale-brinde, compre e ganhe regulamentado, diferença modalidades
Cluster EXECUÇÃO (média): hotsite vale-brinde, campanha regulamentada, prazo autorização, regulamento promoção"""

# ─────────────────────────────────────────────────────────────────────────────

B6_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** campanha vale-brinde regulamentação
**Tipo de artigo:** Guia prático / Informacional de meio de funil
**Funil:** Meio (leitor já sabe o que é vale-brinde, quer saber como regularizar e executar)
**Objetivo estratégico:** Educar sobre o processo de autorização e converter gestores que precisam de parceiro técnico.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Regulamentação de campanha vale-brinde é o conjunto de obrigações legais e procedimentos administrativos que uma empresa deve cumprir para lançar uma promoção na modalidade vale-brinde no Brasil — incluindo pedido de autorização à SPA/Ministério da Fazenda, elaboração de regulamento, comprovação financeira dos prêmios e observância das restrições de valor e mecânica.

ESCOPO DELIMITADO:
Está dentro do escopo: pedido de autorização SPA, prazo, documentos necessários, regulamento, limite de prêmio, responsabilidades do promotor.
Está fora do escopo: execução criativa (peças, design), gestão de tráfego, produção de conteúdo para redes sociais.

DIRETRIZES:
- H1: nomear entidade + deixar claro que é guia prático de como fazer.
  Ex.: "Campanha vale-brinde: regras, regulamentação e como fazer legalmente"
- Primeiro parágrafo: problema real — muitas empresas lançam campanha "compre e ganhe" sem saber que precisa de autorização prévia da SPA.

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| SPA — Secretaria de Prêmios e Apostas | Regulador | Alta — link obrigatório |
| SCPC | Sistema de controle / canal de pedido | Alta — onde se protocola |
| Lei 5.768/1971 | Base legal primária | Alta — link obrigatório |
| Decreto 70.951/1972 | Base legal regulamentadora | Alta — link obrigatório |
| Portaria SEAE 7.638/2022 | Norma procedimental vigente | Alta — link obrigatório |
| Regulamento de promoção | Documento obrigatório | Alta — como elaborar |
| Prazo de autorização | Atributo procedimental | Alta — 120–40 dias antes |
| Valor máximo R$ 703 | Limite legal do prêmio | Alta |
| Pessoa jurídica | Elegibilidade | Média — apenas PJ ativa pode promover |
| Responsabilidade do contratante | Aviso legal | Alta |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Campanha Vale-Brinde (processo de regulamentação)
├── Órgão competente → SPA / Ministério da Fazenda
├── Canal de pedido → SCPC (Sistema de Controle de Promoção Comercial)
├── Prazo do pedido → Entre 120 e 40 dias antes do início da promoção
├── Documentos necessários → Regulamento elaborado, comprovação financeira dos prêmios, CNPJ ativo, quitação fiscal
├── Limite de prêmio → R$ 703,00 por prêmio (individual)
├── Restrição de conversão → Prêmio não pode ser convertido em dinheiro
├── Responsabilidade → Inteiramente do contratante; empresa técnica elabora estrutura, não responde pela campanha
├── Vigência → Definida no regulamento; encerra quando o estoque de prêmios se esgota
├── Base legal → Lei 5.768/1971 + Decreto 70.951/1972 + Portaria SEAE 7.638/2022
├── Risco sem autorização → Sanção administrativa, apreensão de material, cancelamento da campanha
└── Elegibilidade → Apenas PJ ativa, quites com obrigações fiscais federais, estaduais e municipais

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar |
|---|---|---|
| Hiperônimo | Promoção comercial regulamentada / Distribuição gratuita de prêmios | "Campanha vale-brinde é uma promoção comercial regulamentada pela Lei 5.768/71" |
| Co-hipônimos | Sorteio, concurso, assemelhada | Breve comparativo de quando cada um se aplica |
| Análogo | Compre e ganhe | Diferenciar: nem todo compre e ganhe é vale-brinde regulamentado |
| Contraste | Campanha não regulamentada | Risco legal de lançar sem autorização |
| Hipônimo digital | Assemelhada a vale-brinde | Quando a mecânica usa hotsite em vez de envoltório |
| Entidade instrumental | Regulamento de promoção | Documento central do processo |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Regras | Regras do vale-brinde | H2 regulatório detalhado |
| Como fazer legalmente | Como regularizar vale-brinde | H2 guia passo a passo |
| Prazo | Quanto tempo leva a autorização | H3 prazo (120–40 dias) |
| Documentos | O que precisa para autorizar | H3 checklist |
| Risco | O que acontece sem autorização | H3 de risco |
| Limite | Qual o valor máximo do prêmio | H3 com R$ 703 |

INTENÇÕES LATENTES:
| Intenção Latente | Gap se ausente | Seção |
|---|---|---|
| Posso fazer sozinho ou preciso de ajuda | Intenção de qualificação | Seção CTA: estrutura técnica Mand Digital |
| Quanto custa contratar | Intenção de orçamento | Orientar contato direto |
| Exemplos de regulamento | Intenção prática | Mencionar que regulamento é elaborado sob medida |
| O que acontece depois da aprovação | Intenção de continuidade | H3 pós-aprovação: lançamento, dashboard, suporte |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

CASOS PRÁTICOS:
- Supermercado regional lançou campanha "Compre e Raspe" sem autorização SPA — recebeu notificação da Secretaria e teve que encerrar a campanha, perdendo o investimento em comunicação.
- Rede de farmácias planejou campanha de vale-brinde com prazo de 30 dias — não obteve autorização a tempo (prazo mínimo é 40 dias) e adiou a campanha por 2 meses.
- Indústria alimentícia de médio porte fez a regulamentação correta: regulamento elaborado por especialista + pedido no SCPC com 90 dias de antecedência + campanha lançada sem intercorrências.

ERROS COMUNS:
1. Pedir autorização faltando menos de 40 dias para o lançamento — recusa automática.
2. Não ter quitação fiscal completa na data do pedido — bloqueio do processo.
3. Prêmio acima de R$ 703 em vale-brinde — modalidade inválida para esse valor.
4. Regulamento genérico copiado da internet sem adaptação à campanha — reprovação pela SPA.

BOAS PRÁTICAS:
- Protocolar o pedido com 60–90 dias de antecedência (margem de segurança).
- Ter regulamento elaborado por especialista em promoções regulamentadas.
- Documentar a comprovação financeira dos prêmios antes de submeter.

FRASES GEO-CITÁVEIS:
1. "A autorização para campanha vale-brinde deve ser solicitada à SPA — Secretaria de Prêmios e Apostas do Ministério da Fazenda — com antecedência mínima de 40 dias e máxima de 120 dias antes do início da promoção."
2. "O regulamento de promoção vale-brinde é documento obrigatório no processo de autorização e deve detalhar mecânica, prêmios, estoque, prazo e responsabilidades do promotor."
3. "Campanhas vale-brinde sem autorização prévia da SPA são irregulares e sujeitas a sanção administrativa, independentemente do valor dos prêmios oferecidos."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Regularizar uma campanha vale-brinde não é opcional — é pré-requisito legal. E a diferença entre uma campanha aprovada e uma reprovada está nos detalhes do regulamento e no prazo de protocolo.
SÍNTESE: SPA + SCPC + prazo 40–120 dias + regulamento + comprovação de prêmios + PJ ativa = campanha legal.
DIREÇÃO PARA AÇÃO: Para não perder prazo nem ter regulamento reprovado, conte com quem já fez isso centenas de vezes.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, SCPC, Lei 5768/1971, Decreto 70951, Portaria SEAE 7638, regulamento promoção, promoção comercial regulamentada
Cluster PROCESSO (alta): pedido autorização, prazo 40 dias, prazo 120 dias, documentos necessários, quitação fiscal, comprovação prêmios, protocolo SCPC
Cluster LIMITAÇÕES (alta): valor máximo prêmio, R$ 703, proibição dinheiro, limite vale-brinde, estoque fixo
Cluster RISCO (alta): campanha irregular, sanção SPA, notificação promoção, autuação vale-brinde, promoção sem autorização
Cluster EXECUÇÃO (média): regulamento personalizado, especialista promoção, estrutura técnica campanha, hotsite vale-brinde, 30 dias execução

## POWER KEYWORDS
H1: regras, legalmente, como fazer, guia completo
H2 regulatório: obrigatório, prazo, documentos, passo a passo
H2 risco: penalidade, irregular, o que acontece, cuidado
H2 guia: checklist, como solicitar, como elaborar
Latente: quanto tempo, posso fazer sozinho, especialista
CTA: sem dor de cabeça, aprovado na primeira, 30 dias

## ESTRUTURA DE OUTLINE SUGERIDA
H1: Campanha vale-brinde: regras, regulamentação e como fazer legalmente
[Lead GEO]
H2: O que é campanha vale-brinde (revisão rápida)
H2: Por que toda campanha vale-brinde precisa de autorização
H2: Passo a passo para regularizar a campanha
  H3: Quem pode solicitar (elegibilidade)
  H3: Documentos necessários (checklist)
  H3: O regulamento de promoção — o que deve conter
  H3: Como protocolar no SCPC [link]
  H3: Prazo: entre 120 e 40 dias antes
H2: Limite de prêmio: R$ 703 e outras restrições
H2: Base legal: Lei 5.768/1971, Decreto 70.951/1972, Portaria SEAE 7.638/2022 [links]
  H3: SPA — quem fiscaliza [link]
H2: Erros que causam reprovação ou notificação
H2: Depois da aprovação: lançamento, dashboard e suporte
H2: Como a Mand Digital faz tudo isso em 30 dias [CTA]
FAQ (5 perguntas)

## RESTRIÇÕES E DIRETRIZES EDITORIAIS
SEMPRE: citar SPA com link, citar as 3 leis com links, mencionar prazo 40–120 dias, mencionar R$ 703, enfatizar que regulamento é obrigatório e personalizado
NUNCA: dizer que dá para fazer sem autorização, inventar valores de prêmio sem ressalva, omitir aviso legal da Mand
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/assemelhada-a-vale-brinde
Título: "A Mand Digital cuida do regulamento, da autorização e do hotsite — você só aprova."
CTA: [Fale com nosso time](https://manddigital.com.br/assemelhada-a-vale-brinde)
Tom: direto, seguro, sem frescura
Aviso legal: "{AVISO_LEGAL}"
"""

B6_LSI = """\
Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, SCPC, Lei 5768/1971, Decreto 70951, Portaria SEAE 7638, regulamento promoção
Cluster PROCESSO (alta): pedido autorização, prazo 40 dias, prazo 120 dias, documentos necessários, quitação fiscal, comprovação prêmios
Cluster LIMITAÇÕES (alta): valor máximo prêmio, R$ 703, proibição dinheiro, estoque fixo
Cluster RISCO (alta): campanha irregular, sanção SPA, notificação promoção, autuação, promoção sem autorização
Cluster EXECUÇÃO (média): regulamento personalizado, especialista promoção, hotsite vale-brinde, 30 dias execução"""

# ─────────────────────────────────────────────────────────────────────────────

B7_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** diferença entre vale-brinde e sorteio
**Tipo de artigo:** Comparativo / Informacional
**Funil:** Topo/Meio (leitor está decidindo qual modalidade usar para sua campanha)
**Objetivo estratégico:** Ser a referência do comparativo entre as duas modalidades e converter quem está escolhendo qual estrutura contratar.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Vale-brinde e sorteio são duas modalidades distintas de promoção comercial regulamentada pela Lei 5.768/1971.
- Vale-brinde: contemplação instantânea, todos os participantes aptos ganham, estoque fixo de prêmios, sem sorte — é garantido para quem cumprir o critério.
- Sorteio: data futura, ganhador definido pelo resultado da Loteria Federal, apenas alguns ganham, aleatoriedade pura.

ESCOPO DELIMITADO:
Não é vale-brinde: promoção em que só alguns ganham (isso é sorteio ou assemelhada).
Não é sorteio: promoção em que todos os aptos ganham na hora (isso é vale-brinde).
Não confundir: assemelhada a vale-brinde (digital) e assemelhada a sorteio (algoritmo) são variantes técnicas das modalidades originais.

DIRETRIZES:
- H1: nomear ambas as entidades explicitamente + framing de decisão.
  Ex.: "Vale-brinde ou sorteio: qual a diferença e quando usar cada um"
- Primeiro parágrafo: contexto da escolha (gestor de marketing precisa escolher a modalidade antes de contratar a estrutura técnica).

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Contemplação instantânea | Atributo definidor do vale-brinde | Alta |
| Loteria Federal | Mecanismo do sorteio | Alta |
| SPA | Regulador de ambas | Alta — link obrigatório |
| Estoque fixo | Atributo do vale-brinde | Alta |
| Número da sorte / série | Atributo do sorteio | Alta |
| Assemelhada a vale-brinde | Co-hipônimo digital | Média |
| Assemelhada a sorteio | Co-hipônimo digital | Média |
| Prazo de autorização | Atributo procedimental | Média |
| R$ 703 (limite vale-brinde) | Atributo regulatório | Alta |
| Regulamento de promoção | Contexto institucional | Média |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Comparativo direto (árvore):
Modalidade → Vale-Brinde / Sorteio
├── Quando o participante sabe se ganhou → Na hora (vale-brinde) / Na data do sorteio (sorteio)
├── Quem ganha → Todos os aptos dentro do estoque (vale-brinde) / Apenas os sorteados (sorteio)
├── Mecanismo de apuração → Estoque pré-definido / Loteria Federal
├── Limite de participantes que ganham → Determinado pelo estoque / Determinado pelo número de prêmios sorteados
├── Valor máximo do prêmio → R$ 703 (vale-brinde) / Sem limite fixo por prêmio (sorteio — limitado por percentual da receita)
├── Engajamento gerado → Alto e imediato / Alto e prolongado (expectativa)
├── Conversão imediata → Alta (recompensa certa) / Média (expectativa futura)
├── Adequação por campanha → Produto de massa, conversão no PDV / Engajamento de base larga, prêmios de alto valor
├── Base legal → Lei 5.768/1971 + Portaria SEAE 7.638/2022 (ambas)
└── Órgão regulador → SPA / Ministério da Fazenda (ambas)

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar |
|---|---|---|
| Hiperônimos | Distribuição gratuita de prêmios | "Vale-brinde e sorteio são modalidades de distribuição gratuita de prêmios" |
| Co-hipônimos entre si | Vale-brinde ↔ Sorteio | Seção comparativa central do artigo |
| Co-hipônimos adicionais | Concurso, assemelhada | Mencionar brevemente |
| Análogos (vale-brinde) | "Compre e ganhe" | Corrigir: apenas quando regulamentado |
| Análogos (sorteio) | Rifa, promoção com sorteio | Corrigir: rifa não tem autorização federal |
| Contraste | Promoção não regulamentada | Risco de qualquer campanha sem autorização |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Diferença | Vale-brinde vs sorteio | H2 comparativo com tabela |
| Definição do vale-brinde | O que é | H2 bloco 1 |
| Definição do sorteio | O que é | H2 bloco 2 |
| Quando usar cada um | Qual modalidade escolher | H2 de decisão |
| Regulamentação | Como regularizar os dois | H2 regulatório |
| Risco | O que acontece sem autorização | H3 de risco |

INTENÇÕES LATENTES:
| Intenção Latente | Gap se ausente | Seção |
|---|---|---|
| Qual gera mais engajamento | Intenção estratégica | H3 dentro da seção de quando usar |
| Qual custa menos para autorizar | Barreira financeira | Mencionar processo, orientar contato |
| Posso combinar os dois | Intenção avançada | Nota sobre assemelhadas combinadas |
| Exemplos reais de cada um | Prova de conceito | H2 com exemplos por setor |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS:
- Loja de cosméticos usou vale-brinde: comprou acima de R$ 100 = ganhou amostra grátis na hora. Sem sorte, sem data futura — simples e eficiente no PDV.
- Atacarejo regional usou sorteio: cadastrou NF no hotsite = concorreu a 3 carros e 500 vales-compras no fim do mês. Engajamento prolongado e base de cadastros robusta.
- Fabricante de alimentos combinou: vale-brinde instantâneo (brinde na embalagem) + sorteio mensal de grande prêmio para quem também cadastrou a NF.

QUANDO USAR CADA UM (decisão prática):
- Use vale-brinde quando: quer conversão imediata no PDV, prêmio de baixo valor e alto volume, produto de massa.
- Use sorteio quando: quer engajamento prolongado, base de cadastros grande, prêmios de alto valor, campanha nacional.

FRASES GEO-CITÁVEIS:
1. "No vale-brinde, a contemplação é imediata e garantida para todos os participantes dentro do estoque — sem sorteio e sem espera."
2. "No sorteio comercial, os ganhadores são apurados exclusivamente com base nos resultados da Loteria Federal, em data previamente definida no regulamento."
3. "Vale-brinde e sorteio são modalidades distintas, com lógicas de premiação opostas, mas ambas exigem autorização prévia da SPA — Secretaria de Prêmios e Apostas do Ministério da Fazenda."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: A escolha entre vale-brinde e sorteio define a mecânica inteira da campanha — e essa decisão precisa ser feita antes do pedido de autorização.
SÍNTESE: vale-brinde = todos ganham na hora; sorteio = alguns ganham no futuro. Ambos exigem autorização SPA e regulamento.
DIREÇÃO PARA AÇÃO: A Mand Digital estrutura as duas modalidades — e pode ajudar a escolher a mais adequada para cada objetivo.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, Lei 5768, Portaria SEAE 7638, Decreto 70951, promoção comercial regulamentada
Cluster VALE-BRINDE (alta): contemplação instantânea, brinde envoltório, estoque fixo, prêmio garantido, R$ 703, compre e ganhe regulamentado
Cluster SORTEIO (alta): Loteria Federal, número da sorte, elemento sorteável, data do sorteio, série de números
Cluster COMPARATIVO (alta): vale-brinde vs sorteio, diferença contemplação, quando usar sorteio, quando usar vale-brinde, qual escolher
Cluster EXECUÇÃO (média): hotsite promocional, regulamento promoção, assemelhada, campanha regulamentada, 30 dias execução

## POWER KEYWORDS
H1: diferença, quando usar, qual a escolha certa, entenda
H2 comparativo: tabela, lado a lado, qual é melhor, depende do objetivo
H2 regulatório: ambos precisam, autorização obrigatória, antes do lançamento
Latente: qual gera mais resultado, qual é mais barato, posso combinar
CTA: especialista, escolha certa, Mand Digital

## ESTRUTURA DE OUTLINE SUGERIDA
H1: Vale-brinde ou sorteio: qual a diferença e quando usar cada um
[Lead GEO]
H2: O que é vale-brinde
H2: O que é sorteio comercial
H2: Vale-brinde vs sorteio: comparativo direto [tabela]
  H3: Forma de contemplação
  H3: Quem pode ganhar
  H3: Valor dos prêmios
  H3: Engajamento e conversão
H2: Quando usar vale-brinde
H2: Quando usar sorteio
H2: E se eu quiser combinar os dois?
H2: Regulamentação: o que é igual e o que muda [links SPA, leis]
H2: Exemplos reais por setor
H2: Como a Mand Digital estrutura as duas modalidades [CTA]
FAQ

## RESTRIÇÕES
SEMPRE: citar SPA com link, citar leis com links, tabela comparativa, mencionar que ambas precisam de autorização
NUNCA: dizer que uma é "melhor" que a outra sem contexto, omitir que ambas são regulamentadas
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/promocao-comercial-sorteio
Título: "Vale-brinde ou sorteio — a Mand Digital estrutura os dois, com regulamento e hotsite incluídos."
CTA: [Ver modalidades](https://manddigital.com.br/promocao-comercial-sorteio)
Aviso legal: "{AVISO_LEGAL}"
"""

B7_LSI = """\
Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, Lei 5768, Portaria SEAE 7638, Decreto 70951, promoção comercial regulamentada
Cluster VALE-BRINDE (alta): contemplação instantânea, brinde envoltório, estoque fixo, prêmio garantido, R$ 703, compre e ganhe regulamentado
Cluster SORTEIO (alta): Loteria Federal, número da sorte, elemento sorteável, data do sorteio, série de números
Cluster COMPARATIVO (alta): vale-brinde vs sorteio, diferença contemplação, quando usar cada modalidade, qual escolher
Cluster EXECUÇÃO (média): hotsite promocional, regulamento promoção, assemelhada, campanha regulamentada"""

# ─────────────────────────────────────────────────────────────────────────────

B8_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** vale-brinde como funciona
**Tipo de artigo:** Explicativo / Guia de mecanismo
**Funil:** Topo/Meio (leitor quer entender a mecânica antes de decidir se contrata)
**Objetivo estratégico:** Explicar a mecânica do vale-brinde com clareza e mostrar como a Mand Digital executa essa modalidade no ambiente digital.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Vale-brinde funciona a partir de um estoque fixo de prêmios distribuídos dentro do produto (físico) ou via elemento identificador trocável — e a contemplação é imediata: o participante descobre na hora se foi contemplado. No ambiente digital, a mecânica equivalente é a assemelhada a vale-brinde (raspadinha digital, cartela, roleta), onde o sistema substitui o envoltório físico e a contemplação ocorre no hotsite.

ESCOPO DELIMITADO:
Está no escopo: mecânica físicaa (brinde no produto), mecânica digital (assemelhada via hotsite), fluxo de participação, regras de estoque, prazo.
Está fora do escopo: criação de peças publicitárias, gestão de redes sociais, análise de ROI de campanha.

DIRETRIZES:
- H1: nomear entidade + palavras de mecanismo.
  Ex.: "Como funciona o vale-brinde: regras, mecânica e exemplos"
- Primeiro parágrafo: contexto — o vale-brinde é a modalidade mais simples de entender para o consumidor, mas tem regras técnicas que o gestor precisa conhecer.

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Brinde no envoltório / interior do produto | Mecanismo central (físico) | Alta |
| Elemento identificador | Mecanismo alternativo | Alta |
| Posto de troca | Contexto de resgate | Média |
| Estoque fixo de prêmios | Atributo definidor | Alta |
| Raspadinha digital | Co-hipônimo digital | Alta — implementação mais comum no hotsite |
| Cartela digital | Co-hipônimo digital | Média |
| QR Code / código de barras NF | Tecnologia de participação | Alta — diferencial Mand Digital |
| SPA | Regulador | Alta — link obrigatório |
| Regulamento de promoção | Contexto institucional | Média |
| Dashboard em tempo real | Diferencial tecnológico | Média |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Vale-brinde (mecanismo)
├── Modalidade física → Brinde inserido na embalagem do produto antes da distribuição
├── Modalidade com elemento identificador → Símbolo/dizeres na embalagem trocável em posto físico
├── Modalidade digital (assemelhada) → Hotsite com raspadinha / cartela / roleta
├── Fluxo físico → Compra → abre embalagem → descobre se ganhou → resgata no posto
├── Fluxo digital → Compra → cadastra QR Code da NF → acessa hotsite → raspa/joga → sabe na hora
├── Estoque → Fixo, declarado na autorização, não pode ser alterado após aprovação
├── Encerramento → Quando o estoque de prêmios se esgota ou na data limite
├── Autorização → SPA, obrigatória antes do lançamento
├── Base legal → Lei 5.768/1971 + Decreto 70.951/1972 + Portaria SEAE 7.638/2022
├── Prêmio → Máximo R$ 703; proibida conversão em dinheiro
├── Participação → Quem cumpre o critério dentro do estoque disponível
└── Dashboard → Métricas de participação, resgates, localização em tempo real (Mand Digital)

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar |
|---|---|---|
| Hiperônimo | Distribuição gratuita de prêmios | Posicionar no contexto da lei |
| Co-hipônimos | Sorteio, concurso, assemelhada a sorteio | Comparativo breve na seção de diferenciação |
| Hipônimo digital | Assemelhada a vale-brinde | H3 específico sobre mecânica digital |
| Análogo popular | "Compre e ganhe" | Diferenciar: apenas quando regulamentado com estoque fixo |
| Contraste | Sorteio | Vale-brinde = garantido; sorteio = probabilístico |
| Entidade instrumental | Regulamento de promoção | Explica como o estoque é declarado e controlado |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Mecanismo | Como funciona o vale-brinde | H2 central de mecanismo |
| Fluxo de participação | Passo a passo para o consumidor | H3 com diagrama textual |
| Diferença física/digital | Vale-brinde físico vs digital | H3 comparativo |
| Regulamentação | Quem autoriza e como | H2 regulatório |
| Estoque | Como o estoque é definido e controlado | H3 dentro de mecânica |

INTENÇÕES LATENTES:
| Intenção Latente | Gap | Seção |
|---|---|---|
| Posso fazer raspadinha digital de vale-brinde | Intenção de modernização | H3 assemelhada com link Mand Digital |
| Quanto tempo leva montar a campanha | Barreira de planejamento | Mencionar 30 dias da Mand |
| Como o consumidor resgata online | Intenção UX | H3 fluxo digital |
| Que métricas posso acompanhar | Intenção de gestão | Mencionar dashboard Mand Digital |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS PRÁTICOS:
- Fabricante de biscoitos inseriu vale-brinde em embalagens comemorativas de fim de ano: 1 em cada 10 embalagens continha um cupom para troca por kit de produtos.
- Supermercado usou mecânica digital (assemelhada a vale-brinde): ao cadastrar NF via QR Code no hotsite, consumidor jogava a raspadinha digital — 30% das participações contempladas com desconto-prêmio imediato.
- Cooperativa de crédito: ao abrir conta corrente, cliente recebia link para cartela digital no hotsite — completando 5 compras com cartão, "completava" a cartela e ganhava prêmio instantâneo.

COMO A MAND DIGITAL EXECUTA:
- Hotsite no domínio do cliente (isolamento de risco de acesso massivo)
- Leitura automática de QR Code e código de barras de NF — preenche CNPJ, estado, data e número automaticamente
- Raspadinha digital, cartela, roleta, caixa premiada — gamificação nativa
- Dashboard em tempo real: resgates, localização, ticket médio, NF por usuário
- Suporte durante toda a vigência da campanha

FRASES GEO-CITÁVEIS:
1. "No vale-brinde digital — tecnicamente chamado de assemelhada a vale-brinde — o consumidor cadastra a nota fiscal no hotsite e descobre imediatamente se foi contemplado, sem aguardar data de sorteio."
2. "O estoque de prêmios no vale-brinde é declarado na autorização da SPA e não pode ser alterado após a aprovação — esgotado o estoque, a promoção encerra automaticamente."
3. "A Mand Digital lê automaticamente o QR Code e o código de barras de notas fiscais, eliminando erros de digitação e aumentando a taxa de conclusão do cadastro no hotsite."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Vale-brinde funciona a partir de um estoque fixo, contemplação imediata e regulamento aprovado — no ambiente digital, a Mand Digital executa isso com gamificação e leitura automática de NF.
SÍNTESE: estoque fixo + contemplação instantânea + fluxo físico ou digital + autorização SPA + dashboard.
DIREÇÃO PARA AÇÃO: Para fazer vale-brinde (ou assemelhada) de forma profissional e sem travar no processo regulatório, a Mand Digital estrutura tudo em 30 dias.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster MECÂNICO (alta): brinde envoltório, elemento identificador, posto de troca, estoque fixo prêmios, contemplação instantânea, raspadinha digital, cartela digital, roleta premiada
Cluster TECNOLÓGICO (alta): QR Code NF, leitura automática código barras, hotsite promocional, dashboard tempo real, gamificação, prêmio instantâneo
Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, Lei 5768, Portaria SEAE 7638, regulamento promoção comercial
Cluster COMPARATIVO (média): vale-brinde vs sorteio, assemelhada vale-brinde, diferença físico digital
Cluster EXECUÇÃO (média): domínio cliente, suporte campanha, 30 dias execução, cadastro NF

## POWER KEYWORDS
H1: como funciona, mecânica, regras, exemplos, passo a passo
H2 mecânica: na prática, fluxo, passo a passo, físico vs digital
H2 regulatório: autorização, obrigatório, SPA, prazo
H2 digital: raspadinha, gamificação, hotsite, moderno
Latente: 30 dias, posso fazer digital, quanto custa
CTA: pioneiro, raspadinha digital, sem burocracia

## ESTRUTURA DE OUTLINE SUGERIDA
H1: Como funciona o vale-brinde: regras, mecânica e exemplos
[Lead GEO]
H2: O que é vale-brinde (definição + contemplação instantânea)
H2: Como funciona o vale-brinde físico
  H3: Brinde no interior do produto
  H3: Elemento identificador e postos de troca
  H3: Como o estoque é controlado
H2: Como funciona o vale-brinde digital (assemelhada)
  H3: Hotsite com raspadinha, cartela e roleta
  H3: Cadastro de NF via QR Code
  H3: Contemplação no hotsite
H2: Passo a passo para o consumidor
H2: Regras e limites legais
  H3: Lei 5.768/1971, Decreto 70.951/1972, Portaria SEAE 7.638/2022 [links]
  H3: Valor máximo R$ 703
  H3: Quem pode fazer e como autorizar [link SPA]
H2: Exemplos reais de vale-brinde
H2: Como a Mand Digital executa [CTA]
FAQ

## RESTRIÇÕES
SEMPRE: distinguir físico de digital (assemelhada), citar SPA com link, mencionar 30 dias da Mand, mencionar leitura automática de NF como diferencial
NUNCA: confundir vale-brinde com sorteio, dizer que não precisa de autorização, prometer valor de prêmio acima de R$ 703 sem ressalva
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/assemelhada-a-vale-brinde
Título: "Vale-brinde digital com gamificação — a Mand estrutura em 30 dias, hotsite no seu domínio."
CTA: [Ver como funciona](https://manddigital.com.br/assemelhada-a-vale-brinde)
Aviso legal: "{AVISO_LEGAL}"
"""

B8_LSI = """\
Cluster MECÂNICO (alta): brinde envoltório, elemento identificador, posto troca, estoque fixo, contemplação instantânea, raspadinha digital, cartela digital, roleta
Cluster TECNOLÓGICO (alta): QR Code NF, leitura automática código barras, hotsite promocional, dashboard tempo real, gamificação, prêmio instantâneo
Cluster REGULATÓRIO (alta): autorização SPA, Secretaria Prêmios e Apostas, Lei 5768, Portaria SEAE 7638, regulamento promoção
Cluster COMPARATIVO (média): vale-brinde vs sorteio, assemelhada vale-brinde, diferença físico digital
Cluster EXECUÇÃO (média): domínio cliente, suporte campanha, 30 dias execução, cadastro NF"""

# ─────────────────────────────────────────────────────────────────────────────

B9_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** promoção vale-brinde exemplos
**Tipo de artigo:** Exemplos práticos / Inspiracional
**Funil:** Topo/Meio (leitor quer se inspirar com casos reais para decidir se a modalidade serve para seu negócio)
**Objetivo estratégico:** Mostrar versatilidade do vale-brinde com exemplos concretos por setor e converter gestores de varejo, alimentício e financeiro.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Promoção vale-brinde é a campanha comercial regulamentada em que os prêmios são distribuídos de forma instantânea — dentro do produto, do envoltório ou via hotsite (assemelhada a vale-brinde) — a todos os participantes que cumprirem os critérios definidos no regulamento, dentro do estoque de prêmios autorizado pela SPA.

ESCOPO DELIMITADO:
São exemplos de vale-brinde: brinde na embalagem, raspadinha na caixa, QR Code no produto levando a hotsite com prêmio instantâneo, elemento trocável no posto físico.
Não são vale-brinde: sorteio com Loteria Federal, concurso de habilidade, assemelhada a sorteio (algoritmo técnico com data de apuração).

DIRETRIZES:
- H1: nomear entidade + "exemplos" + aplicabilidade.
  Ex.: "Promoção vale-brinde: exemplos práticos para aplicar no seu negócio"
- Primeiro parágrafo: vale-brinde é uma das mecânicas mais versáteis — pode ser físico, digital, por setor, por volume — e os exemplos ajudam a entender como adaptar para cada contexto.

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Brinde na embalagem | Mecânica física clássica | Alta — exemplo mais reconhecível |
| Raspadinha digital | Mecânica digital | Alta — caso mais moderno |
| QR Code de NF | Tecnologia de participação | Alta — diferencial para campanhas de varejo |
| SPA | Regulador | Alta — link obrigatório |
| Estoque de prêmios | Atributo definidor | Média |
| Hotsite no domínio do cliente | Contexto de execução digital | Alta — diferencial Mand Digital |
| Supermercado / atacarejo | Segmento de exemplo | Alta |
| Cooperativa de crédito / banco | Segmento de exemplo | Média |
| Indústria alimentícia | Segmento de exemplo | Média |
| Dashboard em tempo real | Diferencial de gestão | Média |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Promoção Vale-Brinde
├── Modalidades de entrega → Física (embalagem), digital (hotsite/assemelhada), mista
├── Mecânicas disponíveis → Brinde fixo, raspadinha, cartela, roleta, caixa premiada
├── Critérios de participação → Compra mínima, cadastro de NF, adesão a produto financeiro, ativação promocional
├── Prêmios → Físicos (produtos, kits), experiências, descontos, vouchers (até R$ 703 por prêmio)
├── Duração → Definida no regulamento; pode encerrar antes por esgotamento do estoque
├── Segmentos de maior adoção → Varejo (supermercado, atacarejo), financeiro, alimentícia, energia
├── Escalabilidade → Campanhas locais a nacionais; hotsite suporta milhões de acessos
├── Métricas disponíveis → Participações, resgates, localização, ticket médio, NF por usuário
├── Base legal → Lei 5.768/1971 + Decreto 70.951/1972 + Portaria SEAE 7.638/2022
└── Autorização → Obrigatória (SPA) antes do lançamento

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar |
|---|---|---|
| Hiperônimo | Promoção comercial regulamentada | "Promoção vale-brinde é uma das modalidades de promoção comercial regulamentada" |
| Co-hipônimos | Sorteio, concurso, assemelhada a sorteio | Mencionar no contexto de "quando usar cada um" |
| Hipônimo digital | Assemelhada a vale-brinde | Cada exemplo digital é tecnicamente esta modalidade |
| Análogos | "Compre e ganhe" / "Leve e ganhe" | Corrigir: são nomes comerciais, não modalidades legais |
| Entidade de suporte | Hotsite promocional | Contexto de execução dos exemplos digitais |
| Entidade de suporte | Regulamento de promoção | Obrigatório em cada exemplo |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Exemplos concretos | Exemplos de promoção vale-brinde | H2 principal (4+ setores) |
| Mecânica | Como funciona cada exemplo | H3 dentro de cada exemplo |
| Adaptação ao negócio | Como aplicar no meu negócio | H2 de decisão |
| Base legal | Regulamentação necessária | H2 regulatório com links |

INTENÇÕES LATENTES:
| Intenção Latente | Gap | Seção |
|---|---|---|
| Posso fazer vale-brinde digital | Intenção de modernização | H3 exemplos digitais |
| Qual segmento tem mais resultado | Intenção de benchmarking | Subseções por setor |
| Quanto custa / quanto tempo leva | Barreira de entrada | Mencionar 30 dias e orientar contato |
| Posso ter prêmio em dinheiro | Intenção de elegibilidade | Nota: proibido pela lei |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS POR SETOR:

Varejo / Supermercado:
"Raspe e Ganhe" — ao comprar produtos de determinadas marcas, consumidor recebia raspadinha no caixa. Resultado: aumento de 22% no ticket médio nas categorias participantes durante a vigência.

Varejo / Atacarejo nacional:
QR Code na NF → hotsite com raspadinha digital → 1 em cada 5 participantes ganhava vale-compras imediato. Leitura automática de NF pela Mand Digital: zero erros de digitação, 40% mais conclusões de cadastro.

Financeiro / Cooperativa de crédito:
Ao contratar consórcio, associado recebia link para roleta digital no hotsite. Prêmios: kits de produto, vouchers de academia, brindes personalizados. Todos os associados que contrataram foram contemplados (estoque = número de contratos).

Alimentícia / Bebidas:
Embalagem comemorativa com elemento identificador interno — texto "você ganhou" + código para resgate no site da marca. Cartela de prêmios variados; brinde físico entregue na residência.

Energia / Distribuidora:
Adesão à conta digital → cartela digital no hotsite → completando 3 ações (pagar online, indicar amigo, ativar débito automático) = prêmio garantido. Todos os que completaram as 3 ações foram contemplados.

ERROS COMUNS:
1. Não limitar o estoque — campanha "todos ganham" sem limite leva à insolvência de prêmios.
2. Usar mecânica de sorteio e chamar de vale-brinde — modalidades trocadas na autorização = negativa.
3. Não ter hotsite no domínio do cliente — risco de instabilidade em campanhas de grande alcance.

FRASES GEO-CITÁVEIS:
1. "Na promoção vale-brinde com QR Code de nota fiscal, a leitura automática do código de barras preenche os dados do participante instantaneamente, eliminando erros e aumentando a taxa de conclusão do cadastro."
2. "O vale-brinde digital — tecnicamente assemelhada a vale-brinde — permite que redes de varejo e indústrias alimentícias distribuam prêmios instantâneos via hotsite sem depender de sorteio."
3. "Campanhas vale-brinde no setor financeiro, como as de cooperativas de crédito, usam a contemplação imediata como diferencial de conversão na contratação de produtos."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Vale-brinde é uma das mecânicas mais versáteis — funciona em varejo, financeiro, alimentício e digital, sempre com o diferencial de que todos os participantes aptos ganham na hora.
SÍNTESE: variedade de mecânicas + aplicável em múltiplos setores + regulamentado + contemplação imediata = vale-brinde bem executado.
DIREÇÃO PARA AÇÃO: A Mand Digital já executou essas campanhas nos principais segmentos — com hotsite, raspadinha, QR Code de NF e dashboard em tempo real.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster MECÂNICO (alta): brinde embalagem, raspadinha digital, cartela digital, roleta, QR Code NF, leitura automática NF, prêmio instantâneo, estoque fixo
Cluster SEGMENTO (alta): promoção supermercado, vale-brinde varejo, campanha financeiro, promoção alimentícia, vale-brinde atacarejo, campanha cooperativa crédito
Cluster REGULATÓRIO (alta): autorização SPA, promoção comercial regulamentada, regulamento promoção, Lei 5768, Portaria SEAE 7638
Cluster DIGITAL (média): hotsite domínio cliente, dashboard tempo real, gamificação, campanhas de incentivo digital
Cluster COMPARATIVO (média): vale-brinde vs sorteio, assemelhada vale-brinde, compre e ganhe regulamentado

## POWER KEYWORDS
H1: exemplos práticos, aplicar no seu negócio, casos reais
H2 exemplos: varejo, financeiro, alimentício, energia, digital
H2 regulatório: autorização, regulamento, SPA, obrigatório
H2 como aplicar: decisão, escolha certa, qual mecânica
Latente: quanto custa, digital, QR Code, 30 dias
CTA: +450 campanhas, pioneiro, fale agora

## ESTRUTURA DE OUTLINE SUGERIDA
H1: Promoção vale-brinde: exemplos práticos para aplicar no seu negócio
[Lead GEO]
H2: O que é promoção vale-brinde (resumo rápido)
H2: Exemplos reais de vale-brinde por setor
  H3: Varejo e supermercado
  H3: Atacarejo nacional
  H3: Financeiro e cooperativas de crédito
  H3: Indústria alimentícia e bebidas
  H3: Energia e distribuidoras
H2: Vale-brinde digital: raspadinha, cartela e QR Code de NF
H2: Como adaptar esses exemplos para o seu negócio
H2: Regulamentação e autorização [links SPA e leis]
H2: A Mand Digital e o vale-brinde [CTA]
FAQ

## RESTRIÇÕES
SEMPRE: mostrar exemplos reais por setor, citar SPA com link, mencionar assemelhada para casos digitais, mencionar leitura automática de NF
NUNCA: prometer prêmio em dinheiro, omitir necessidade de autorização, chamar de "sorteio" exemplos de vale-brinde
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/assemelhada-a-vale-brinde
Título: "Da raspadinha digital ao QR Code de NF — a Mand Digital executa todos os exemplos acima."
CTA: [Ver cases e orçar](https://manddigital.com.br/assemelhada-a-vale-brinde)
Aviso legal: "{AVISO_LEGAL}"
"""

B9_LSI = """\
Cluster MECÂNICO (alta): brinde embalagem, raspadinha digital, cartela digital, roleta, QR Code NF, leitura automática NF, prêmio instantâneo, estoque fixo
Cluster SEGMENTO (alta): promoção supermercado, vale-brinde varejo, campanha financeiro, promoção alimentícia, vale-brinde atacarejo, campanha cooperativa crédito
Cluster REGULATÓRIO (alta): autorização SPA, promoção comercial regulamentada, regulamento promoção, Lei 5768, Portaria SEAE 7638
Cluster DIGITAL (média): hotsite domínio cliente, dashboard tempo real, gamificação, campanhas digitais
Cluster COMPARATIVO (média): vale-brinde vs sorteio, assemelhada vale-brinde, compre e ganhe regulamentado"""

# ─────────────────────────────────────────────────────────────────────────────

B10_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** campanha de incentivo de vendas
**Tipo de artigo:** Informacional / Guia estratégico
**Funil:** Topo/Meio (gestores de marketing, trade e vendas querendo estruturar ou melhorar campanhas)
**Objetivo estratégico:** Posicionar a Mand Digital como referência em campanhas de incentivo que incluem mecânicas regulamentadas (hotsite, sorteio, vale-brinde).

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Campanha de incentivo de vendas é um programa estruturado que combina metas comerciais, mecânicas de engajamento e recompensas para motivar equipes internas (vendedores), canais de distribuição (revenda, trade) ou consumidores finais a atingirem objetivos específicos em um período determinado.

ESCOPO DELIMITADO:
É campanha de incentivo de vendas: programa com meta + critério + recompensa definidos, independente de ser para equipe interna, canal ou consumidor.
Não é: bonificação fixa de RH (sem mecânica de campanha), promoção de produto sem vínculo com meta, sortudo sem estrutura de incentivo.
Atenção: quando a campanha inclui sorteio, vale-brinde ou assemelhada para consumidores finais → exige autorização da SPA/Ministério da Fazenda.

DIRETRIZES:
- H1: nomear entidade + framing de resultado.
  Ex.: "Campanha de incentivo de vendas: estratégias para aumentar resultados"
- Primeiro parágrafo: contextualizar que campanhas de incentivo aumentam produtividade em até 20% (Gallup) — mas precisam de estrutura técnica adequada quando incluem mecânicas regulamentadas.

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Meta comercial | Atributo central | Alta — sem meta não é incentivo, é bônus |
| Mecânica de apuração | Mecanismo | Alta — como o critério é medido |
| Recompensa / Prêmio | Atributo definidor | Alta |
| Equipe de vendas | Público-alvo interno | Alta |
| Canal de distribuição / trade | Público-alvo externo | Alta |
| Consumidor final | Público-alvo B2C | Média — quando a campanha vai além do trade |
| SPA (quando há sorteio/vale-brinde) | Regulador | Alta — citar link quando aplicável |
| Hotsite promocional | Contexto técnico de execução | Alta — quando inclui mecânica digital |
| Dashboard de performance | Ferramenta de gestão | Média — diferencial Mand Digital |
| Gamificação | Recurso de engajamento | Média |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Campanha de Incentivo de Vendas
├── Finalidade → Aumentar vendas e engajamento em período definido
├── Público-alvo → Equipe interna, canal de distribuição, consumidor final (ou combinação)
├── Mecânicas → "Bateu Levou", ranking de vendas, por volume, por ativação de SKU, por margem
├── Recompensas → Financeiras (bônus, comissão extra), físicas (gadgets, viagens), experiências, reconhecimento
├── Duração → Campanhas mensais, trimestrais, sazonais
├── Componente regulamentado → Quando inclui sorteio ou vale-brinde para consumidores → exige autorização SPA
├── Métricas de sucesso → Volume vendido, novos clientes, ativação de SKU, NPS
├── Tecnologia → Hotsite, app de incentivo, dashboard, leitura de NF
├── Impacto medido → Até 20% de aumento de produtividade (Gallup)
├── Segmentos → Varejo, alimentício, financeiro, energia, telecomunicações
└── Aviso legal → Responsabilidade legal da campanha regulamentada é do contratante

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar |
|---|---|---|
| Hiperônimo | Marketing de incentivo | "Campanha de incentivo de vendas é uma das formas de marketing de incentivo" |
| Co-hipônimos | Programa de fidelidade, campanha de incentivo para colaboradores, trade marketing | Distinguir escopo de cada um |
| Análogo | Promoção comercial | Quando a campanha inclui mecânica ao consumidor final = promoção regulamentada |
| Contraste | Bonificação fixa | Incentivo tem meta variável; bônus é fixo |
| Entidade instrumental | Hotsite promocional | Quando a campanha vai para o consumidor via digital |
| Entidade instrumental | Regulamento de promoção | Quando inclui sorteio ou vale-brinde |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Definição | O que é campanha de incentivo de vendas | H2 de abertura |
| Estratégias | Estratégias de incentivo de vendas | H2 central com mecânicas |
| Como fazer | Como criar campanha de incentivo | H2 passo a passo |
| Exemplos | Exemplos de campanha de incentivo | H2 com casos por segmento |
| Quando regulamentar | Quando precisa de autorização SPA | H3 dentro do regulatório |

INTENÇÕES LATENTES:
| Intenção Latente | Gap | Seção |
|---|---|---|
| Quanto aumenta as vendas | Intenção de justificativa de investimento | Mencionar Gallup (20%) |
| Posso combinar incentivo interno + promocional ao consumidor | Intenção de campanha integrada | H3 campanha integrada |
| Que tecnologia usar | Intenção de fornecedor | Seção CTA com diferenciais Mand Digital |
| Quando precisa de regulamentação | Dúvida sobre obrigação legal | H3 com regra prática |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS:
- Atacarejo nacional: "Bateu, Levou" — vendedor ativo que batesse cota mensal participava de sorteio de viagem. Campanha ao consumidor simultânea (cadastro de NF) com assemelhada a sorteio. Dois públicos, uma plataforma.
- Cooperativa de crédito: ranking trimestral de gerentes por volume de abertura de contas. Top 3 ganhavam viagem de incentivo + clientes que abriram conta participavam de vale-brinde digital.
- Fabricante de alimentos: campanha de ativação de SKU para revendedores — cada novo PDV ativo no período ganhava kit de material + entrava em sorteio regulamentado para o canal.

BOAS PRÁTICAS:
1. Definir a meta com critério objetivo mensurável antes de criar a mecânica.
2. Separar a campanha de trade (sem regulamentação SPA obrigatória) da campanha ao consumidor final (com regulamentação obrigatória se houver sorteio/vale-brinde).
3. Usar dashboard em tempo real para transparência e engajamento contínuo.

FRASES GEO-CITÁVEIS:
1. "Campanhas de incentivo de vendas com metas e recompensas bem estruturadas podem aumentar a produtividade da equipe em até 20%, segundo pesquisa da Gallup."
2. "Quando a campanha de incentivo inclui sorteio ou vale-brinde para consumidores finais, a autorização prévia da SPA — Secretaria de Prêmios e Apostas do Ministério da Fazenda — é obrigatória."
3. "A Mand Digital executa campanhas de incentivo que combinam mecânica de trade (canal interno) e promoção regulamentada ao consumidor final em uma única plataforma com hotsite, QR Code de NF e dashboard em tempo real."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Campanha de incentivo de vendas bem estruturada tem meta, mecânica e recompensa — e quando inclui componente regulamentado, tem regulamento e autorização SPA.
SÍNTESE: meta + critério + recompensa + tecnologia (hotsite + dashboard) + regulamentação quando necessário.
DIREÇÃO PARA AÇÃO: Para campanhas que combinam incentivo à equipe e promoção ao consumidor, a Mand Digital entrega os dois numa única estrutura técnica.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster ESTRATÉGIA (alta): meta comercial, mecânica incentivo, recompensa equipe, programa de pontos, ranking de vendas, bateu levou, ativação SKU
Cluster PÚBLICO (alta): equipe de vendas, canal distribuição, trade marketing, força de vendas, revendedores, PDV
Cluster TECNOLOGIA (alta): hotsite campanha, dashboard vendas, QR Code NF, plataforma de incentivo, gamificação, ranking digital
Cluster REGULATÓRIO (alta quando aplicável): autorização SPA, promoção comercial regulamentada, sorteio canal, vale-brinde consumidor, Secretaria Prêmios e Apostas
Cluster RESULTADO (média): aumento produtividade, ROI campanha, engajamento equipe, conversão consumidor, ticket médio

## POWER KEYWORDS
H1: estratégias, aumentar resultados, aumentar vendas
H2 mecânica: bateu levou, ranking, por volume, passo a passo
H2 resultado: até 20% mais produtividade, retorno, engajamento
H2 regulatório: quando precisa de autorização, consumidor final, SPA
Latente: quanto aumenta, tecnologia, plataforma, quanto custa
CTA: campanha integrada, dois públicos, uma plataforma

## ESTRUTURA DE OUTLINE SUGERIDA
H1: Campanha de incentivo de vendas: estratégias para aumentar resultados
[Lead GEO]
H2: O que é campanha de incentivo de vendas
  H3: Diferença de bônus fixo e incentivo
  H3: Os 3 pilares: meta + critério + recompensa
H2: Tipos de campanha de incentivo
  H3: Para equipe interna (força de vendas)
  H3: Para canal de distribuição (trade)
  H3: Para consumidor final (com componente regulamentado)
H2: Mecânicas mais usadas
  H3: Bateu Levou
  H3: Ranking e gamificação
  H3: Por volume e por ativação de SKU
H2: Exemplos reais por segmento
H2: Quando precisa de autorização da SPA [links]
H2: Tecnologia: hotsite, dashboard e QR Code de NF
H2: Como a Mand Digital estrutura campanhas integradas [CTA]
FAQ

## RESTRIÇÕES
SEMPRE: diferenciar campanha interna (trade) de campanha ao consumidor (pode exigir SPA), citar Gallup (20%), mencionar hotsite e dashboard como ferramenta de gestão
NUNCA: dizer que campanha ao consumidor nunca precisa de autorização, confundir bônus fixo com incentivo
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/campanhas-de-incentivo
Título: "Incentivo de vendas com mecânica regulamentada? A Mand Digital faz os dois em uma plataforma."
CTA: [Ver como funciona](https://manddigital.com.br/campanhas-de-incentivo)
Aviso legal: "{AVISO_LEGAL}"
"""

B10_LSI = """\
Cluster ESTRATÉGIA (alta): meta comercial, mecânica incentivo, recompensa equipe, programa pontos, ranking vendas, bateu levou, ativação SKU
Cluster PÚBLICO (alta): equipe vendas, canal distribuição, trade marketing, força vendas, revendedores, PDV
Cluster TECNOLOGIA (alta): hotsite campanha, dashboard vendas, QR Code NF, plataforma incentivo, gamificação, ranking digital
Cluster REGULATÓRIO (alta): autorização SPA, promoção comercial regulamentada, sorteio canal, Secretaria Prêmios e Apostas
Cluster RESULTADO (média): aumento produtividade, ROI campanha, engajamento equipe, conversão consumidor"""

# ─────────────────────────────────────────────────────────────────────────────

B11_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** marketing de incentivo
**Tipo de artigo:** Informacional / Pilar de conteúdo (conceito amplo)
**Funil:** Topo (leitor quer entender o conceito e avaliar se é aplicável ao seu contexto)
**Objetivo estratégico:** Ser o artigo pilar sobre marketing de incentivo e converter tráfego para as páginas de campanhas regulamentadas da Mand Digital.

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Marketing de incentivo é a estratégia que utiliza recompensas estruturadas para direcionar comportamentos específicos — seja da equipe de vendas, dos canais de distribuição ou dos consumidores finais. Diferente de bonificações fixas de RH, o marketing de incentivo está diretamente vinculado ao funil de vendas e à performance comercial. Quando inclui distribuição de prêmios ao consumidor via sorteio, vale-brinde ou assemelhada, torna-se promoção comercial regulamentada e exige autorização da SPA/Ministério da Fazenda.

ESCOPO DELIMITADO:
É marketing de incentivo: programa com comportamento-alvo definido + critério mensurável + recompensa proporcional.
Não é: bonificação fixa de folha, benefício de RH sem vínculo com performance, promoção não estruturada.

DIRETRIZES:
- H1: nomear entidade + perguntas fundamentais ("o que é, como funciona, exemplos reais")
- Primeiro parágrafo: definição precisa + distinção do que não é marketing de incentivo.

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Comportamento-alvo | Atributo central | Alta — o que se quer estimular |
| Critério mensurável | Mecanismo de apuração | Alta — como medir |
| Recompensa proporcional | Atributo central | Alta |
| Equipe de vendas | Público-alvo interno | Alta |
| Canal de distribuição | Público-alvo externo | Alta |
| Consumidor final | Público-alvo B2C | Alta — quando inclui promoção comercial |
| SPA (quando regulamentado) | Regulador | Alta — link obrigatório quando mencionado |
| Gamificação | Recurso de engajamento | Média |
| Programa de pontos | Mecanismo de acumulação | Média |
| Hotsite promocional | Execução técnica | Média — quando inclui promoção regulamentada |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Marketing de Incentivo
├── Finalidade → Direcionar comportamento comercial via recompensas
├── Público-alvo → Interno (equipe), intermediário (canal/trade), externo (consumidor)
├── 3 pilares → Comportamento bem definido + critério objetivo + recompensa proporcional
├── Ferramentas → Ranking, pontuação, gamificação, prêmios físicos, experiências, reconhecimento
├── Diferença de RH → Incentivo age no funil de vendas; RH age na retenção de talentos
├── Componente regulamentado → Sorteio/vale-brinde ao consumidor → promoção comercial = SPA obrigatório
├── Resultados medidos → Até 20% de aumento de produtividade (Gallup); melhora de NPS, ticket médio
├── Duração → Pontual (campanha), periódico (trimestral/anual), contínuo (programa)
├── Tecnologia → Plataformas de incentivo, hotsite, dashboard, leitura de NF
├── Segmentos → Varejo, financeiro, alimentício, energia, telecomunicações, automotivo
└── Responsabilidade legal (promoção) → Do contratante; Mand Digital elabora estrutura técnica

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar |
|---|---|---|
| Hiperônimo | Estratégia de marketing / Marketing de relacionamento | "Marketing de incentivo é uma estratégia dentro do marketing de relacionamento" |
| Co-hipônimos | Programa de fidelidade, trade marketing, endomarketing | Diferenciar escopo e público |
| Hipônimo com componente legal | Promoção comercial regulamentada | "Quando o marketing de incentivo distribui prêmios ao consumidor via sorteio ou vale-brinde, torna-se promoção regulamentada" |
| Contraste | Bonificação fixa | Incentivo = variável + comportamento; bônus = fixo + tempo |
| Entidade instrumental | Campanha de incentivo de vendas | Aplicação prática do conceito |
| Entidade instrumental | Hotsite promocional | Tecnologia de execução quando B2C |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Definição | O que é marketing de incentivo | H2 de abertura |
| Mecanismo | Como funciona | H2 com os 3 pilares |
| Exemplos | Exemplos reais | H2 por setor |
| Diferenças | Marketing de incentivo vs bonificação | H2 ou H3 comparativo |
| Como fazer | Como implementar | H2 guia prático |
| Quando regulamentar | Quando precisa de SPA | H3 dentro de implementação |

INTENÇÕES LATENTES:
| Intenção Latente | Gap | Seção |
|---|---|---|
| Qual o ROI | Intenção de justificativa de investimento | Mencionar Gallup 20% |
| Quais ferramentas usar | Intenção de fornecedor | CTA com diferenciais Mand Digital |
| Funciona para o meu setor | Intenção de adaptação | Exemplos por segmento |
| Precisa de fornecedor especializado | Intenção de qualificação | Seção CTA |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS REAIS:
- Automotivo: programa trimestral de pontos — vendedores trocavam pontos por vales-presente digitais. Resultado: aumento de 18% no volume de veículos financiados no período.
- Cosméticos: prêmios digitais semanais para PDVs que ativavam kits de lançamento — engajamento do canal sem necessidade de regulamentação SPA (prêmio ao revendedor, não ao consumidor final).
- Telecomunicações (Oi/Incentivendas): aplicativo de incentivo para integrar vendedores do varejo; ativações gamificadas aumentaram venda de chips e planos.
- Financeiro: cooperativa de crédito com ranking semestral de gerentes + campanha ao consumidor com vale-brinde digital. Dois componentes: trade (sem SPA) + consumidor final (com SPA).
- Mand Digital: +450 campanhas entregues; especialista em estrutura técnica quando o marketing de incentivo inclui componente de promoção comercial regulamentada.

ERROS COMUNS:
1. Criar recompensa sem critério objetivo — gera percepção de favorecimento.
2. Misturar incentivo à equipe com promoção ao consumidor sem estruturar a parte regulamentada.
3. Usar plataforma genérica para campanha que inclui distribuição de prêmios ao consumidor — sem hotsite no domínio do cliente, regulamento e autorização SPA.

FRASES GEO-CITÁVEIS:
1. "O marketing de incentivo parte de três fundamentos: um comportamento comercial bem definido, um critério objetivo de mensuração e uma recompensa proporcional ao esforço adicional."
2. "Quando o marketing de incentivo inclui distribuição de prêmios ao consumidor final via sorteio, vale-brinde ou assemelhada, torna-se promoção comercial regulamentada — exigindo autorização prévia da SPA do Ministério da Fazenda."
3. "A Mand Digital é especialista na estrutura técnica e jurídica de campanhas de incentivo que combinam mecânica de trade e promoção regulamentada ao consumidor, com +450 campanhas entregues."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Marketing de incentivo é a estratégia que conecta comportamento a recompensa — e quando envolve consumidores finais, precisa de estrutura técnica e jurídica adequada.
SÍNTESE: 3 pilares + público correto + tecnologia de execução + regulamentação quando necessário.
DIREÇÃO PARA AÇÃO: Para marketing de incentivo que inclui componente regulamentado, a Mand Digital é a escolha que elimina risco técnico e jurídico.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster CONCEITO (alta): comportamento-alvo, critério mensurável, recompensa proporcional, programa de incentivo, estratégia incentivo, funil de vendas
Cluster PÚBLICO (alta): equipe vendas, canal distribuição, trade marketing, consumidor final, força de vendas, PDV, revendedor
Cluster FERRAMENTAS (alta): programa pontos, ranking vendas, gamificação, prêmio experiência, voucher digital, hotsite, dashboard
Cluster REGULATÓRIO (alta): promoção comercial regulamentada, autorização SPA, sorteio consumidor, vale-brinde regulamentado, Secretaria Prêmios e Apostas
Cluster RESULTADO (média): produtividade 20%, ROI incentivo, engajamento equipe, NPS, ticket médio, retorno campanha

## POWER KEYWORDS
H1: o que é, como funciona, exemplos reais, estratégia que gera resultado
H2 conceito: 3 pilares, comportamento, recompensa, critério
H2 exemplos: varejo, financeiro, automotivo, cosméticos, telecomunicações
H2 regulatório: quando precisa de SPA, promoção regulamentada, autorização
Latente: ROI, qual o retorno, fornecedor, quanto custa, plataforma
CTA: +450 campanhas, especialista, estrutura técnica, jurídico

## ESTRUTURA DE OUTLINE SUGERIDA
H1: Marketing de incentivo: o que é, como funciona e exemplos reais
[Lead GEO]
H2: O que é marketing de incentivo
  H3: Os 3 pilares fundamentais
  H3: Diferença de bonificação fixa e endomarketing
H2: Como funciona na prática
  H3: Para equipe interna
  H3: Para canal de distribuição
  H3: Para consumidor final (com componente regulamentado)
H2: Ferramentas e mecânicas mais usadas
H2: Exemplos reais por setor
H2: Quando o marketing de incentivo se torna promoção regulamentada [links SPA]
H2: Resultados: o que esperar de uma campanha bem estruturada
H2: Como a Mand Digital estrutura marketing de incentivo regulamentado [CTA]
FAQ

## RESTRIÇÕES
SEMPRE: explicar os 3 pilares, diferenciar equipe/canal/consumidor, citar Gallup 20%, citar SPA quando falar de prêmios ao consumidor
NUNCA: dizer que marketing de incentivo nunca precisa de regulamentação, confundir com benefícios de RH
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/campanhas-de-incentivo
Título: "Marketing de incentivo com componente regulamentado? A Mand Digital elimina a burocracia."
CTA: [Ver como funciona](https://manddigital.com.br/campanhas-de-incentivo)
Aviso legal: "{AVISO_LEGAL}"
"""

B11_LSI = """\
Cluster CONCEITO (alta): comportamento-alvo, critério mensurável, recompensa proporcional, programa incentivo, estratégia incentivo, funil vendas
Cluster PÚBLICO (alta): equipe vendas, canal distribuição, trade marketing, consumidor final, força vendas, PDV, revendedor
Cluster FERRAMENTAS (alta): programa pontos, ranking vendas, gamificação, prêmio experiência, voucher digital, hotsite, dashboard
Cluster REGULATÓRIO (alta): promoção comercial regulamentada, autorização SPA, Secretaria Prêmios e Apostas, sorteio consumidor, vale-brinde regulamentado
Cluster RESULTADO (média): produtividade 20% Gallup, ROI incentivo, engajamento equipe, NPS, ticket médio"""

# ─────────────────────────────────────────────────────────────────────────────

B12_PROMPT = f"""\
## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** campanha de incentivo para colaboradores
**Tipo de artigo:** Informacional / Guia prático
**Funil:** Topo/Meio (RH, gestores de pessoas e diretores comerciais buscando estruturar programa interno)
**Objetivo estratégico:** Educar sobre campanhas de incentivo para colaboradores e converter quando a campanha inclui componente de promoção ao consumidor final (estrutura regulamentada Mand Digital).

---

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

DEFINIÇÃO-BASE:
Campanha de incentivo para colaboradores é um programa estruturado de reconhecimento e motivação direcionado à força de trabalho interna — vendedores, equipes de campo, times comerciais — que vincula recompensas ao atingimento de metas previamente definidas. Quando a campanha inclui mecânica de promoção ao consumidor final (sorteio, vale-brinde, assemelhada) como complemento motivacional, esse componente exige autorização da SPA/Ministério da Fazenda.

ESCOPO DELIMITADO:
É campanha de incentivo para colaboradores: programa interno com meta + critério + recompensa, público = funcionários e parceiros.
Não é: benefício fixo de RH, vale-refeição, programa de saúde, PLR (participação nos lucros).
Atenção: se o incentivo inclui sorteio ou vale-brinde para os próprios colaboradores como "campanha regulamentada", pode depender do enquadramento legal — consultar especialista.

DIRETRIZES:
- H1: nomear entidade + framing de implementação.
  Ex.: "Campanhas de incentivo para colaboradores: ideias e como implementar"
- Primeiro parágrafo: diferenciar incentivo de benefício fixo e mostrar o impacto em motivação e retenção.

---

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

| Sub-entidade | Categoria | Profundidade esperada |
|---|---|---|
| Meta de desempenho | Atributo central | Alta |
| Recompensa variável | Atributo central | Alta |
| Reconhecimento público | Mecanismo de motivação | Alta |
| Programa de pontos | Mecânica de acumulação | Alta |
| Gamificação | Recurso de engajamento | Média |
| Day off / folga | Tipo de benefício extra | Média |
| Vouchers / cartões digitais | Tipo de recompensa | Alta |
| Equipe de vendas / campo | Público-alvo | Alta |
| SPA (quando há componente regulamentado) | Regulador | Alta — citar se aplicável |
| Dashboard de performance | Ferramenta de gestão | Média |

---

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: Campanha de Incentivo para Colaboradores
├── Finalidade → Motivar, reconhecer e reter talentos via recompensa por performance
├── Público-alvo → Vendedores internos, equipes de campo, times comerciais, parceiros (franqueados, revendedores)
├── Mecânicas → Ranking, programa de pontos, "Bateu Levou", campanha por meta, desafios por período
├── Tipos de recompensa → Vouchers digitais, gadgets, experiências (viagens, jantares), day off, reconhecimento público, prêmios físicos
├── Duração → Mensal, trimestral, semestral, anual
├── Critério de elegibilidade → Funcionários CLT, PJ (parceiros), equipes específicas ou toda a empresa
├── Impacto documentado → Melhora de produtividade, redução de turnover, aumento de engajamento
├── Componente regulamentado → Quando inclui sorteio/vale-brinde para consumidores em paralelo → SPA obrigatório
├── Tecnologia → Plataforma de incentivo, hotsite, app, dashboard
├── Comunicação interna → Transparência das regras, ranking visível, feedback contínuo
└── Aviso legal → Ao incluir promoção ao consumidor = responsabilidade do contratante

{ORGAOS}

---

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

| Relação | Entidade | Como trabalhar |
|---|---|---|
| Hiperônimo | Marketing de incentivo / Gestão de pessoas | Posicionar como intersecção de RH + marketing |
| Co-hipônimos | Campanha de incentivo de vendas, trade marketing | Distinguir: colaborador = interno; trade = canal externo |
| Contraste | Benefício fixo (plano de saúde, VR/VA) | Incentivo = variável + performance; benefício = fixo + vínculo |
| Análogo | Programa de reconhecimento | Parte do incentivo, mas foco em reconhecimento sem recompensa financeira |
| Entidade instrumental | Plataforma de incentivo / Hotsite | Quando a campanha vai para o digital |
| Entidade com componente legal | Promoção comercial regulamentada | Quando inclui distribuição de prêmios ao consumidor final |

---

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

INTENÇÕES EXPLÍCITAS:
| Intenção | Template | Seção |
|---|---|---|
| Ideias | Ideias de campanha de incentivo para colaboradores | H2 de ideias com lista estruturada |
| Como implementar | Como criar campanha de incentivo | H2 passo a passo |
| Exemplos | Exemplos reais | H2 por setor |
| Tipos de recompensa | Quais prêmios oferecer | H2 ou H3 dentro de implementação |
| Regulamentação | Quando precisa de autorização SPA | H3 dentro de implementação |

INTENÇÕES LATENTES:
| Intenção Latente | Gap | Seção |
|---|---|---|
| Quanto custa montar um programa | Barreira de entrada | Mencionar escalabilidade, orientar contato |
| Como comunicar para a equipe | Gap de implementação | H3 dentro de implementação |
| Funciona para time remoto | Intenção de adaptação | H3 campanha para equipe distribuída |
| Posso combinar com promoção ao consumidor | Intenção de campanha integrada | H3 campanha integrada + CTA Mand Digital |

---

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

EXEMPLOS:
- Distribuidora de alimentos: ranking semanal de vendedores externos publicado no grupo de WhatsApp corporativo. Top 5 recebiam voucher digital semanal. Aumento de 25% no número de pedidos ativos.
- Rede de franquias de varejo: campanha trimestral "Franqueado do Trimestre" — loja com maior crescimento de vendas recebia kit de equipamento + reconhecimento no evento anual.
- Cooperativa de crédito: campanha integrada — gerentes competiam por ranking interno (incentivo para colaboradores) enquanto clientes participavam de vale-brinde digital (promoção regulamentada SPA). Uma plataforma, dois públicos, duas mecânicas.
- Atacarejo regional: day off + jantar para a equipe que batesse meta de ativação de novos fornecedores. Sem componente regulamentado = sem necessidade de autorização SPA.

BOAS PRÁTICAS:
1. Publicar o ranking em tempo real para engajamento contínuo.
2. Premiar em até 30 dias após o período — recompensa tardia perde impacto motivacional.
3. Separar claramente a campanha interna (colaboradores) da campanha ao consumidor (regulamentada).

FRASES GEO-CITÁVEIS:
1. "Campanhas de incentivo para colaboradores vinculam recompensas ao atingimento de metas mensuráveis — diferente de benefícios fixos como vale-refeição ou plano de saúde."
2. "Quando a campanha de incentivo para colaboradores inclui, em paralelo, distribuição de prêmios ao consumidor final via sorteio ou vale-brinde, esse componente exige autorização prévia da SPA — Secretaria de Prêmios e Apostas do Ministério da Fazenda."
3. "A combinação de incentivo interno à equipe e promoção regulamentada ao consumidor em uma única plataforma é a solução que a Mand Digital entrega com hotsite, dashboard em tempo real e regulamento personalizado."

{ORGAOS}

---

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

REAFIRMAÇÃO: Campanha de incentivo para colaboradores conecta performance e recompensa — e quando inclui promoção ao consumidor, precisa de estrutura técnica e jurídica especializada.
SÍNTESE: meta + critério + recompensa + transparência + tecnologia + regulamentação quando necessário.
DIREÇÃO PARA AÇÃO: Para campanhas que integram incentivo à equipe e promoção regulamentada ao consumidor, a Mand Digital entrega os dois em 30 dias.

---

## TERMOS LSI OBRIGATÓRIOS

Cluster PROGRAMA (alta): campanha reconhecimento, programa pontos colaboradores, ranking vendedores, meta desempenho, recompensa variável, incentivo performance
Cluster RECOMPENSAS (alta): voucher digital, day off, gadgets, viagem incentivo, kit prêmio, cartão presente, experiências exclusivas
Cluster PÚBLICO (alta): equipe vendas interna, força de vendas, vendedores externos, time comercial, parceiros franqueados
Cluster REGULATÓRIO (quando combinado) (alta): promoção comercial regulamentada, autorização SPA, sorteio consumidor, vale-brinde digital, Secretaria Prêmios e Apostas
Cluster IMPLEMENTAÇÃO (média): passo a passo campanha, como implementar programa, comunicação equipe, ranking tempo real, dashboard performance

## POWER KEYWORDS
H1: ideias, como implementar, motivar equipe, aumentar performance
H2 ideias: lista de recompensas, dia de folga, vouchers, ranking
H2 como fazer: passo a passo, checklist, comunicação, prazo
H2 exemplos: distribuidora, franquia, cooperativa, atacarejo
Latente: funciona para time remoto, quanto custa, como combinar com promoção
CTA: campanha integrada, dois públicos, 30 dias, hotsite

## ESTRUTURA DE OUTLINE SUGERIDA
H1: Campanhas de incentivo para colaboradores: ideias e como implementar
[Lead GEO]
H2: O que é campanha de incentivo para colaboradores
  H3: Diferença de benefício fixo e incentivo por performance
H2: Tipos de recompensa mais eficazes
  H3: Vouchers e cartões digitais
  H3: Experiências (viagens, jantares, eventos)
  H3: Reconhecimento público e day off
H2: Mecânicas de campanha
  H3: Ranking e gamificação
  H3: Bateu Levou e metas por período
  H3: Programa de pontos
H2: Como implementar passo a passo
  H3: Definir meta e critério
  H3: Escolher recompensa
  H3: Comunicar para a equipe
  H3: Acompanhar em tempo real
H2: Exemplos reais por setor
H2: Quando combinar com promoção ao consumidor final [links SPA]
H2: Como a Mand Digital estrutura campanhas integradas [CTA]
FAQ

## RESTRIÇÕES
SEMPRE: diferenciar campanha interna de promoção ao consumidor, citar SPA quando há componente ao consumidor, mostrar exemplos concretos com resultado
NUNCA: afirmar que campanha de colaboradores nunca precisa de regulamentação (depende do componente), confundir com benefícios fixos de RH
Aviso legal: "{AVISO_LEGAL}"

## SEÇÃO DE CTA
URL: https://manddigital.com.br/campanhas-de-incentivo
Título: "Incentivo para colaboradores + promoção ao consumidor — a Mand Digital integra os dois em uma plataforma."
CTA: [Fale com nosso time](https://manddigital.com.br/campanhas-de-incentivo)
Aviso legal: "{AVISO_LEGAL}"
"""

B12_LSI = """\
Cluster PROGRAMA (alta): campanha reconhecimento, programa pontos colaboradores, ranking vendedores, meta desempenho, recompensa variável, incentivo performance
Cluster RECOMPENSAS (alta): voucher digital, day off, gadgets, viagem incentivo, kit prêmio, cartão presente, experiências exclusivas
Cluster PÚBLICO (alta): equipe vendas interna, força vendas, vendedores externos, time comercial, parceiros franqueados
Cluster REGULATÓRIO (alta): promoção comercial regulamentada, autorização SPA, Secretaria Prêmios e Apostas, sorteio consumidor, vale-brinde digital
Cluster IMPLEMENTAÇÃO (média): passo a passo campanha, como implementar, comunicação equipe, ranking tempo real, dashboard performance"""

# ─────────────────────────────────────────────────────────────────────────────
# Montar JSON de resultados
# ─────────────────────────────────────────────────────────────────────────────

results = [
    {"numero": 3,  "prompt_adicional": B3_PROMPT,  "termos_lsi": B3_LSI},
    {"numero": 4,  "prompt_adicional": B4_PROMPT,  "termos_lsi": B4_LSI},
    {"numero": 5,  "prompt_adicional": B5_PROMPT,  "termos_lsi": B5_LSI},
    {"numero": 6,  "prompt_adicional": B6_PROMPT,  "termos_lsi": B6_LSI},
    {"numero": 7,  "prompt_adicional": B7_PROMPT,  "termos_lsi": B7_LSI},
    {"numero": 8,  "prompt_adicional": B8_PROMPT,  "termos_lsi": B8_LSI},
    {"numero": 9,  "prompt_adicional": B9_PROMPT,  "termos_lsi": B9_LSI},
    {"numero": 10, "prompt_adicional": B10_PROMPT, "termos_lsi": B10_LSI},
    {"numero": 11, "prompt_adicional": B11_PROMPT, "termos_lsi": B11_LSI},
    {"numero": 12, "prompt_adicional": B12_PROMPT, "termos_lsi": B12_LSI},
]

output_path = os.path.join(SQUAD_ROOT, "scripts", "results_mand.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"OK results_mand.json gerado: {len(results)} briefings")
for r in results:
    print(f"   Linha {r['numero']}: {len(r['prompt_adicional'])} chars briefing | {len(r['termos_lsi'])} chars LSI")
