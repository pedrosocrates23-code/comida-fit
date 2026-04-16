#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Combina todos os briefings (linhas 2-16) e gera a planilha final.
"""
import json
import subprocess
import sys

# ─────────────────────────────────────────────────────────────────────────────
# LINHAS 12–16 — dados embutidos diretamente
# ─────────────────────────────────────────────────────────────────────────────

ROW_12_PROMPT = """BRIEFING E.E.A.T.S. COMPLETO — Keyword: gestão de minimercado autônomo

## 1. ENTITY LOCK-IN
Entidade âncora principal: gestão de minimercado autônomo (processo gerencial digital e remoto aplicado ao varejo self-service). Entidade operacional: franqueado/operador (responsável pela gestão cotidiana). Entidade de suporte estrutural: Peggô Market (franqueadora com plataforma proprietária de gestão integrada). O artigo responde ao intent operacional/procedimental de quem já decidiu investir no modelo ou está em fase ativa de operação. É diferente dos artigos de atração (como abrir, quanto custa) — aqui o foco é COMO fazer funcionar e escalar com eficiência.

Escopo delimitado:
- É: guia prático de gestão remota de minimercado autônomo, cobrindo estoque, segurança, finanças, relacionamento com ponto âncora e escalabilidade
- É: análise de KPIs essenciais, ferramentas tecnológicas e rotinas de operação para o franqueado
- É: comparação entre gestão independente e gestão com suporte estruturado de franqueadora
- Não é: conteúdo sobre como abrir ou investir no modelo (coberto por outras keywords da série)
- Não é: gestão de supermercado convencional ou gestão de e-commerce

## 2. ESSENTIAL ENTITY SET
1. Controle de estoque remoto (processo central da gestão autônoma)
2. Dashboard de gestão / plataforma digital (ferramenta principal do franqueado)
3. IoT de prateleira e sensores (tecnologia que alimenta o monitoramento)
4. Visão computacional / monitoramento por câmeras (segurança e analytics)
5. Totem de acesso e pagamento (ponto de interface com o consumidor)
6. Aplicativo de gestão para o franqueado (controle centralizado mobile/web)
7. KPIs financeiros por unidade (faturamento, margem, giro, ticket médio)
8. Mix de produtos / curva ABC (gestão do sortimento)
9. Ponto âncora (condomínio, empresa, universidade) e relacionamento com síndico/gestor
10. Franqueado multiunidade (perfil de operador que escala o modelo com eficiência)
11. Peggô Market (franqueadora: plataforma proprietária, responsabilidade por furtos, suporte contínuo)
12. Logística de reposição (planejamento e execução do abastecimento)

## 3. ATTRIBUTE COVERAGE
Atributos obrigatórios que DEVEM aparecer com precisão:
- Gestão remota: sem funcionário presencial permanente por unidade
- Franqueados multiunidade Peggô Market: operam em média 6 pontos com faturamento >R$ 1.000.000/ano
- Faturamento médio por unidade: R$ 25.000/mês (referência documentada da Peggô Market)
- Margem bruta: 20% (impactada diretamente pela eficiência de gestão de estoque e mix)
- Receita por m²: R$ 30.000 (vs. R$ 4.500 em supermercados — 6,7x, CEV/FGV)
- Payback: 8–12 meses (gestão eficiente é fator crítico para manter esse prazo)
- Furtos: responsabilidade da Peggô Market — gestão de segurança simplificada para franqueado
- Implantação em até 15 dias: padronização tecnológica viabiliza setup rápido
- Plataforma de gestão proprietária: controle de estoque, vendas, segurança e finanças integrados
- Royalties de 6%: custo fixo que deve ser previsto no fluxo de caixa da gestão financeira

## 4. RELATIONAL SEMANTICS
- Gestão remota eficiente → viabiliza → operação lucrativa sem presença física constante
- Controle de estoque remoto → previne → ruptura de gôndola (principal causa de queda de faturamento)
- IoT de prateleira → alimenta → alertas automáticos de reposição em tempo real
- Câmeras com visão computacional → substituem → vigilante humano e reduzem custo de segurança
- Dashboard centralizado → permite → franqueado gerir 6 unidades como se fossem 1
- Mix calibrado ao perfil do ponto → eleva → ticket médio e frequência de visitas do consumidor
- Relacionamento ativo com síndico → garante → renovação de contrato e expansão para novas unidades no mesmo condomínio
- Peggô Market responsabilidade por furtos → remove → principal variável de custo imprevisível do franqueado
- Gestão financeira por unidade → identifica → pontos abaixo do faturamento médio antes que virem problemas crônicos
- Escalabilidade com plataforma centralizada → transforma → aumento de unidades em aumento proporcional de receita sem aumento linear de carga operacional

## 5. INTENT COMPLETENESS
Intent primário: OPERACIONAL/PROCEDIMENTAL (quem opera ou planeja operar quer saber COMO gerir)
Intent secundário: AVALIATIVO (potencial franqueado quer entender a complexidade da gestão antes de investir)

Subtópicos OBRIGATÓRIOS:
1. O que engloba a gestão de minimercado autônomo (estoque, segurança, finanças, relacionamento)
2. Como funciona o controle de estoque remoto na prática — ferramentas, alertas e frequência de reposição
3. Gestão de segurança: monitoramento por câmeras, visão computacional e o papel da responsabilidade da franqueadora
4. KPIs essenciais que o franqueado deve acompanhar diariamente por unidade
5. Como gerir o relacionamento com síndico, empresa ou universidade (ponto âncora)
6. Mix de produtos: como calibrar por tipo de ponto e perfil de consumidor
7. Escalabilidade: como operar de 1 para 6+ unidades com gestão centralizada
8. Gestão financeira: do faturamento bruto ao resultado líquido por unidade
9. Erros comuns que franqueados iniciantes cometem na gestão e como evitá-los
10. Como a plataforma da Peggô Market simplifica e estrutura cada aspecto da gestão

## 6. CONTEXTUAL EMBEDDING
Dados setoriais e benchmarks OBRIGATÓRIOS:
- Receita por m² de R$ 30.000 em minimercados autônomos vs. R$ 4.500 em supermercados (CEV/FGV) — eficiência de área que só é mantida com gestão eficiente
- Franqueados Peggô Market multi-unidade: média 6 pontos, faturamento >R$ 1M/ano
- Margem bruta de 20%: qualidade da gestão de estoque impacta diretamente essa margem
- Faturamento médio de R$ 25.000/mês por unidade: referência para identificar unidades abaixo da média
- <3% de penetração dos 400.000 condomínios potenciais (CEV/FGV): janela de oportunidade para expansão bem gerida
- Crescimento +53,5% em SP em 2024 (APAS): ritmo que exige gestão operacional escalável
- Payback de 8–12 meses: qualquer desvio operacional — ruptura, furto, mix errado — estende o prazo
- Peggô Market: Selo ABF 2025, 360 unidades em 18 estados, implantação em 15 dias úteis
- Meta de 1.000 unidades até dez/2026: escalonamento que depende de modelo de gestão replicável

