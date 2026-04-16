# Template: Delivery Package

<!-- USO: Preencher todas as variáveis {placeholder} antes de entregar ao usuário -->
<!-- EXECUTOR: output-packager -->
<!-- GATE: SP-004 -->

---

```
═══════════════════════════════════════════════════════════════
📦 PACOTE DE ENTREGA
Cliente: {nome_empresa}
Keyword: {keyword}
Tipo de artigo: {tipo_artigo}
Data: {data_producao}
═══════════════════════════════════════════════════════════════
```

---

## 📌 1. Meta Description

```
{meta_description}
```

**Validação:**
- Palavras: {word_count_meta} (target: 18-22)
- Keyword presente: {sim/não}
- Tom: declarativo, sem imperativo

---

## 📌 2. Título Principal (H1)

```
{h1_titulo}
```

**Validação:**
- Caracteres: {char_count_h1} (target: máx. 70)
- Keyword presente: {sim/não}

---

## 📌 3. Slug

```
{slug}
```

**Validação:**
- Caracteres: {char_count_slug} (target: máx. 60)
- Formato: kebab-case lowercase
- Acentos: nenhum

---

## 📌 4. Conteúdo Completo (HTML)

> ⚠️ O FAQ está integrado como última seção do HTML abaixo — não é entregue separado.

```html
{html_content}
```

**Validação:**
- Summarization presente: {sim/não}
- Word count total: {total_words} palavras
- Seções: {n_h2} H2 + {n_h3} H3
- Tags proibidas: nenhuma
- Wrappers HTML: nenhum
- Conectores proibidos: nenhum
- FAQ integrado no final: {sim/não} ({n_perguntas} perguntas)

---

```
═══════════════════════════════════════════════════════════════
STATUS: ✅ Gate SP-004 PASS
Próxima keyword: {proxima_keyword | "Batch concluído"}
═══════════════════════════════════════════════════════════════
```
