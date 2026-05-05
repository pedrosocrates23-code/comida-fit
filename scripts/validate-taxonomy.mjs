#!/usr/bin/env node
// ───────────────────────────────────────────────────────────────
// validate-taxonomy.mjs
// ───────────────────────────────────────────────────────────────
//
// Garante que TODO ASIN que aparece em src/content/blog/*.md tem
// entrada em src/data/produto-taxonomy.ts. Falha o build se faltar.
//
// Também checa:
//  - se cada `categoria` referenciada existe em CATEGORIAS
//  - se cada `marca` referenciada existe em MARCAS
//  - se o `tipo` da entrada bate com o `tipo` declarado em CATEGORIAS
//
// Uso:
//   node scripts/validate-taxonomy.mjs           # roda check + relatório
//   npm run validate:taxonomy
// ───────────────────────────────────────────────────────────────

import { readdir, readFile } from 'node:fs/promises';
import { join, dirname }     from 'node:path';
import { fileURLToPath }     from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname  = dirname(__filename);
const ROOT       = join(__dirname, '..');
const BLOG_DIR   = join(ROOT, 'src', 'content', 'blog');
const TAX_FILE   = join(ROOT, 'src', 'data', 'produto-taxonomy.ts');

// ── Cores ──
const C = {
  red:    (s) => `\x1b[31m${s}\x1b[0m`,
  green:  (s) => `\x1b[32m${s}\x1b[0m`,
  yellow: (s) => `\x1b[33m${s}\x1b[0m`,
  cyan:   (s) => `\x1b[36m${s}\x1b[0m`,
  bold:   (s) => `\x1b[1m${s}\x1b[0m`,
  dim:    (s) => `\x1b[2m${s}\x1b[0m`,
};

// ── Utilidades ──
function fail(msg) { console.error(C.red(`✘ ${msg}`)); process.exitCode = 1; }
function ok(msg)   { console.log(C.green(`✔ ${msg}`)); }
function info(msg) { console.log(C.cyan(`ℹ ${msg}`)); }
function warn(msg) { console.log(C.yellow(`⚠ ${msg}`)); }

// ── Parser do produto-taxonomy.ts ──
// Não vamos importar TS direto (sem ts-node). Extraímos via regex
// os mapas que precisamos: taxonomia, CATEGORIAS, MARCAS.
async function parseTaxonomy() {
  const src = await readFile(TAX_FILE, 'utf8');

  // Extrai entradas de `taxonomia`: 'ASIN': { tipo: 'X', categoria: 'Y', marca: 'Z' }
  const taxonomia = {};
  const taxRegex = /'([A-Z0-9]{10})'\s*:\s*\{\s*tipo:\s*'(\w+)',\s*categoria:\s*'([\w-]+)',\s*marca:\s*'([\w-]+)'\s*\}/g;
  let m;
  while ((m = taxRegex.exec(src)) !== null) {
    const [, asin, tipo, categoria, marca] = m;
    taxonomia[asin] = { tipo, categoria, marca };
  }

  // Extrai chaves de CATEGORIAS: '<slug>': { label: '...', tipo: '...' }
  const categorias = {};
  const catBlock = src.match(/CATEGORIAS:[^=]*=\s*\{([\s\S]*?)\n\};/);
  if (catBlock) {
    const catRegex = /'([\w-]+)'\s*:\s*\{\s*label:\s*'[^']+',\s*tipo:\s*'(\w+)'\s*\}/g;
    while ((m = catRegex.exec(catBlock[1])) !== null) {
      categorias[m[1]] = { tipo: m[2] };
    }
  }

  // Extrai chaves de MARCAS: '<slug>': { label: '...' }
  const marcas = new Set();
  const marcaBlock = src.match(/MARCAS:[^=]*=\s*\{([\s\S]*?)\n\};/);
  if (marcaBlock) {
    const marcaRegex = /'([\w-]+)'\s*:\s*\{\s*label:\s*'[^']+'\s*\}/g;
    while ((m = marcaRegex.exec(marcaBlock[1])) !== null) {
      marcas.add(m[1]);
    }
  }

  return { taxonomia, categorias, marcas };
}

// ── Coleta ASINs dos blog posts ──
async function collectAsinsFromBlog() {
  const files = (await readdir(BLOG_DIR)).filter((f) => f.endsWith('.md'));
  const asinsPorPost = new Map();
  const todosAsins = new Set();

  for (const file of files) {
    const content = await readFile(join(BLOG_DIR, file), 'utf8');
    const asinRegex = /^\s*-\s*asin:\s*"([A-Z0-9]{10})"/gm;
    const lista = [];
    let m;
    while ((m = asinRegex.exec(content)) !== null) {
      lista.push(m[1]);
      todosAsins.add(m[1]);
    }
    if (lista.length) asinsPorPost.set(file, lista);
  }

  return { asinsPorPost, todosAsins };
}