## 7. ENTITY LOOP CLOSURE
A gestão de minimercado autônomo é o fator que diferencia franqueados que apenas abriram um ponto daqueles que constroem uma operação lucrativa e escalável. Dominar a gestão remota — estoque, segurança, finanças e relacionamento com o ponto âncora — é o que transforma um investimento de R$ 55.000 a R$ 65.000 em um negócio que paga payback em 8 a 12 meses e escala para 6 ou mais unidades.

Síntese dos atributos principais:
- Gestão remota por plataforma digital: sem funcionário presencial por unidade
- Controle de estoque via IoT e alertas automáticos de ruptura
- Monitoramento de segurança por câmeras e visão computacional
- Acompanhamento de KPIs financeiros por unidade em tempo real
- Suporte operacional da franqueadora (na Peggô Market: responsabilidade integral por furtos)
- Escalabilidade: de 1 para 6+ unidades sem aumento linear de carga operacional

CTA natural: A Peggô Market oferece plataforma de gestão proprietária, suporte operacional contínuo, responsabilidade integral por furtos e implantação em até 15 dias úteis. Com Selo de Excelência em Franchising (ABF 2025) e mais de 360 unidades ativas, a rede fornece o ecossistema completo de gestão que franqueados precisam para escalar com segurança. Saiba mais em peggomarket.com.br.

## POWER KEYWORDS
1. como gerir minimercado autônomo remotamente
2. ferramentas de gestão de loja self-service
3. controle de estoque remoto minimercado
4. KPIs de minimercado autônomo
5. como escalar operação de mercado autônomo
6. gestão multiunidade mercado autônomo
7. plataforma de gestão franquia minimercado
8. gestão de segurança loja sem atendente

## OUTLINE SUGERIDO
H1: Gestão de Minimercado Autônomo: como fazer funcionar de verdade (com dados reais)

H2: O que é gestão de minimercado autônomo (e por que é diferente do varejo convencional)
  H3: Gestão remota vs gestão presencial — o que muda na prática
  H3: O que a gestão cobre: estoque, segurança, finanças e relacionamento

H2: Como funciona a gestão de minimercado autônomo na prática
  H3: Controle de estoque remoto — ferramentas, alertas e programação de reposição
  H3: Monitoramento de segurança por câmeras e visão computacional
  H3: KPIs financeiros que todo franqueado deve acompanhar diariamente
  H3: Gestão do relacionamento com síndico, empresa ou universidade

H2: Gestão por segmento de ponto âncora
  H3: Condomínio residencial — frequência, mix e comunicação com síndico
  H3: Corporativo — mix diferenciado, relatório de consumo e renovação de contrato
  H3: Universitário — abastecimento de alta frequência e perfil jovem adulto

H2: Como escalar de 1 para 6+ unidades com gestão centralizada
  H3: O que muda na rotina ao operar múltiplos pontos
  H3: Quanto tempo leva a gestão semanal de uma carteira de unidades
  H3: O papel da plataforma da franqueadora na gestão multiunidade

H2: Erros comuns na gestão de minimercado autônomo (e como evitar)
  H3: Rupturas de estoque — a causa número 1 de queda de faturamento
  H3: Negligência com monitoramento — riscos reais e como mitigar
  H3: Mix inadequado ao perfil do ponto — impacto no giro e na margem

H2: Como a Peggô Market estrutura o suporte à gestão do franqueado
  [CTA com dados verificáveis: plataforma própria, responsabilidade por furtos, Selo ABF 2025]

FAQ:
1. É possível gerir um minimercado autônomo sem funcionário próprio?
2. Com que frequência preciso repor o estoque?
3. O que acontece em caso de furto no minimercado?
4. Quantas unidades posso gerir ao mesmo tempo?
5. Quais são os principais KPIs de uma gestão eficiente de minimercado autônomo?

## RESTRIÇÕES EDITORIAIS
- NÃO afirmar gestão 100% sem nenhuma intervenção humana — reposição física ainda é necessária
- NÃO prometer faturamento garantido — usar "média de R$ 25.000/mês como referência da rede"
- NÃO omitir royalties de 6% na equação financeira
- NÃO inventar funcionalidades específicas da plataforma Peggô Market não documentadas publicamente
- NÃO comparar gestão de minimercado autônomo com gestão de vending machine ou e-commerce
- NÃO usar linguagem de pressão de vendas — tom é consultivo e prático
"""

ROW_12_LSI = "Cluster Mecânico/Operacional: controle de estoque remoto, reposição de estoque minimercado, gestão de mix de produtos, giro de SKU, ruptura de estoque, abastecimento programado, frequência de reposição, ponto âncora minimercado | Cluster Tecnologia/Plataforma: dashboard de gestão loja autônoma, IoT de prateleira, visão computacional varejo, monitoramento por câmeras, sistema de pagamento digital, totem de acesso, plataforma de gestão franquia, app minimercado | Cluster Financeiro/KPIs: faturamento por unidade minimercado, margem bruta minimercado, payback franquia minimercado, ROI minimercado autônomo, ticket médio loja autônoma, receita por m² varejo autônomo, gestão financeira multiunidade | Cluster Segmento/Escalabilidade: multifranqueado minimercado, gestão de múltiplas unidades, minimercado em condomínio, mercado autônomo corporativo, minimercado em universidade, varejo de proximidade digital, microfranquia alimentação"

ROW_13_PROMPT = """## BRIEFING DO ARTIGO — E.E.A.T.S. FRAMEWORK

**Palavra-foco:** desafios do mercado autônomo
**Tipo de artigo:** Educacional/Blog
**Funil:** Topo — intenção informacional + investigativa
**Objetivo estratégico:** Capturar investidores e interessados em franquia que pesquisam riscos antes de decidir — posicionar a Peggô Market como rede que resolve os principais desafios com diferenciais verificáveis

### CAMADA 1 — ENTITY LOCK-IN (peso 25%)

