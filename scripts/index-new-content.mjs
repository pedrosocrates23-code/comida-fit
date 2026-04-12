/**
 * Auto-indexer para conteúdo novo
 * Detecta arquivos .md novos em src/content/receitas/ e src/content/blog/
 * e submete as URLs correspondentes para o GSC Indexing API.
 *
 * Uso:
 *   node scripts/index-new-content.mjs           → detecta e indexa novos
 *   node scripts/index-new-content.mjs --dry-run → mostra o que seria indexado, sem submeter
 */

import { google } from 'googleapis';
import { readFileSync, existsSync, writeFileSync, statSync } from 'fs';
import { readdir } from 'fs/promises';
import { fileURLToPath } from 'url';
import { dirname, join, basename } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

const KEY_FILE    = join(__dirname, 'gsc-service-account.json');
const LOG_FILE    = join(__dirname, 'indexing-log.json');
const CONTENT_LOG = join(__dirname, 'content-index-state.json');
const SITE_URL    = 'https://melhoresreceitasfit.com.br';
const DRY_RUN     = process.argv.includes('--dry-run');

// Mapeia pasta de conteúdo → URL base no site
const CONTENT_MAP = {
  'receitas': `${SITE_URL}/receitas/`,
  'blog':     `${SITE_URL}/blog/`,
};

const auth = new google.auth.GoogleAuth({
  keyFile: KEY_FILE,
  scopes: ['https://www.googleapis.com/auth/indexing'],
});

function loadJson(path) {
  if (!existsSync(path)) return {};
  try { return JSON.parse(readFileSync(path, 'utf8')); }
  catch { return {}; }
}

function saveJson(path, data) {
  writeFileSync(path, JSON.stringify(data, null, 2), 'utf8');
}

function slugFromFilename(filename) {
  return basename(filename, '.md');
}

async function getContentFiles(contentType) {
  const dir = join(__dirname, '..', 'src', 'content', contentType);
  if (!existsSync(dir)) return [];
  const files = await readdir(dir);
  return files
    .filter(f => f.endsWith('.md'))
    .map(f => ({
      file: f,
      slug: slugFromFilename(f),
      url: `${CONTENT_MAP[contentType]}${slugFromFilename(f)}/`,
      mtime: statSync(join(dir, f)).mtimeMs,
    }));
}

async function indexUrl(client, url) {
  if (DRY_RUN) return { ok: true, dryRun: true };
  try {
    const res = await client.request({
      url: 'https://indexing.googleapis.com/v3/urlNotifications:publish',
      method: 'POST',
      data: { url, type: 'URL_UPDATED' },
    });
    return { ok: true, status: res.status };
  } catch (err) {
    return {
      ok: false,
      status: err.response?.status,
      msg: err.response?.data?.error?.message || err.message,
    };
  }
}

async function main() {
  console.log('\n🚀  Auto-indexer — Conteúdo Novo');
  if (DRY_RUN) console.log('   (DRY RUN — nenhuma requisição será enviada)\n');

  const state  = loadJson(CONTENT_LOG); // { url: { mtime, indexed } }
  const log    = loadJson(LOG_FILE);
  const client = DRY_RUN ? null : await auth.getClient();

  let toIndex = [];

  // Varre todos os tipos de conteúdo
  for (const [type] of Object.entries(CONTENT_MAP)) {
    const files = await getContentFiles(type);
    for (const { file, url, mtime } of files) {
      const prev = state[url];
      // Novo arquivo ou modificado após última indexação
      if (!prev || prev.mtime < mtime || !prev.indexed) {
        toIndex.push({ url, mtime, type, file });
      }
    }
  }

  if (toIndex.length === 0) {
    console.log('✅  Nenhum conteúdo novo ou modificado encontrado.\n');
    return;
  }

  console.log(`📋  ${toIndex.length} URL(s) para indexar:\n`);
  toIndex.forEach(({ url, type }) => console.log(`   [${type}] ${url}`));
  console.log('');

  let ok = 0, fail = 0;
  for (const { url, mtime, file } of toIndex) {
    const result = await indexUrl(client, url);
    const ts     = Date.now();

    if (result.ok) {
      ok++;
      state[url] = { mtime, indexed: true, ts, file };
      log[url]   = { status: 'ok', ts, date: new Date(ts).toISOString() };
      console.log(`  ✅  ${url}${DRY_RUN ? ' (simulado)' : ''}`);
    } else {
      fail++;
      state[url] = { mtime, indexed: false, ts, file, error: result.msg };
      console.log(`  ❌  [${result.status}] ${result.msg?.slice(0,60)} → ${url}`);

      if (result.status === 403) {
        const key = JSON.parse(readFileSync(KEY_FILE, 'utf8'));
        console.log(`\n  🔑  Adicione ${key.client_email} como Proprietário no GSC.\n`);
        break;
      }
    }

    if (!DRY_RUN) {
      saveJson(CONTENT_LOG, state);
      saveJson(LOG_FILE, log);
      await new Promise(r => setTimeout(r, 400));
    }
  }

  console.log(`\n📊  Resultado: ${ok} ✅  | ${fail} ❌`);
  if (!DRY_RUN) {
    saveJson(CONTENT_LOG, state);
    saveJson(LOG_FILE, log);
  }
  console.log('');
}

main().catch(err => {
  console.error('❌  Erro:', err.message);
  process.exit(1);
});
