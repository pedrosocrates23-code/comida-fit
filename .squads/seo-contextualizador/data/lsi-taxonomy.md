# LSI Taxonomy — Guia de Extração por Cluster

> Referência para @nebula e @atlas na categorização de termos LSI.

---

## Os 5 Clusters Padrão

### Cluster 1 — Regulatório (alta prioridade em nichos regulados)

**O que é:** Termos relacionados à conformidade legal, normas, regulamentação, órgãos competentes.

**Quando tem alta prioridade:**
- Nicho regulamentado por lei (promoções, saúde, finanças, alimentação, etc.)
- Keyword tem componente legal ou burocrático

**Exemplos universais:**
- autorização prévia, regulamentação vigente, órgão competente, conformidade legal
- base legal, legislação, decreto, portaria, norma, resolução
- fiscalização, responsabilidade legal, pessoa jurídica, contratante
- licença, permissão, autorizado, homologado

**Como identificar:**
- Aparece ao lado de nomes de leis, decretos, portarias no SERP
- Aparece em contexto de "precisa de" ou "é obrigatório"
- Aparece em sites .gov.br ou sites jurídicos

---

### Cluster 2 — Mecânico (alta prioridade)

**O que é:** Como a coisa funciona — processo, mecanismo, ferramentas, fluxo operacional.

**Quando tem alta prioridade:** Sempre — qualquer artigo explicativo

**Exemplos universais:**
- como funciona, passo a passo, processo, fluxo, etapas
- participação, cadastro, inscrição, número, código
- plataforma, sistema, ferramenta, tecnologia, interface
- extração, sorteio, resultado, ganhador, vencedor (para nichos de promoção)
- mecanismo, metodologia, protocolo, procedimento

**Como identificar:**
- Aparece em explicações de "como" fazer algo
- Associado a verbos de ação: cadastrar, inscrever, participar, enviar
- Em snippets de artigos "passo a passo"

---

### Cluster 3 — Risco/Conformidade (média prioridade)

**O que é:** Erros comuns, penalidades, riscos de não conformidade, irregularidades.

**Quando tem alta prioridade:**
- Artigos que precisam cobrir o aspecto de "o que acontece se não fizer certo"
- Keyword em nicho regulado

**Exemplos universais:**
- ilegal, irregular, não autorizado, sem autorização
- multa, penalidade, suspensão, embargo, sanção
- campanha suspensa, proibido, infração, irregularidade
- erro comum, armadilha, cuidado, atenção, risco
- prejudicado, dano, responsabilidade, consequência

**Como identificar:**
- Aparece em contextos de advertência ou cautela
- Associado a verbos: proibir, suspender, multar, autuar
- Em snippets sobre "o que evitar" ou "cuidados"

---

### Cluster 4 — Execução (média prioridade)

**O que é:** Como implementar na prática — fornecedores, estrutura, entrega, suporte.

**Quando tem alta prioridade:**
- Artigos de fundo de funil ou meio de funil
- Quando o cliente tem serviço de execução a oferecer

**Exemplos universais:**
- estrutura técnica, desenvolvimento, implementação, criação
- regulamento personalizado, hotsite, landing page, campanha
- fornecedor, empresa especializada, agência, parceiro
- dashboard, monitoramento, relatório, métricas, dados
- suporte, hospedagem, manutenção, atualização

**Como identificar:**
- Aparece em contextos de "como contratar" ou "quem faz"
- Associado a serviços específicos do nicho
- Em páginas de fornecedores ou comparativos de serviços

---

### Cluster 5 — Comercial/Conversão (baixa prioridade — só em seções CTA)

**O que é:** Termos de intenção comercial, compra, contratação.

**Quando usar:**
- Apenas nas seções de CTA do artigo
- Não usar no corpo principal (parece forçado e prejudica E-E-A-T)

**Exemplos universais:**
- como contratar, orçamento, preço, investimento
- empresa confiável, especialista, expertise, experiência
- casos de sucesso, portfólio, clientes, referências
- fale conosco, entre em contato, solicitar proposta

---

## Regras de Extração

### Do SERP (via @nebula)

1. Ler snippets dos top 10 resultados para a keyword
2. Extrair substantivos e expressões nominais relevantes (não stop words)
3. Classificar em qual cluster cada termo pertence
4. Só incluir se aparecer em ≥2 resultados OU for termo técnico verificável do nicho

### Validação de qualidade

**Incluir:**
- Termos técnicos específicos do nicho
- Entidades nomeadas (nomes de leis, órgãos, etc.)
- Termos de ação relevantes para o processo
- Termos de qualidade/resultado específicos

**Excluir:**
- Palavras genéricas de qualquer texto ("importante", "empresa", "solução")
- Stop words ("de", "para", "com", "por")
- A própria keyword exata (isso é a keyword principal, não LSI)
- Termos proibidos do cliente (verificar contexto-empresa-ativo.md)

---

## Formato de Saída para a Planilha (coluna "Termos LSI")

```
[Cluster Regulatório — alta prioridade]:
autorização prévia, regulamentação vigente, órgão competente, base legal, ...

[Cluster Mecânico — alta prioridade]:
como funciona, participação, cadastro, número da sorte, ...

[Cluster Risco/Conformidade — média prioridade]:
promoção ilegal, sem autorização, multa, suspensão, ...

[Cluster Execução — média prioridade]:
estrutura técnica, regulamento personalizado, hotsite, dashboard, ...

[Cluster Comercial — baixa prioridade — apenas CTAs]:
empresa especializada, como contratar, ...
```

---

*LSI Taxonomy v1.0 — SEO Contextualizador Squad*