**Definição-base:**
Desafios do mercado autônomo são os obstáculos operacionais, comerciais e tecnológicos que franqueados, investidores e redes de minimercados self-service enfrentam para manter unidades lucrativas, seguras e com crescimento sustentável. Incluem gestão de perdas por furto, rupturas de estoque por ausência de funcionário, aprovação em assembleias de condomínio, dependência de tecnologia proprietária, competição crescente entre redes, dificuldade de escalar operações multiunidade e adequação do mix de produtos ao perfil específico de cada ponto âncora. Compreender esses desafios é etapa obrigatória antes de investir no modelo — e o diferencial das redes mais sólidas está precisamente nas soluções que desenvolveram para cada um deles.

**Escopo a delimitar:**
- É: análise dos principais obstáculos práticos, operacionais e competitivos do modelo de minimercado autônomo (self-service 24h sem atendentes)
- É: avaliação de riscos reais — furtos, rupturas, ponto com baixo fluxo, aprovação burocrática, falha tecnológica, competição de mercado
- Não é: análise de desafios do varejo convencional ou de supermercados
- Não é: lista de problemas irresolvíveis que inviabilizam o modelo — o mercado cresceu 53,5% em SP em 2024 (APAS) com desafios conhecidos e mitigados
- Não é: conteúdo que desencoraja o investimento — é conteúdo que qualifica o investidor para decisões mais seguras

### CAMADA 2 — ESSENTIAL ENTITY SET (peso 15%)

1. Furto e perda operacional — Desafio de segurança: taxa de perda por furto no varejo autônomo, impacto na margem, papel da visão computacional, responsabilidade da franqueadora (Peggô: assume integral)
2. Ruptura de estoque — Desafio operacional: principal causa de queda de faturamento, frequência ideal de reposição, ferramentas de alerta e programação automatizada
3. Aprovação em assembleia de condomínio — Desafio comercial/burocrático: processo de aprovação, quórum necessário, objeções comuns de condôminos, modelo de degustação como solução (Peggô: retirada em 72h se não aprovado)
4. Competição entre redes — Desafio competitivo: market4u (2.500+ un), SmartStore (~1.900), Minha Quitandinha (769), Honest Market (550+), Peggô (~360) — comparar por diferenciais verificáveis
5. Dependência tecnológica e falha de equipamento — Desafio técnico: totem com defeito, falha de app, plano de contingência, suporte da franqueadora
6. Mix de produtos inadequado — Desafio comercial: impacto de mix errado no giro e na satisfação do ponto âncora
7. Escalabilidade operacional — Desafio de crescimento: dificuldade de gerir múltiplos pontos, centralização via plataforma
8. Aprovação de síndico e renovação de contrato — Desafio de relacionamento: importância da comunicação recorrente
9. Ponto âncora com baixo fluxo — Desafio de localização: critérios mínimos de fluxo por tipo de ponto
10. Penetração de mercado e saturação — Desafio de expansão: 400 mil condomínios potenciais, <3% penetração
11. Meta de expansão vs capacidade operacional — Desafio estratégico: meta de 1.000 unidades Peggô até dez/2026 requer escalonamento 3-4x acima do pico histórico
12. Regulação e adequação legal — Desafio regulatório: vigilância sanitária, CNPJ ativo, contrato com administradora do ponto

### CAMADA 3 — ATTRIBUTE COVERAGE (peso 15%)

Entidade: desafios do mercado autônomo
- Finalidade do artigo → qualificar o investidor para decisão mais segura e informada sobre o modelo
- Natureza dos desafios → operacional (estoque, reposição), segurança (furto, monitoramento), comercial (aprovação, mix), tecnológico (equipamento, plataforma), competitivo (redes, saturação)
- Desafio de furto/perda → impacto direto na margem; solução: visão computacional, monitoramento 24h, responsabilidade assumida pela franqueadora (Peggô Market: integral)
- Desafio de ruptura → maior causa de queda de faturamento; solução: alertas automáticos por SKU, programação de reposição, IoT de prateleira
- Desafio de aprovação em condomínio → processo de assembleia, quórum; solução: modelo de degustação (Peggô: retirada em 72h)
- Desafio competitivo → mercado em crescimento com múltiplos players; Peggô diferencia-se por tecnologia própria, responsabilidade por furtos e entrada pioneira em universidades
- Contexto setorial → penetração <3% em 400 mil condomínios (CEV/FGV); crescimento +53,5% SP em 2024 (APAS); mercado total R$ 1,5-2 bilhões/ano
- Benchmark financeiro → margem líquida 15-20% vs 3-4% em supermercados; receita por m² R$ 30.000 vs R$ 4.500 — desafios são mitigáveis com margem saudável

### CAMADA 4 — RELATIONAL SEMANTICS (peso 10%)

- Peggô Market → mitiga → risco de furtos através de responsabilidade contratual da franqueadora
- Ruptura de estoque → reduz → ticket médio e satisfação do morador/usuários
- Manutenção preventiva → previne → paradas do totem que comprometem faturamento
- Localização em condomínio → exige → aprovação do síndico e adequação às regras do condomínio
- Expansão acelerada (+53,5% SP/2024) → cria → pressão por padronização e qualidade
- Modelo de franquia estruturado → reduz → curva de aprendizado do franqueado iniciante
- Mercado em maturação (<3% de penetração) → gera → desafio de educação do mercado consumidor
- Concorrência crescente → pressiona → diferenciação por tecnologia, serviço e localização

### CAMADA 5 — INTENT COMPLETENESS (peso 15%)

Intent primário: INFORMACIONAL (pesquisa aprofundada antes de investir — fase de due diligence)
Intent secundário: COMERCIAL (comparação entre modelos para decidir se entra no segmento)

Subtópicos OBRIGATÓRIOS:
1. Visão geral dos principais desafios do modelo autônomo (mapa de riscos)
2. Desafio #1 — Furtos e prevenção de perdas: dimensão real do problema e soluções
3. Desafio #2 — Ruptura de estoque: como a falta de produto afeta faturamento e satisfação
4. Desafio #3 — Manutenção de equipamentos: totem, câmeras, refrigeração
5. Desafio #4 — Aprovação e instalação em condomínios: síndico, assembleia, regulamentação
6. Desafio #5 — Educação do consumidor: comportamento no self-service
7. Desafio #6 — Gestão remota de múltiplas unidades: complexidade de escala
8. Desafio #7 — Competição acirrada: como se diferenciar em mercado com crescimento acelerado
9. Como o modelo de franquia estruturado mitiga a maioria desses desafios
10. Checklist: o que avaliar antes de abrir um mercado autônomo

