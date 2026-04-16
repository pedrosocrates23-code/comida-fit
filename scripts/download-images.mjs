/**
 * download-images.mjs
 * Busca imagens no Pexels e salva como WebP em public/images/receitas/
 *
 * Uso:
 *   node scripts/download-images.mjs --key=SUA_CHAVE_PEXELS
 *
 * Chave gratuita em: https://www.pexels.com/api/
 */

import https from 'https';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import sharp from 'sharp';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'images', 'receitas');

// ── Chave via argumento --key=xxx ──────────────────────────────────────────
const keyArg = process.argv.find((a) => a.startsWith('--key='));
const PEXELS_KEY = keyArg ? keyArg.split('=')[1] : process.env.PEXELS_API_KEY;

if (!PEXELS_KEY) {
  console.error('\n❌  Chave Pexels não encontrada.');
  console.error('   Execute: node scripts/download-images.mjs --key=SUA_CHAVE\n');
  process.exit(1);
}

// ── Mapa slug → termos de busca em inglês ─────────────────────────────────
const SEARCH_TERMS = {
  'agua-detox-de-pepino-e-hortela':        'cucumber mint detox water drink',
  'arroz-integral-com-feijao-carioca':     'brown rice beans healthy meal',
  'banana-com-pasta-de-amendoim':          'banana peanut butter healthy snack',
  'barrinha-de-cereal-caseira':            'homemade granola energy bar',
  'batata-doce-assada-com-mel':            'baked sweet potato honey',
  'biscoito-de-aveia-e-banana':            'oat banana cookies healthy biscuit',
  'bolinho-de-atum-assado':                'baked tuna patties fish cake',
  'brownie-de-batata-doce':                'sweet potato chocolate brownie',
  'camarao-grelhado-com-salada-verde':     'grilled shrimp green salad seafood',
  'carne-moida-com-abobrinha':             'ground beef zucchini healthy',
  'chips-de-batata-doce-assada':           'baked sweet potato chips crispy',
  'crepioca-de-ovos':                      'egg tapioca crepe healthy breakfast',
  'frango-ao-molho-de-iogurte':            'chicken yogurt sauce herbs',
  'frango-desfiado-com-arroz-integral':    'shredded chicken brown rice bowl',
  'frango-grelhado-com-legumes-no-vapor':  'grilled chicken steamed vegetables',
  'fruta-com-castanhas-pre-treino':        'fresh fruit mixed nuts snack bowl',
  'gelatina-proteica-de-morango':          'strawberry gelatin dessert protein',
  'hamburguer-de-grao-de-bico':            'chickpea veggie burger patty',
  'iogurte-grego-com-granola-caseira':     'greek yogurt granola bowl breakfast',
  'iogurte-proteico-com-frutas':           'protein yogurt fresh fruits bowl',
  'mingau-de-aveia-com-frutas-vermelhas':  'oatmeal porridge berries breakfast',
  'mousse-de-maracuja-fit':               'passion fruit mousse dessert healthy',
  'muffin-de-proteina-de-chocolate':       'chocolate protein muffin healthy',
  'omelete-de-espinafre-e-queijo-cottage': 'spinach cottage cheese omelet',
  'omelete-pos-treino-de-clara':           'egg white omelet post workout',
  'omelete-recheada-de-legumes':           'vegetable stuffed fluffy omelet',
  'ovos-mexidos-com-abacate':              'scrambled eggs avocado toast',
  'palito-de-cenoura-com-homus':           'carrot sticks hummus dip healthy',
  'panqueca-de-banana-sem-farinha':        'banana pancakes flourless healthy',
  'pudim-fit-sem-lactose':                 'vanilla pudding dessert healthy',
  'quinoa-com-legumes-grelhados':          'quinoa grilled vegetables bowl',
  'risoto-de-couve-flor-com-frango':       'cauliflower risotto chicken healthy',
  'salada-de-atum-com-grao-de-bico':       'tuna chickpea salad healthy',
  'salmao-assado-com-aspargos':            'baked salmon asparagus healthy',
  'sanduiche-de-atum-integral':            'tuna whole grain sandwich healthy',
  'shake-de-aveia-pre-treino':             'oatmeal pre workout shake smoothie',
  'shake-proteico-de-chocolate':           'chocolate protein shake fitness',
  'shake-whey-com-banana':                 'banana protein shake whey',
  'smoothie-bowl-de-acai-fit':             'acai smoothie bowl toppings',
  'smoothie-de-morango-com-iogurte':       'strawberry yogurt smoothie glass',
  'smoothie-verde-detox':                  'green detox smoothie spinach',
  'sopa-de-legumes-proteica':              'vegetable protein soup bowl',
  'sorvete-de-banana-com-pasta-de-amendoim': 'banana ice cream peanut butter',
  'strogonoff-fit-de-frango':              'chicken stroganoff cream sauce',
  'suco-de-beterraba-com-gengibre':        'beet ginger juice red healthy',
  'tapioca-de-frango-desfiado':            'tapioca crepe shredded chicken',
  'tilapia-assada-com-ervas':              'baked tilapia fish herbs lemon',
  'torrada-integral-com-ovos':             'whole grain toast eggs breakfast',
  'trufa-de-chocolate-com-oleo-de-coco':   'chocolate coconut truffle dessert',
  'vitamina-de-mamao-com-linhaca':         'papaya flaxseed smoothie vitamin',
  'wrap-de-frango-com-alface':             'chicken lettuce wrap healthy',
  'zoodles-com-pesto-de-manjericao':       'zucchini noodles pesto basil',

  // ── 36 novos slugs (pipeline 404 recovery) ────────────────────────────────
  'panquecas-fininhas-sem-gluten-e-lactose-free': 'thin gluten free pancakes stack healthy',
  'mini-pizza-de-abobrinha':              'zucchini mini pizza low carb healthy',
  'bolo-de-limao-lowcarb':               'lemon low carb cake slice healthy',
  'suco-para-desinchar':                 'detox juice reduce bloating healthy drink',
  'shake-detox-de-banana':              'banana detox smoothie green healthy',
  'bolo-de-chocolate-low-carb':         'chocolate low carb cake slice dessert',
  'receitas-fitness':                   'healthy fitness meal prep bowl',
  'bolo-mousse-de-chocolate':           'chocolate mousse cake dessert creamy',
  'pudim-de-coco-low-carb':            'coconut pudding low carb dessert',
  'receita-de-torta-salgada-low-carb':  'savory low carb tart pie healthy',
  'receita-low-carb-facil':            'easy low carb healthy meal bowl',
  'como-fazer-cuscuz-fit':             'healthy couscous fit meal plate',
  'receita-de-bolo-low-carb-facil':    'easy low carb cake simple healthy',
  'receitas-low-carb-com-espinafre':   'spinach low carb recipes healthy green',
  'receita-de-bolo-de-aniversario-low-carb': 'birthday cake low carb celebration healthy',
  'danette-low-carb':                  'chocolate cream pudding dessert healthy',
  'mousse-de-morango-fit':             'strawberry mousse fit dessert healthy',
  'receita-de-vitamina-saudavel':      'healthy vitamin smoothie glass nutritious',
  'casadinho-fit':                     'fit sandwich cookie coconut healthy sweet',
  'receita-de-bolo-low-carb':         'low carb cake slice healthy dessert',
  'receita-de-bolo-de-chocolate-low-carb': 'chocolate low carb cake healthy dessert',
  'receitas-saudaveis-e-rapidas':      'quick healthy recipes meal prep',
  'bolo-de-coco-gelado':              'coconut frozen cake dessert slice',
  'bolo-fit-saboroso':                'fit tasty cake healthy dessert slice',
  '5-receitas-de-quiche-low-carb':    'low carb quiche savory tart eggs',
  'receita-fit-e-saudavel':           'healthy fit recipe meal plate',
  'receitas-fit-com-batata-doce':     'sweet potato healthy fit recipes bowl',
  'barrinha-de-chocolate-com-coco-low-carb': 'chocolate coconut energy bar healthy',
  'enroladinho-de-banana':            'banana roll snack sweet healthy',
  'bolo-de-chocolate-fit':            'fit chocolate cake healthy dessert',
  'bolo-de-maca-canela-e-frutas-secas': 'apple cinnamon dried fruit cake healthy',
  'chips-de-banana':                  'baked banana chips crispy healthy snack',
  'bolo-de-caneca-low-carb-de-chocolate': 'chocolate mug cake low carb healthy',
  '10-receitas-de-bolo-de-banana-fit': 'banana fit cake varieties healthy dessert',
  'bolo-de-laranja-fit':              'orange fit cake slice healthy dessert',
  'macarrao-de-abobrinha-com-molho-branco': 'zucchini noodles white sauce creamy healthy',
};