// ── Main ──
async function main() {
  console.log(C.bold('\n🔎 Validando taxonomia de produtos\n'));

  const { taxonomia, categorias, marcas } = await parseTaxonomy();
  const { asinsPorPost, todosAsins }      = await collectAsinsFromBlog();

  info(`Posts com produtos: ${asinsPorPost.size}`);
  info(`ASINs únicos no blog: ${todosAsins.size}`);
  info(`ASINs cadastrados em produto-taxonomy.ts: ${Object.keys(taxonomia).length}`);
  info(`Categorias canônicas: ${Object.keys(categorias).length}`);
  info(`Marcas canônicas: ${marcas.size}`);
  console.log();

  let problemas = 0;

  // 1. Cada ASIN do blog deve ter taxonomia
  const semTaxonomia = [];
  for (const asin of todosAsins) {
    if (!taxonomia[asin]) semTaxonomia.push(asin);
  }
  if (semTaxonomia.length) {
    fail(`${semTaxonomia.length} ASIN(s) sem entrada em produto-taxonomy.ts:`);
    for (const asin of semTaxonomia) {
      // Encontra em qual post ele aparece para facilitar a edição
      const posts = [...asinsPorPost.entries()]
        .filter(([, lista]) => lista.includes(asin))
        .map(([file]) => file);
      console.error(C.dim(`    ${asin}  ${C.dim('← ' + posts.join(', '))}`));
    }
    problemas += semTaxonomia.length;
  } else {
    ok('Todos os ASINs do blog têm taxonomia');
  }

  // 2. Categorias e marcas referenciadas existem
  const catsOrfas = new Set();
  const marcasOrfas = new Set();
  const tipoIncoerente = [];
  for (const [asin, t] of Object.entries(taxonomia)) {
    if (!categorias[t.categoria]) catsOrfas.add(t.categoria);
    if (!marcas.has(t.marca))     marcasOrfas.add(t.marca);
    if (categorias[t.categoria] && categorias[t.categoria].tipo !== t.tipo) {
      tipoIncoerente.push({ asin, esperado: categorias[t.categoria].tipo, atual: t.tipo, categoria: t.categoria });
    }
  }
  if (catsOrfas.size) {
    fail(`Categorias usadas mas não declaradas em CATEGORIAS: ${[...catsOrfas].join(', ')}`);
    problemas += catsOrfas.size;
  }
  if (marcasOrfas.size) {
    fail(`Marcas usadas mas não declaradas em MARCAS: ${[...marcasOrfas].join(', ')}`);
    problemas += marcasOrfas.size;
  }
  if (tipoIncoerente.length) {
    fail(`Tipo do produto não bate com tipo da categoria:`);
    for (const x of tipoIncoerente) {
      console.error(C.dim(`    ${x.asin}: tipo=${x.atual} mas categoria '${x.categoria}' é tipo=${x.esperado}`));
    }
    problemas += tipoIncoerente.length;
  }

  // 3. ASINs cadastrados mas que não aparecem em nenhum post (warning, não fail)
  const orfaos = [];
  for (const asin of Object.keys(taxonomia)) {
    if (!todosAsins.has(asin)) orfaos.push(asin);
  }
  if (orfaos.length) {
    warn(`${orfaos.length} ASIN(s) na taxonomia sem post correspondente (ok, mas pode ser limpeza):`);
    for (const a of orfaos) console.log(C.dim(`    ${a}`));
  }

  // ── Relatório por tipo / categoria / marca ──
  console.log(C.bold('\n📊 Distribuição\n'));
  const porTipo = {};
  const porCat  = {};
  const porMarca = {};
  for (const t of Object.values(taxonomia)) {
    porTipo[t.tipo]      = (porTipo[t.tipo] ?? 0) + 1;
    porCat[t.categoria]  = (porCat[t.categoria] ?? 0) + 1;
    porMarca[t.marca]    = (porMarca[t.marca] ?? 0) + 1;
  }
  console.log(C.cyan('  Por tipo:'));
  for (const [k, v] of Object.entries(porTipo).sort((a, b) => b[1] - a[1])) {
    console.log(`    ${k.padEnd(14)} ${v}`);
  }
  console.log(C.cyan('\n  Por categoria:'));
  for (const [k, v] of Object.entries(porCat).sort((a, b) => b[1] - a[1])) {
    console.log(`    ${k.padEnd(20)} ${v}`);
  }
  console.log(C.cyan(`\n  Por marca: ${Object.keys(porMarca).length} marcas (top 10)`));
  for (const [k, v] of Object.entries(porMarca).sort((a, b) => b[1] - a[1]).slice(0, 10)) {
    console.log(`    ${k.padEnd(20)} ${v}`);
  }

  // ── Resultado ──
  console.log();
  if (problemas > 0) {
    console.error(C.red(C.bold(`\n✘ Validação falhou: ${problemas} problema(s).\n`)));
    process.exit(1);
  } else {
    ok(C.bold('Taxonomia válida. Build pode prosseguir.\n'));
  }
}

main().catch((err) => {
  console.error(C.red('Erro fatal na validação:'), err);
  process.exit(1);
});