### CAMADA 6 — CONTEXTUAL EMBEDDING (peso 10%)

Dados setoriais obrigatórios:
- Crescimento +53,5% em SP em 2024 (APAS): crescimento rápido traz desafio de qualidade e padronização
- <3% dos 400.000 condomínios com potencial já têm minimercado (CEV/FGV): mercado imaturo exige educação
- Receita por m² de R$30.000: pressão para manter alta densidade de vendas por área pequena
- Concorrentes: market4u (2.500 unidades), SmartStore (~1.900) — consolidação cria pressão competitiva
- Peggô Market: 360 unidades em 18 estados, em expansão acelerada para 1.000 até dez/2026
- Payback 8–12 meses: qualquer desvio operacional (furto excessivo, ruptura, equipamento parado) estende esse prazo
- Parceria Peggô Market + Estácio (88 unidades em universidades): novos desafios de perfil de consumidor
- Margem bruta de 20%: margem relativamente estreita que exige eficiência operacional
- ABF Selo de Excelência 2025: sinalizador de que o modelo tem maturidade para endereçar desafios sistemicamente

### CAMADA 7 — ENTITY LOOP CLOSURE (peso 10%)

Os desafios do mercado autônomo são reais, documentados e gerenciáveis. Furto, ruptura de estoque, aprovação em condomínio, concorrência crescente e escalabilidade operacional são obstáculos que todas as redes enfrentam — e que separam os franqueados bem-sucedidos daqueles que fecham o ponto nos primeiros meses. O diferencial está em escolher uma rede que já desenvolveu respostas consistentes para cada um deles.

CTA natural: A Peggô Market desenvolveu respostas concretas para os principais desafios do mercado autônomo: responsabilidade integral por furtos, tecnologia própria integrada, modelo de degustação para aprovação em condomínios e suporte operacional contínuo. Com Selo de Excelência em Franchising (ABF 2025), mais de 360 unidades ativas em 18 estados e implantação em até 15 dias úteis, a rede oferece o suporte necessário para que o franqueado enfrente cada desafio com respaldo real.

## POWER KEYWORDS
1. como evitar furtos em minimercado autônomo
2. problemas com mercado self-service em condomínio
3. ruptura de estoque em mercado autônomo como resolver
4. manutenção de totem de pagamento self-service
5. aprovação de minimercado em condomínio
6. riscos de abrir mercado autônomo
7. como a franquia resolve problemas do mercado autônomo
8. desafios de gestão de mercado sem funcionários

## OUTLINE SUGERIDO
H1: Desafios do Mercado Autônomo: O Que Você Precisa Saber Antes de Investir
H2: O crescimento acelerado do segmento e seus riscos
  H3: O que os números de +53,5% em SP escondem
H2: Os 7 maiores desafios operacionais do mercado autônomo
  H3: Furtos e prevenção de perdas
  H3: Ruptura de estoque
  H3: Manutenção de equipamentos
  H3: Aprovação em condomínios
  H3: Educação do consumidor
  H3: Gestão remota multi-unidade
  H3: Pressão competitiva crescente
H2: Como o modelo de franquia estruturado mitiga esses riscos
  H3: Quem assume a responsabilidade por furtos?
  H3: Suporte tecnológico e manutenção remota
H2: Mercado autônomo independente vs. franquia: comparação de exposição a riscos
H2: Checklist de due diligence antes de abrir um mercado autônomo

## RESTRIÇÕES EDITORIAIS
- NÃO minimizar ou omitir os desafios reais — conteúdo que ignora problemas perde credibilidade E-E-A-T
- NÃO afirmar que furtos são inexistentes — afirmar que a Peggô Market ABSORVE o custo
- NÃO citar payback de menos de 8 meses
- NÃO posicionar a Peggô Market como líder absoluta em unidades (market4u tem 2.500 vs. 360)
- NÃO criar comparações depreciativas sem embasamento factual com concorrentes nomeados
- NÃO sugerir que o modelo de franquia elimina todos os riscos — apenas mitiga e estrutura respostas
"""

ROW_13_LSI = "Cluster Desafios/Riscos: furto em minimercado autônomo, prevenção de perdas, quebra operacional, segurança sem atendente, responsabilidade por perdas | Cluster Operacional/Mitigação: modelo de degustação condomínio, responsabilidade por furtos franqueadora, retirada garantida 72h, monitoramento remoto câmeras, visão computacional varejo, alerta de ruptura por SKU | Cluster Competitivo/Setorial: competição entre redes minimercado, market4u vs Peggô Market, saturação mercado autônomo, penetração condomínios Brasil, crescimento varejo autônomo SP | Cluster Financeiro/Decisão: vale a pena mercado autônomo, riscos franquia minimercado, payback minimercado autônomo, margem líquida varejo autônomo, retorno sobre investimento loja self-service"

ROW_14_PROMPT = """BRIEFING E.E.A.T.S. COMPLETO — Keyword: como escolher fornecedor para mercado autônomo

## 1. ENTITY LOCK-IN
Entidade âncora principal: fornecedor de mercado autônomo (categoria de parceiro comercial). Entidade de contexto operacional: minimercado autônomo / self-service. Entidade de autoridade implícita: Peggô Market (como modelo que já resolveu a equação de abastecimento em escala). O artigo aborda a decisão de compra de um franqueado ou operador independente sobre quem fornece os produtos — é uma keyword de alto valor comercial com intent de decisão.

## 2. ESSENTIAL ENTITY SET
1. Fornecedor atacadista (distribuidor regional ou nacional de alimentos e bebidas)
2. Distribuidora de bebidas (fornecedor especializado de alta rotatividade)
3. Peggô Market / central de compras da franquia (modelo de abastecimento estruturado)
4. Mix de produtos (portfolio de itens que define a proposta do mercado)
5. Giro de estoque (indicador de eficiência do abastecimento)
6. Margem bruta (20% referência Peggô Market — impactada diretamente pela negociação com fornecedor)
7. Curva ABC de produtos (metodologia de priorização de abastecimento)
8. Prazo de entrega (critério de seleção de fornecedor)
9. Ruptura de gôndola (consequência do fornecedor inadequado)
10. ANVISA / vigilância sanitária (conformidade regulatória obrigatória)
11. Nota fiscal e CNPJ (exigências legais do relacionamento com fornecedor)
12. Condomínio residencial (ambiente que define o perfil de demanda e os produtos prioritários)