// ── Helpers ────────────────────────────────────────────────────────────────
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function fetchJson(url, headers) {
  return new Promise((resolve, reject) => {
    const req = https.get(url, { headers }, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error(`JSON parse error: ${data.slice(0, 200)}`)); }
      });
    });
    req.on('error', reject);
  });
}

function downloadBuffer(url) {
  return new Promise((resolve, reject) => {
    const get = (u) => {
      https.get(u, (res) => {
        if (res.statusCode === 301 || res.statusCode === 302) {
          return get(res.headers.location);
        }
        const chunks = [];
        res.on('data', (c) => chunks.push(c));
        res.on('end', () => resolve(Buffer.concat(chunks)));
      }).on('error', reject);
    };
    get(url);
  });
}

async function searchPexels(query) {
  const encoded = encodeURIComponent(query + ' food');
  const url = `https://api.pexels.com/v1/search?query=${encoded}&per_page=3&orientation=landscape&size=medium`;
  const data = await fetchJson(url, { Authorization: PEXELS_KEY });

  if (!data.photos || data.photos.length === 0) {
    // fallback: busca mais genérica
    const fallback = encodeURIComponent('healthy food meal');
    const fb = await fetchJson(
      `https://api.pexels.com/v1/search?query=${fallback}&per_page=1&orientation=landscape`,
      { Authorization: PEXELS_KEY }
    );
    return fb.photos?.[0]?.src?.large2x || fb.photos?.[0]?.src?.large || null;
  }

  // Prefere a foto com melhor resolução
  const photo = data.photos[0];
  return photo.src.large2x || photo.src.large;
}

