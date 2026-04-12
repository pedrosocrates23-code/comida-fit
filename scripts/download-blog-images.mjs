/**
 * download-blog-images.mjs
 * Baixa imagens do Pexels para:
 *   - Hero da Home
 *   - Hero do Blog
 *   - Artigos do blog (src/content/blog/)
 *
 * Uso:
 *   node scripts/download-blog-images.mjs --key=SUA_CHAVE_PEXELS
 */

import https from 'https';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import sharp from 'sharp';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PUBLIC    = path.join(__dirname, '..', 'public', 'images');

const keyArg    = process.argv.find((a) => a.startsWith('--key='));
const PEXELS_KEY = keyArg ? keyArg.split('=')[1] : process.env.PEXELS_API_KEY;

if (!PEXELS_KEY) {
  console.error('\n❌  Chave Pexels não encontrada.');
  console.error('   Execute: node scripts/download-blog-images.mjs --key=SUA_CHAVE\n');
  process.exit(1);
}

// ── Imagens a baixar ──────────────────────────────────────────────────────────
// formato: { file, query, width, height, quality }
const IMAGES = [
  // Hero da Home (480×480, quadrado)
  {
    dest:    path.join(PUBLIC, 'hero-receitas-fit.webp'),
    query:   'colorful healthy food bowls vegetables fruits meal prep',
    width:   960,
    height:  960,
    quality: 85,
    label:   'Hero Home',
  },
  // Hero do Blog (1200×480, banner wide)
  {
    dest:    path.join(PUBLIC, 'hero-blog.webp'),
    query:   'healthy nutrition food science diet article',
    width:   1200,
    height:  480,
    quality: 85,
    label:   'Hero Blog',
  },
  // Artigo: Proteínas na Dieta Fit
  {
    dest:    path.join(PUBLIC, 'blog', 'proteinas-dieta-fit.webp'),
    query:   'chicken eggs salmon protein rich foods healthy diet',
    width:   1200,
    height:  675,
    quality: 85,
    label:   'Blog: Proteínas',
  },
  // Artigo: Carboidratos Bons e Ruins
  {
    dest:    path.join(PUBLIC, 'blog', 'carboidratos.webp'),
    query:   'brown rice sweet potato oats quinoa healthy carbohydrates bowl',
    width:   1200,
    height:  675,
    quality: 85,
    label:   'Blog: Carboidratos',
  },
];

// ── Helpers ──────────────────────────────────────────────────────────────────
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function fetchJson(url, headers) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers }, (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error(`JSON parse: ${data.slice(0, 200)}`)); }
      });
    }).on('error', reject);
  });
}

function downloadBuffer(url) {
  return new Promise((resolve, reject) => {
    const get = (u) => {
      https.get(u, (res) => {
        if (res.statusCode === 301 || res.statusCode === 302) return get(res.headers.location);
        const chunks = [];
        res.on('data', c => chunks.push(c));
        res.on('end', () => resolve(Buffer.concat(chunks)));
      }).on('error', reject);
    };
    get(url);
  });
}

async function searchPexels(query, orientation = 'landscape') {
  const encoded = encodeURIComponent(query);
  const url = `https://api.pexels.com/v1/search?query=${encoded}&per_page=5&orientation=${orientation}&size=large`;
  const data = await fetchJson(url, { Authorization: PEXELS_KEY });
  if (!data.photos?.length) throw new Error('nenhuma foto encontrada');
  // Pega a foto com maior resolução disponível
  const photo = data.photos[0];
  return photo.src.large2x || photo.src.large || photo.src.medium;
}

// ── Main ─────────────────────────────────────────────────────────────────────
async function main() {
  fs.mkdirSync(path.join(PUBLIC, 'blog'), { recursive: true });

  console.log(`\n🖼  Baixando ${IMAGES.length} imagens via Pexels\n`);

  let ok = 0, skip = 0, fail = 0;

  for (let i = 0; i < IMAGES.length; i++) {
    const { dest, query, width, height, quality, label } = IMAGES[i];

    if (fs.existsSync(dest)) {
      console.log(`[${i+1}/${IMAGES.length}] ⏭  ${label} (já existe)`);
      skip++;
      continue;
    }

    process.stdout.write(`[${i+1}/${IMAGES.length}] 🔎 ${label} ...`);

    try {
      const orientation = width > height ? 'landscape' : 'square';
      const imageUrl = await searchPexels(query, orientation);
      const buffer   = await downloadBuffer(imageUrl);

      await sharp(buffer)
        .resize(width, height, { fit: 'cover', position: 'attention' })
        .webp({ quality })
        .toFile(dest);

      const kb = Math.round(fs.statSync(dest).size / 1024);
      console.log(` ✅  (${kb} KB)`);
      ok++;
    } catch (err) {
      console.log(` ❌  ${err.message}`);
      fail++;
    }

    if (i < IMAGES.length - 1) await sleep(400);
  }

  console.log(`\n📊  ${ok} baixadas, ${skip} puladas, ${fail} falhas`);
  if (fail === 0) console.log('   Todas prontas! 🎉\n');
}

main().catch(err => {
  console.error('\n💥 Erro fatal:', err.message);
  process.exit(1);
});