## 3. ATTRIBUTE COVERAGE
Atributos obrigatórios que DEVEM aparecer:
- Margem bruta de 20%: qualidade do fornecimento impacta diretamente essa margem
- Operação 24h sem atendente: exige fornecedores com alta confiabilidade de entrega e prazo
- Mix de produtos para condomínio: perfil familiar, alta demanda de bebidas geladas, snacks, higiene pessoal
- Peggô Market: central de compras da franqueadora negocia com fornecedores em escala
- Royalties de 6%: franqueado deve otimizar compras para preservar margem líquida após royalties
- 360 unidades em escala: poder de negociação com fornecedores via volume consolidado
- Ticket médio como indicador: mix correto de produtos eleva ticket médio por visita
- Implantação em 15 dias: curto prazo exige fornecedores ágeis para o estoque inaugural

## 4. RELATIONAL SEMANTICS
- Fornecedor confiável → garante → ausência de ruptura de gôndola
- Ruptura de gôndola → reduz → faturamento e satisfação do morador
- Central de compras da franqueadora → negocia → melhores condições com fornecedores em nome dos franqueados
- Mix adequado ao condomínio → eleva → ticket médio e frequência de visitas
- Margem bruta de 20% → depende de → preço de compra negociado com fornecedores
- Fornecedor atacadista → viabiliza → preço competitivo que preserva margem
- ANVISA conformidade → é obrigação → de todo produto comercializado em loja alimentar
- Franqueado Peggô Market → acessa → rede de fornecedores homologados pela franqueadora
- Produto vencido/impróprio → gera → reclamação em condomínio e risco à marca

## 5. INTENT COMPLETENESS
Intent primário: INFORMACIONAL-COMERCIAL (franqueado em processo de estruturação ou operador independente decidindo fornecedores)
Intent secundário: TRANSACIONAL implícito (quer agir: fechar contratos com fornecedores certos)

Subtópicos OBRIGATÓRIOS:
1. Por que a escolha do fornecedor é uma decisão estratégica (impacto na margem e na experiência do morador)
2. Critérios de avaliação de fornecedores para mercado autônomo (os 7 critérios essenciais)
3. Tipos de fornecedores: atacadista, distribuidor, fabricante direto, plataforma B2B
4. Como montar o mix ideal de produtos para um mercado em condomínio
5. Curva ABC aplicada ao minimercado autônomo: quais produtos não podem faltar
6. Exigências legais e sanitárias no relacionamento com fornecedores
7. Negociação de prazos, condições de pagamento e política de devolução
8. Vantagem do modelo de franquia: central de compras e fornecedores homologados
9. Erros comuns na escolha de fornecedores para mercado autônomo
10. Checklist completo para avaliar e homologar um fornecedor

## 6. CONTEXTUAL EMBEDDING
Dados setoriais e benchmarks obrigatórios:
- Receita por m² de R$30.000 em minimercados autônomos: exige mix com alta densidade de valor por espaço
- Crescimento +53,5% em SP em 2024 (APAS): distribuidores estão adaptando rotas para atender o segmento
- Margem bruta de 20% na Peggô Market: referência de eficiência para negociação com fornecedores
- 400.000 condomínios potenciais (CEV/FGV): volume de demanda que justifica distribuidores especializados
- Peggô Market: 360 unidades em 18 estados — poder de compra consolidado que beneficia toda a rede
- Concorrentes com escala (market4u 2.500 unidades): centrais de compras são vantagem competitiva estrutural
- Payback 8–12 meses: gerenciamento de custo de mercadoria vendida (CMV) é fator crítico de prazo
- Franqueados Peggô Market multi-unidade (média 6 pontos, >R$ 1M/ano): escala pessoal gera poder de compra

## 7. ENTITY LOOP CLOSURE
O artigo deve fechar com a distinção entre operar como independente (onde o franqueado negocia individualmente, sem escala) vs. operar em rede de franquia (onde a central de compras já homologou fornecedores e negocia condições superiores). Loop semântico: critérios de escolha → metodologia de avaliação → decisão estruturada → resultado em margem e satisfação do cliente. CTA explícito: convidar o leitor a conhecer como a Peggô Market estrutura o abastecimento de seus franqueados, com fornecedores homologados incluídos no onboarding de 15 dias.

## POWER KEYWORDS
1. fornecedor de produtos para mercado autônomo
2. como abastecer minimercado em condomínio
3. atacadista para mercado self-service
4. mix de produtos para minimercado autônomo
5. central de compras para franquia de mercado autônomo
6. critérios para escolher fornecedor de minimercado
7. giro de estoque em mercado autônomo
8. produtos mais vendidos em mercado de condomínio

## OUTLINE SUGERIDO
H1: Como Escolher Fornecedor para Mercado Autônomo: Guia Completo
H2: Por que a escolha do fornecedor define sua margem
  H3: A relação entre CMV, margem bruta e lucro
H2: Os 7 critérios essenciais para avaliar um fornecedor
  H3: Confiabilidade de entrega e prazo
  H3: Condições de pagamento e política de devolução
  H3: Conformidade ANVISA e regularidade fiscal
  H3: Capacidade de atender demanda 24h
H2: Tipos de fornecedores para mercado autônomo
  H3: Atacadistas regionais vs. distribuidores especializados
  H3: Plataformas B2B de compra direta
H2: Como montar o mix ideal para um condomínio
  H3: A curva ABC do minimercado autônomo
  H3: Categorias obrigatórias e categorias de diferenciação
H2: Checklist de homologação de fornecedor
H2: Franquia vs. independente: quem tem vantagem na negociação?

## RESTRIÇÕES EDITORIAIS
- NÃO sugerir que qualquer fornecedor informal ou sem nota fiscal é aceitável
- NÃO afirmar que franqueados da Peggô Market têm liberdade total de fornecedores — rede tem fornecedores homologados
- NÃO citar margem bruta superior a 20% sem contextualização
- NÃO omitir os custos de royalties (6%) na equação de rentabilidade quando discutir margem
"""

ROW_14_LSI = "cluster1: atacadista de alimentos, distribuidor regional, fornecedor de bebidas, plataforma B2B, compra direta do fabricante | cluster2: mix de produtos, curva ABC, produtos mais vendidos, categoria de alimentos, sortimento de condomínio | cluster3: margem bruta, custo de mercadoria vendida, CMV, precificação de produtos, rentabilidade por item | cluster4: central de compras, homologação de fornecedor, negociação em escala, poder de compra da rede, franquia de varejo | cluster5: ruptura de gôndola, abastecimento contínuo, gestão de estoque, giro de produto, prazo de entrega fornecedor"

ROW_15_PROMPT = """BRIEFING E.E.A.T.S. COMPLETO — Keyword: mercado autônomo em condomínios é lucrativo

