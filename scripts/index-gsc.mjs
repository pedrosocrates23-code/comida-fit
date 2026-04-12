/**
 * Google Search Console — Indexing API
 * Submete URLs para indexação imediata via Indexing API.
 *
 * Uso:
 *   node scripts/index-gsc.mjs           → submete TODAS as URLs do sitemap
 *   node scripts/index-gsc.mjs --new     → submete apenas URLs novas (não registradas)
 *   node scripts/index-gsc.mjs --url https://... → submete uma URL específica
 *
 * Pré-requisito no GSC:
 *   Adicione fit-82@fits-493115.iam.gserviceaccount.com como Proprietário Delegado
 *   em Search Console → Configurações → Usuários e Permissões.
 */

import { google } from 'googleapis';
import { readFileSync, existsSync, writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

// ── Config ──────────────────────────────────────────────────────────────
const KEY_FILE   = join(__dirname, 'gsc-service-account.json');
const SITEMAP    = join(__dirname, '..', 'dist', 'sitemap.xml');
const LOG_FILE   = join(__dirname, 'indexing-log.json');
const SITE_URL   = 'https://melhoresreceitasfit.com.br';
const BATCH_SIZE = 100; // limite da API: 100 req/dia para indexação
const DELAY_MS   = 500; // delay entre requests (evitar rate limit)

// ── Auth ─────────────────────────────────────────────────────────────────
const auth = new google.auth.GoogleAuth({
  keyFile: KEY_FILE,
  scopes: ['https://www.googleapis.com/auth/indexing'],
});

// ── Helpers ───────────────────────────────────────────────────────────────
function extractUrls(xmlContent) {
  const matches = xmlContent.matchAll(/<loc>(https?:\/\/[^<]+)<\/loc>/g);
  return [...matches].map(m => m[1].trim());
}

function loadLog() {
  if (!existsSync(LOG_FILE)) return {};
  try { return JSON.parse(readFileSync(LOG_FILE, 'utf8')); }
  catch { return {}; }
}

function saveLog(log) {
  writeFileSync(LOG_FILE, JSON.stringify(log, null, 2), 'utf8');
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function formatDate(ts) {
  return new Date(ts).toLocaleString('pt-BR', { timeZone: 'America/Sao_Paulo' });
}

// ── Core: indexar uma URL ─────────────────────────────────────────────────
async function indexUrl(client, url, type = 'URL_UPDATED') {
  try {
    const res = await client.request({
      url: 'https://indexing.googleapis.com/v3/urlNotifications:publish',
      method: 'POST',
      data: { url, type },
    });
    return { ok: true, status: res.status, data: res.data };
  } catch (err) {
    const status = err.response?.status;
    const msg    = err.response?.data?.error?.message || err.message;
    return { ok: false, status, msg };
  }
}

// ── Main ──────────────────────────────────────────────────────────────────
async function main() {
  const args    = process.argv.slice(2);
  const onlyNew = args.includes('--new');
  const singleUrl = args.find(a => a.startsWith('http'));

  console.log('\n🔍  GSC Indexing API — Melhores Receitas Fit');
  console.log('════════════════════════════════════════════\n');

  // Obtém client autenticado
  const client = await auth.getClient();

  // Determina lista de URLs
  let urls = [];
  if (singleUrl) {
    urls = [singleUrl];
    console.log(`Modo: URL única → ${singleUrl}`);
  } else {
    if (!existsSync(SITEMAP)) {
      console.error('❌  sitemap.xml não encontrado. Execute: npm run build');
      process.exit(1);
    }
    const xml = readFileSync(SITEMAP, 'utf8');
    urls = extractUrls(xml);
    console.log(`Modo: ${onlyNew ? 'apenas novas' : 'todas'} | Total no sitemap: ${urls.length} URLs`);
  }

  // Filtra já indexadas (se --new)
  const log = loadLog();
  if (onlyNew && !singleUrl) {
    const antes = urls.length;
    urls = urls.filter(u => !log[u] || log[u].status !== 'ok');
    console.log(`Já indexadas: ${antes - urls.length} | A submeter: ${urls.length}`);
  }

  if (urls.length === 0) {
    console.log('\n✅  Nenhuma URL nova para submeter.');
    return;
  }

  // Limita ao batch diário
  const batch = urls.slice(0, BATCH_SIZE);
  if (urls.length > BATCH_SIZE) {
    console.log(`\n⚠️  Limite diário da API: ${BATCH_SIZE} URLs. Restando ${urls.length - BATCH_SIZE} para próxima execução.`);
  }

  console.log(`\nSubmetendo ${batch.length} URL(s)...\n`);

  let ok = 0, fail = 0;
  const errors = [];

  for (const url of batch) {
    const result = await indexUrl(client, url);
    const ts     = Date.now();

    if (result.ok) {
      ok++;
      log[url] = { status: 'ok', ts, date: formatDate(ts) };
      console.log(`  ✅  ${url}`);
    } else {
      fail++;
      log[url] = { status: 'error', ts, date: formatDate(ts), msg: result.msg, httpStatus: result.status };
      errors.push({ url, msg: result.msg, status: result.status });

      console.log(`  ❌  [${result.status}] ${result.msg} → ${url}`);
    }

    saveLog(log);
    if (batch.indexOf(url) < batch.length - 1) await sleep(DELAY_MS);
  }

  // Resumo
  console.log('\n════════════════════════════════════════════');
  console.log(`Resultado: ${ok} ✅  sucesso | ${fail} ❌  erro`);
  if (errors.length > 0 && errors[0].status === 403) {
    console.log('\n🔑  Ação necessária: adicione a conta de serviço como proprietário no GSC.');
    console.log(`   E-mail: ${readKeyEmail()}`);
    console.log('   GSC > Configurações > Usuários e permissões > Adicionar usuário');
    console.log('   Permissão: Proprietário (Owner)');
  }
  console.log(`\nLog salvo em: scripts/indexing-log.json\n`);
}

function readKeyEmail() {
  try {
    const key = JSON.parse(readFileSync(KEY_FILE, 'utf8'));
    return key.client_email;
  } catch { return '—'; }
}

main().catch(err => {
  console.error('\n❌  Erro fatal:', err.message);
  process.exit(1);
});