// ── Main ───────────────────────────────────────────────────────────────────
async function main() {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const slugs = Object.keys(SEARCH_TERMS);
  let ok = 0, skip = 0, fail = 0;

  console.log(`\n🔍 Baixando ${slugs.length} imagens para public/images/receitas/\n`);

  for (let i = 0; i < slugs.length; i++) {
    const slug = slugs[i];
    const dest = path.join(OUTPUT_DIR, `${slug}.webp`);

    // Pula se já existe
    if (fs.existsSync(dest)) {
      console.log(`[${i + 1}/${slugs.length}] ⏭  ${slug} (já existe)`);
      skip++;
      continue;
    }

    const terms = SEARCH_TERMS[slug];
    process.stdout.write(`[${i + 1}/${slugs.length}] 🔎 ${slug} ...`);

    try {
      const imageUrl = await searchPexels(terms);
      if (!imageUrl) throw new Error('sem resultado');

      const buffer = await downloadBuffer(imageUrl);

      // Converte para WebP 400×300 com sharp
      await sharp(buffer)
        .resize(400, 300, { fit: 'cover', position: 'centre' })
        .webp({ quality: 82 })
        .toFile(dest);

      console.log(` ✅`);
      ok++;
    } catch (err) {
      console.log(` ❌ ${err.message}`);
      fail++;
    }

    // Aguarda 350ms entre requests (limite Pexels: ~200 req/hora free)
    if (i < slugs.length - 1) await sleep(350);
  }

  console.log(`\n📊 Resultado: ${ok} baixadas, ${skip} puladas, ${fail} falhas`);
  if (fail > 0) console.log('   Execute novamente para tentar as que falharam.\n');
  else console.log('   Todas as imagens estão prontas! 🎉\n');
}

main().catch((err) => {
  console.error('\n💥 Erro fatal:', err.message);
  process.exit(1);
});