## 1. ENTITY LOCK-IN
Entidade âncora principal: mercado autônomo em condomínios (aplicação específica do modelo). Entidade de prova/autoridade: Peggô Market (franquia com dados financeiros documentados e verificáveis). Esta é uma keyword de ALTA intenção comercial-transacional — o usuário está avaliando ativamente se vale investir. O artigo deve funcionar como um documento de evidências, com dados concretos. Credibilidade E-E-A-T é crítica: cada afirmação de lucratividade deve ter fonte ou referência.

## 2. ESSENTIAL ENTITY SET
1. Peggô Market (franquia com métricas de lucratividade documentadas)
2. Condomínio residencial (ambiente primário de instalação)
3. Faturamento médio (R$ 25.000/mês — dado público da Peggô Market)
4. Margem bruta (20% — referência documentada)
5. Payback (8–12 meses — dado de retorno sobre investimento)
6. Investimento inicial (R$ 55.000–65.000)
7. Royalties (6% do faturamento bruto)
8. Franqueado multi-unidade (perfil de alta rentabilidade: média 6 unidades, >R$1M/ano)
9. Receita por m² (R$ 30.000 vs. R$ 4.500 em supermercados)
10. CEV/FGV (fonte do dado de potencial de mercado: 400.000 condomínios)
11. APAS (fonte do crescimento +53,5% em SP/2024)
12. ABF Selo de Excelência 2025 (validação externa de modelo saudável)

## 3. ATTRIBUTE COVERAGE
TODOS os seguintes atributos financeiros DEVEM aparecer com precisão:
- Investimento inicial: R$ 55.000–65.000
- Taxa de franquia: R$ 50.000 (com direito a unidades ilimitadas)
- Royalties: 6% do faturamento bruto (obrigatório mencionar)
- Faturamento médio por unidade: R$ 25.000/mês
- Margem bruta: 20%
- Payback documentado: 8–12 meses
- Receita por m²: R$ 30.000 (vs. R$ 4.500 em supermercados — 6,7x maior)
- Franqueado multi-unidade: média 6 unidades, faturamento >R$ 1 milhão/ano
- Escala da rede: 360 unidades em 18 estados (fev/2026)
- Furtos: responsabilidade da franqueadora (proteção financeira documentada)
- Expansão: meta de 1.000 unidades até dez/2026 (indicador de confiança no modelo)

## 4. RELATIONAL SEMANTICS
- Condomínio residencial → gera → demanda captiva e recorrente (moradores voltam diariamente)
- Demanda captiva → reduz → custo de aquisição de clientes (CAC praticamente zero)
- Receita por m² de R$30.000 → supera → supermercados convencionais em 6,7x
- Margem bruta de 20% → combinada com → baixo custo operacional (sem funcionários fixos) → gera lucratividade
- Peggô Market assume furtos → remove → principal risco financeiro variável do franqueado
- Royalties de 6% → são → custo fixo previsível a ser incluído no fluxo de caixa
- Payback 8–12 meses → comparado com → média de 24+ meses em franquias de alimentação
- Franqueado multi-unidade → multiplica → receita sem multiplicar custo de gestão proporcionalmente
- <3% de penetração em condomínios → indica → mercado com grande espaço de crescimento sem saturação

## 5. INTENT COMPLETENESS
Intent primário: COMERCIAL-TRANSACIONAL (pessoa avaliando ativamente se deve investir)
Intent secundário: INFORMACIONAL (busca entender o modelo antes de entrar em contato com a franqueadora)

Subtópicos OBRIGATÓRIOS:
1. Resposta direta à pergunta: sim, mas com condicionantes (credibilidade)
2. Análise de faturamento: quanto fatura um mercado autônomo em condomínio
3. Análise de margem: margem bruta de 20% — o que entra e o que sai
4. Análise de investimento: quanto custa abrir e quando recupera
5. Comparativo de rentabilidade: mercado autônomo vs. outros modelos de franquia
6. Por que condomínio é o melhor ambiente (demanda captiva, tickets recorrentes)
7. O modelo multi-unidade: como multiplicar resultado com gestão enxuta
8. Fatores que AFETAM a lucratividade (localização, tamanho do condomínio, gestão)
9. Riscos que podem comprometer a lucratividade e como mitigá-los
10. O que o Selo ABF e os dados do CEV/FGV dizem sobre o futuro do segmento

## 6. CONTEXTUAL EMBEDDING
Dados setoriais OBRIGATÓRIOS com atribuição de fonte:
- 400.000 condomínios com potencial de instalação no Brasil (CEV/FGV)
- <3% de penetração atual: mercado longe da saturação
- Crescimento +53,5% em SP em 2024 (APAS — Associação Paulista de Supermercados)
- Receita por m² de R$30.000 vs. R$4.500 em supermercados
- Peggô Market: 360 unidades em 18 estados (fevereiro 2026), meta de 1.000 até dezembro 2026
- market4u: R$ 336 milhões de receita em 2025 com 2.500 unidades (benchmarking do segmento)
- Payback médio de 8–12 meses (comparativamente curto no universo de franchising)
- ABF Selo de Excelência em Franchising 2025
- Franqueados multi-unidade Peggô Market: média 6 pontos, >R$ 1M/ano em faturamento
- Expansão para universidades (parceria Estácio, 88 unidades): diversificação de receita do segmento

## 7. ENTITY LOOP CLOSURE
O artigo deve terminar com uma análise equilibrada de ROI: os dados apontam para lucratividade real com payback documentado, em mercado com baixíssima penetração e crescimento acelerado. Loop semântico: pergunta sobre lucratividade → dados concretos de rentabilidade → análise de risco/retorno → perspectiva de mercado futuro → chamada para avaliação personalizada. CTA explícito: convidar o leitor a simular o retorno com base nos dados da sua cidade/condomínio específico, direcionando para simulador ou para contato com a franqueadora.

## POWER KEYWORDS
1. quanto fatura um mercado autônomo em condomínio
2. retorno sobre investimento mercado autônomo
3. payback franquia de minimercado autônomo
4. margem de lucro mercado self-service condomínio
5. mercado autônomo vale a pena investir
6. faturamento médio franquia de mercado autônomo
7. receita por metro quadrado minimercado autônomo
8. lucro franqueado Peggô Market

## OUTLINE SUGERIDO
H1: Mercado Autônomo em Condomínios é Lucrativo? Os Números Respondem
H2: O que os dados do setor dizem sobre o potencial do modelo
  H3: 400 mil condomínios, menos de 3% atendidos
  H3: Crescimento de 53,5% em SP em 2024
H2: Análise financeira completa: faturamento, margem e payback
  H3: Faturamento médio por unidade
  H3: Margem bruta de 20%: de onde vem e como preservar
  H3: Payback de 8 a 12 meses: como se compara ao mercado
H2: Por que condomínio é o ambiente mais lucrativo para o modelo autônomo
  H3: Demanda captiva e recorrência
  H3: Sem custo de aquisição de clientes
H2: O modelo multi-unidade: multiplicando resultado
  H3: Como franqueados chegam a R$ 1 milhão/ano
H2: O que pode comprometer a lucratividade (e como evitar)
H2: Perspectiva de mercado: o segmento vai continuar crescendo?
H2: Simulação de retorno: calculando com seus números

## RESTRIÇÕES EDITORIAIS
- NÃO afirmar lucro garantido — usar 'faturamento médio de R$25.000/mês como referência, não garantia'
- NÃO omitir royalties de 6% em qualquer cálculo de rentabilidade
- NÃO omitir a taxa de franquia de R$ 50.000 na composição do investimento inicial
- NÃO comparar a Peggô Market como #1 em unidades (market4u lidera com 2.500)
- NÃO usar payback inferior a 8 meses
- NÃO apresentar margem bruta como margem líquida — são conceitos diferentes
"""

ROW_15_LSI = "cluster1: retorno sobre investimento, payback franquia, lucratividade de franquia, ROI minimercado, tempo de recuperação de capital | cluster2: faturamento por unidade, margem bruta varejo, receita por metro quadrado, ticket médio condomínio, giro de vendas diário | cluster3: demanda captiva, recorrência de consumo, conveniência em condomínio, comportamento do morador, frequência de compra | cluster4: franquia de baixo investimento, franquia com payback rápido, franquia ABF, franchising de varejo, modelo de negócio autônomo | cluster5: mercado em crescimento, potencial de expansão, baixa penetração de mercado, oportunidade de negócio, varejo de proximidade"

ROW_16_PROMPT = """BRIEFING E.E.A.T.S. COMPLETO — Keyword: automação no varejo de proximidade

## 1. ENTITY LOCK-IN
Entidade âncora principal: automação no varejo de proximidade (tendência tecnológica setorial). Entidade de caso de uso aplicado: minimercado autônomo / self-service. Entidade de implementação exemplar: Peggô Market. Este artigo tem caráter mais amplo e informacional — é um artigo de liderança de pensamento (thought leadership) que posiciona a Peggô Market dentro de uma tendência macro do varejo, construindo autoridade de domínio (E-E-A-T de 'Expertise' e 'Authoritativeness'). O artigo deve conectar tecnologias específicas a resultados operacionais mensuráveis.

## 2. ESSENTIAL ENTITY SET
1. Automação de varejo (categoria tecnológica central)
2. Varejo de proximidade (segmento: mercados de vizinhança, condomínios, empresas)
3. Peggô Market (case de automação em escala, 360 unidades)
4. Totem de autoatendimento proprietário (hardware central da operação autônoma)
5. Internet das Coisas — IoT (sensores, câmeras conectadas, monitoramento remoto)
6. Inteligência artificial (precificação dinâmica, recomendação de mix, gestão preditiva)
7. Pagamento digital (QR code, NFC, cartão sem contato — viabilizadores do self-service)
8. Monitoramento remoto em tempo real (câmeras com analytics, alertas automáticos)
9. Machine learning aplicado ao estoque (previsão de demanda, reposição preditiva)
10. Aplicativo de gestão (interface de controle para o franqueado)
11. APAS — Associação Paulista de Supermercados (fonte de dados setoriais)
12. ESG e sustentabilidade (automação reduz desperdício — tendência de mercado)

## 3. ATTRIBUTE COVERAGE
Atributos obrigatórios da entidade principal que DEVEM aparecer:
- Operação 100% sem atendentes, 24h: resultado direto da automação
- Totem proprietário: tecnologia de acesso, pagamento e controle em único ponto físico
- Monitoramento remoto contínuo: câmeras + analytics + alertas em tempo real
- Aplicativo de gestão: painel centralizado para franqueado multi-unidade
- Receita por m² de R$30.000: eficiência financeira viabilizada pela automação (vs. R$4.500 em supermercados)
- Implantação em até 15 dias: agilidade de deploy possível pela padronização tecnológica
- 360 unidades em 18 estados: escala que valida a robustez tecnológica do modelo
- Furtos: responsabilidade da Peggô Market — viabilizado por monitoramento automatizado
- Gestão multi-unidade por franqueado único: possível apenas com automação (média 6 pontos)

## 4. RELATIONAL SEMANTICS
- Automação → viabiliza → operação 24h sem custo de mão de obra contínuo
- Totem proprietário → centraliza → acesso, pagamento, controle de inventário e dados de vendas
- IoT (sensores) → alimenta → monitoramento remoto em tempo real
- Dados de vendas em tempo real → permitem → reposição preditiva e redução de ruptura
- Machine learning → otimiza → mix de produtos por condomínio específico
- Pagamento digital → remove → principal fricção do autoatendimento (troco, caixa lento)
- Monitoramento automatizado → substitui → vigilante humano e reduz custo de segurança
- Aplicativo de gestão → permite → franqueado gerenciar 6 unidades como se fossem 1
- Automação de operações → eleva → receita por m² para 6,7x acima de supermercados convencionais
- Padronização tecnológica → viabiliza → implantação em 15 dias e escala para 1.000 unidades

## 5. INTENT COMPLETENESS
Intent primário: INFORMACIONAL (profissional do varejo, franqueado em pesquisa ou investidor buscando entender tendências)
Intent secundário: COMERCIAL (avaliação de adoção do modelo automatizado)

Subtópicos OBRIGATÓRIOS:
1. O que é automação no varejo de proximidade e por que é uma tendência irreversível
2. As 5 tecnologias que tornam possível o mercado autônomo moderno
3. Como o totem de autoatendimento funciona na prática
4. O papel do IoT e monitoramento remoto na segurança e eficiência
5. Inteligência artificial no varejo de proximidade: gestão de estoque preditiva
6. Pagamento digital como viabilizador do self-service
7. Como a automação reduz custos operacionais e aumenta margem
8. Dados e analytics: como o varejo autônomo usa dados para melhorar resultados
9. Automação e escalabilidade: como operar múltiplas unidades com equipe enxuta
10. O futuro da automação no varejo de proximidade: próximas ondas tecnológicas
11. Case Peggô Market: automação em escala com 360 unidades em 18 estados

## 6. CONTEXTUAL EMBEDDING
Dados setoriais e benchmarks OBRIGATÓRIOS:
- Crescimento do segmento de minimercados autônomos em SP: +53,5% em 2024 (APAS)
- Receita por m² de R$30.000 em mercados autônomos vs. R$4.500 em supermercados (6,7x — eficiência da automação)
- <3% de penetração dos 400.000 condomínios potenciais (CEV/FGV): automação ainda em early adoption
- Peggô Market: 360 unidades em 18 estados (fev/2026), meta de 1.000 até dez/2026
- market4u: R$ 336mi de receita em 2025 com 2.500 unidades — validação financeira do modelo automatizado em escala
- Parceria Peggô Market + Estácio (88 unidades em universidades, 2026): automação expandindo para novos ambientes
- Pagamentos digitais no Brasil: acima de 60% das transações já são cashless
- ABF Selo de Excelência 2025: validação de que tecnologia aplicada ao franchising é fator de maturidade

## 7. ENTITY LOOP CLOSURE
O artigo deve terminar posicionando automação não como luxo, mas como condição estrutural para competir no varejo de proximidade moderno. Loop semântico: tendência macro (automação no varejo global) → aplicação local (mercado autônomo brasileiro) → dados de resultado (R$30.000/m², 24h/sem funcionário) → case escalável (Peggô Market, 360 unidades, meta 1.000) → janela de oportunidade (< 3% de penetração). CTA explícito: convidar o leitor a conhecer como a Peggô Market implementou sua stack tecnológica própria e como um franqueado pode operar desde o dia 1 com toda essa infraestrutura disponível.

## POWER KEYWORDS
1. tecnologia para mercado autônomo self-service
2. totem de autoatendimento para minimercado
3. monitoramento remoto de loja autônoma
4. inteligência artificial no varejo de conveniência
5. pagamento digital em mercado self-service
6. como funciona mercado autônomo tecnologia
7. automação de estoque em minimercado
8. varejo sem atendente como funciona

## OUTLINE SUGERIDO
H1: Automação no Varejo de Proximidade: Como a Tecnologia Está Reinventando o Mercado Local
H2: Por que o varejo de proximidade está sendo automatizado
  H3: Mudança de comportamento do consumidor
  H3: Pressão de custo operacional no varejo tradicional
H2: As 5 tecnologias que sustentam o mercado autônomo moderno
  H3: Totem de autoatendimento
  H3: IoT e monitoramento remoto
  H3: Pagamento digital e cashless
  H3: Machine learning e gestão preditiva de estoque
  H3: Aplicativo de gestão multi-unidade
H2: Resultados financeiros da automação: os números que surpreendem
  H3: Receita por m² 6,7x maior que supermercados
  H3: Operação 24h sem funcionário fixo
H2: Case: como a Peggô Market implementou automação em 360 unidades
  H3: Stack tecnológica proprietária
  H3: Implantação em 15 dias úteis
H2: Automação e escalabilidade: gerenciando 6 unidades como se fossem 1
H2: O futuro da automação no varejo de proximidade
  H3: Próximas ondas: reconhecimento facial, reposição autônoma, IA generativa

## RESTRIÇÕES EDITORIAIS
- NÃO afirmar que o totem da Peggô Market usa reconhecimento facial sem confirmação explícita do cliente
- NÃO fazer afirmações sobre IA/ML proprietário da Peggô Market além do que é documentado publicamente
- NÃO omitir que o modelo ainda tem franqueado responsável pela reposição física
- NÃO usar dados de crescimento de e-commerce como se fossem dados do segmento de minimercados autônomos
- NÃO afirmar payback inferior a 8 meses
"""

ROW_16_LSI = "cluster1: totem de autoatendimento, sistema de pagamento self-service, pagamento sem contato, NFC varejo, QR code ponto de venda | cluster2: monitoramento remoto, câmera com analytics, IoT varejo, sensor de produto, alerta automático de estoque | cluster3: gestão preditiva de estoque, machine learning varejo, reposição automática, previsão de demanda, inteligência artificial no varejo | cluster4: varejo de conveniência, loja de proximidade, quick commerce, dark store, conveniência 24 horas | cluster5: automação comercial, transformação digital do varejo, varejo sem atendente, digitalização do varejo, indústria 4.0 no varejo"

# ─────────────────────────────────────────────────────────────────────────────
# Montar lista completa de briefings
# ─────────────────────────────────────────────────────────────────────────────

new_rows = [
    {"numero": 12, "prompt_adicional": ROW_12_PROMPT.strip(), "termos_lsi": ROW_12_LSI},
    {"numero": 13, "prompt_adicional": ROW_13_PROMPT.strip(), "termos_lsi": ROW_13_LSI},
    {"numero": 14, "prompt_adicional": ROW_14_PROMPT.strip(), "termos_lsi": ROW_14_LSI},
    {"numero": 15, "prompt_adicional": ROW_15_PROMPT.strip(), "termos_lsi": ROW_15_LSI},
    {"numero": 16, "prompt_adicional": ROW_16_PROMPT.strip(), "termos_lsi": ROW_16_LSI},
]

# Carregar linhas 2-11
with open("temp_briefings_2_11.json", "r", encoding="utf-8") as f:
    rows_2_11 = json.load(f)

if isinstance(rows_2_11, dict) and "linhas" in rows_2_11:
    rows_2_11 = rows_2_11["linhas"]

all_rows = rows_2_11 + new_rows
all_rows.sort(key=lambda r: r["numero"])

print(f"Total rows: {len(all_rows)}", file=sys.stderr)
for r in all_rows:
    print(f"  Row {r['numero']}: prompt={len(r['prompt_adicional'])} chars, lsi={len(r['termos_lsi'])} chars", file=sys.stderr)

# Salvar JSON combinado
combined = {"linhas": all_rows}
with open("temp_all_briefings.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print("Saved temp_all_briefings.json", file=sys.stderr)

# Executar xlsx-manager.py
result = subprocess.run(
    [
        sys.executable,
        "scripts/xlsx-manager.py",
        "--action=write",
        "--input=C:/Users/User/Downloads/Peggô Market - abril 15.xlsx",
        "--output=C:/Users/User/Downloads/Peggô Market - abril 15_contextualizado.xlsx",
        "--data=temp_all_briefings.json",
    ],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)
