// ───────────────────────────────────────────────────────────────
// Taxonomia de produtos — registro central por ASIN
// ───────────────────────────────────────────────────────────────
//
// Fonte única da verdade para tipo/categoria/marca de cada produto.
// O script scripts/validate-taxonomy.mjs garante que TODO ASIN que
// aparece em src/content/blog/*.md tenha entrada aqui (build falha
// se faltar). Adicione um novo produto:
//
//   1. Cadastre o ASIN abaixo em `taxonomia`.
//   2. Se a marca for nova, adicione em `MARCAS`.
//   3. Se a categoria for nova, adicione em `CATEGORIAS` apontando
//      para um dos 4 `tipo`s.
//   4. Rode `npm run validate:taxonomy` para confirmar.
// ───────────────────────────────────────────────────────────────

export type ProdutoTipo = 'suplemento' | 'alimento' | 'equipamento' | 'acessorio';

export interface ProdutoTaxonomia {
  tipo:      ProdutoTipo;
  categoria: string; // slug — chave de CATEGORIAS
  marca:     string; // slug — chave de MARCAS
}

// Ordem aqui controla ordem na navegação
export const TIPOS: Record<ProdutoTipo, { label: string; descricao: string }> = {
  suplemento: {
    label: 'Suplementos',
    descricao: 'Whey, creatina, BCAA, vitaminas, pré-treino e demais suplementos esportivos.',
  },
  alimento: {
    label: 'Alimentos Fit',
    descricao: 'Pasta de amendoim, granola, barrinhas, aveia e demais alimentos saudáveis.',
  },
  equipamento: {
    label: 'Equipamentos de Cozinha',
    descricao: 'Air fryer, panela de pressão, iogurteira, processador, balança e mais.',
  },
  acessorio: {
    label: 'Acessórios',
    descricao: 'Recipientes, utensílios, peças de reposição e itens complementares.',
  },
};

export const CATEGORIAS: Record<string, { label: string; tipo: ProdutoTipo }> = {
  // Suplementos
  'creatina':         { label: 'Creatina',          tipo: 'suplemento' },
  'whey-protein':     { label: 'Whey Protein',      tipo: 'suplemento' },
  'bcaa':             { label: 'BCAA',              tipo: 'suplemento' },
  'glutamina':        { label: 'Glutamina',         tipo: 'suplemento' },
  'pre-treino':       { label: 'Pré-treino',        tipo: 'suplemento' },
  'vitamina-d3-k2':   { label: 'Vitamina D3 + K2',  tipo: 'suplemento' },
  'multivitaminico':  { label: 'Multivitamínico',   tipo: 'suplemento' },
  // Equipamentos
  'air-fryer':        { label: 'Air Fryer',          tipo: 'equipamento' },
  'panela-pressao':   { label: 'Panela de Pressão',  tipo: 'equipamento' },
  'iogurteira':       { label: 'Iogurteira',         tipo: 'equipamento' },
  'processador':      { label: 'Processador',        tipo: 'equipamento' },
  'balanca-cozinha':  { label: 'Balança de Cozinha', tipo: 'equipamento' },
  'espiralizador':    { label: 'Espiralizador',      tipo: 'equipamento' },
  'geladeira':        { label: 'Geladeira',          tipo: 'equipamento' },
  'geladeira-portatil': { label: 'Geladeira Portátil', tipo: 'equipamento' },
  // Acessórios
  'utensilio-cozinha': { label: 'Utensílios de Cozinha', tipo: 'acessorio' },
  'recipiente':        { label: 'Recipientes',           tipo: 'acessorio' },
  'pecas-reposicao':   { label: 'Peças de Reposição',    tipo: 'acessorio' },
  'ima-geladeira':     { label: 'Ímãs de Geladeira',     tipo: 'acessorio' },
};

export const MARCAS: Record<string, { label: string }> = {
  '3vs-nutrition':     { label: '3VS Nutrition' },
  'black-decker':      { label: 'Black+Decker' },
  'bodyaction':        { label: 'Bodyaction' },
  'bougerv':           { label: 'BougeRV' },
  'brastemp':          { label: 'Brastemp' },
  'cadence':           { label: 'Cadence' },
  'consul':            { label: 'Consul' },
  'dark-lab':          { label: 'Dark Lab' },
  'dona-chefa':        { label: 'Dona Chefa' },
  'easy-boost':        { label: 'Easy Boost' },
  'electrolux':        { label: 'Electrolux' },
  'ellym-nutrition':   { label: 'Ellym Nutrition' },
  'euro-cuisine':      { label: 'Euro Cuisine' },
  'ftw':               { label: 'FTW' },
  'gato-panda':        { label: 'Gato Panda' },
  'generica':          { label: 'Sem marca definida' },
  'insane':            { label: 'Insane' },
  'integralmedica':    { label: 'Integralmédica' },
  'izumi':             { label: 'Izumi' },
  'joymech':           { label: 'JoyMech' },
  'life-seeds':        { label: 'Life Seeds' },
  'mealthy':           { label: 'Mealthy' },
  'mondial':           { label: 'Mondial' },
  'ninja':             { label: 'Ninja' },
  'nutri-saude':       { label: 'Nutri Saúde' },
  'nutrends':          { label: 'Nutrends' },
  'optimum-nutrition': { label: 'Optimum Nutrition' },
  'philco':            { label: 'Philco' },
  'polar':             { label: 'Polar' },
  'puro-nutrition':    { label: 'Puro Nutrition' },
  'qnutri':            { label: 'Qnutri' },
  'rapid-fuse':        { label: 'Rapid Fuse' },
  'suplementsfort':    { label: 'Suplementsfort' },
  'midea':             { label: 'Midea' },
  'samsung':           { label: 'Samsung' },
  'the-one-supps':     { label: 'The One Supps' },
  'thermo-muscle':     { label: 'Thermo Muscle' },
  'tramontina':        { label: 'Tramontina' },
  'trends-nutrition':  { label: 'Trends Nutrition' },
  'trendplain':        { label: 'TrendPlain' },
  'ultra':             { label: 'Ultra' },
  'unique':            { label: 'Unique' },
  'vhita':             { label: 'Vhita' },
  'vitafor':           { label: 'Vitafor' },
};

// ───────────────────────────────────────
// Mapa ASIN → taxonomia
// ───────────────────────────────────────
export const taxonomia: Record<string, ProdutoTaxonomia> = {
  // ── Creatinas ──
  'B081QQFXMK': { tipo: 'suplemento', categoria: 'creatina', marca: 'dark-lab' },
  'B0CF71CJ2L': { tipo: 'suplemento', categoria: 'creatina', marca: 'dark-lab' },
  'B089PGDWG5': { tipo: 'suplemento', categoria: 'creatina', marca: 'ftw' },
  'B0D9MPQ9CP': { tipo: 'suplemento', categoria: 'creatina', marca: 'nutrends' },
  'B00TF3XT4M': { tipo: 'suplemento', categoria: 'creatina', marca: 'optimum-nutrition' },
  'B0F2NBXXRS': { tipo: 'suplemento', categoria: 'creatina', marca: 'the-one-supps' },

  // ── Whey Protein ──
  'B0CLTNBWFL': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'suplementsfort' },
  'B07L5WJPXR': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'bodyaction' },
  'B07MFM36QT': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'bodyaction' },
  'B0DFQN5MT4': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'dark-lab' },
  'B07MC12N2N': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'integralmedica' },
  'B08525PHGW': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'integralmedica' },
  'B0DFQM2GJZ': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'dark-lab' },
  'B0B644TPN3': { tipo: 'suplemento', categoria: 'whey-protein', marca: 'vitafor' }, // estava no post de iogurteira por engano

  // ── BCAA ──
  'B0CLB2QLZ2': { tipo: 'suplemento', categoria: 'bcaa', marca: 'trends-nutrition' },
  'B07NF8X53B': { tipo: 'suplemento', categoria: 'bcaa', marca: '3vs-nutrition' },
  'B082XF3PMP': { tipo: 'suplemento', categoria: 'bcaa', marca: '3vs-nutrition' },

  // ── Glutamina ──
  'B0DLB9H9MD': { tipo: 'suplemento', categoria: 'glutamina', marca: 'nutri-saude' },
  'B0FY8HCG1V': { tipo: 'suplemento', categoria: 'glutamina', marca: 'qnutri' },

  // ── Pré-treino ──
  'B0FJTCRZNK': { tipo: 'suplemento', categoria: 'pre-treino', marca: 'rapid-fuse' },
  'B0DTV6JSNK': { tipo: 'suplemento', categoria: 'pre-treino', marca: 'thermo-muscle' },
  'B0DV788XG4': { tipo: 'suplemento', categoria: 'pre-treino', marca: 'insane' },
  'B09SJT7751': { tipo: 'suplemento', categoria: 'pre-treino', marca: 'ftw' },
  'B0FTGBXH71': { tipo: 'suplemento', categoria: 'pre-treino', marca: 'ftw' },
  'B0GS7JG1P5': { tipo: 'suplemento', categoria: 'pre-treino', marca: 'ftw' },
  'B0FY3Z98MM': { tipo: 'suplemento', categoria: 'pre-treino', marca: 'easy-boost' },

  // ── Vitamina D3+K2 ──
  'B0DLLG9YQK': { tipo: 'suplemento', categoria: 'vitamina-d3-k2', marca: 'life-seeds' },
  'B09XJMX44T': { tipo: 'suplemento', categoria: 'vitamina-d3-k2', marca: 'vhita' },
  'B0FGFQM6QM': { tipo: 'suplemento', categoria: 'vitamina-d3-k2', marca: 'puro-nutrition' },
  'B0D5FM7B2D': { tipo: 'suplemento', categoria: 'vitamina-d3-k2', marca: 'ellym-nutrition' },
  'B0CZ2JQY3W': { tipo: 'suplemento', categoria: 'vitamina-d3-k2', marca: 'ellym-nutrition' },

  // ── Multivitamínico ──
  'B0DHWFK43F': { tipo: 'suplemento', categoria: 'multivitaminico', marca: 'ultra' },
  'B0FQHLZZF3': { tipo: 'suplemento', categoria: 'multivitaminico', marca: 'puro-nutrition' },

  // ── Air Fryer ──
  'B095YWH6PC': { tipo: 'equipamento', categoria: 'air-fryer', marca: 'cadence' },
  'B0CD9JLHTT': { tipo: 'equipamento', categoria: 'air-fryer', marca: 'mondial' },
  'B0CC3ZW7Q4': { tipo: 'equipamento', categoria: 'air-fryer', marca: 'electrolux' },

  // ── Panela de pressão ──
  'B0BZ8WKG61': { tipo: 'equipamento', categoria: 'panela-pressao', marca: 'electrolux' },
  'B076HYKFL7': { tipo: 'equipamento', categoria: 'panela-pressao', marca: 'electrolux' },
  'B0B4PPHG8G': { tipo: 'equipamento', categoria: 'panela-pressao', marca: 'ninja' },
  'B07TK5QZJG': { tipo: 'equipamento', categoria: 'panela-pressao', marca: 'dona-chefa' },
  'B076KJ5LPW': { tipo: 'acessorio',   categoria: 'pecas-reposicao', marca: 'tramontina' },

  // ── Iogurteira ──
  'B002BQ98EU': { tipo: 'equipamento', categoria: 'iogurteira', marca: 'euro-cuisine' },
  'B07SPH3BLY': { tipo: 'equipamento', categoria: 'iogurteira', marca: 'izumi' },
  'B09MP8BK8P': { tipo: 'equipamento', categoria: 'iogurteira', marca: 'joymech' },

  // ── Processador / acessórios cozinha ──
  'B0CJF94M8J': { tipo: 'acessorio',   categoria: 'utensilio-cozinha', marca: 'trendplain' },
  'B07QN1RW8K': { tipo: 'equipamento', categoria: 'processador',       marca: 'philco' },
  'B08XZTYXW1': { tipo: 'equipamento', categoria: 'processador',       marca: 'black-decker' },
  'B08CPLKQ32': { tipo: 'acessorio',   categoria: 'recipiente',        marca: 'gato-panda' },

  // ── Balança ──
  'B0F8G37Y56': { tipo: 'equipamento', categoria: 'balanca-cozinha', marca: 'generica' },
  'B08XX1F44R': { tipo: 'equipamento', categoria: 'balanca-cozinha', marca: 'unique' },

  // ── Espiralizador ──
  'B074BC9FT9': { tipo: 'equipamento', categoria: 'espiralizador', marca: 'mealthy' },

  // ── Geladeira (doméstica) ──
  // Nota: B07FY23K8B está no post "geladeira-consul-frost-free.md" mas o
  // produto é Brastemp (título indica Brastemp) — taxonomia reflete o produto, não o post.
  'B07FY23K8B': { tipo: 'equipamento', categoria: 'geladeira', marca: 'brastemp' },
  'B0B3PGGKVT': { tipo: 'equipamento', categoria: 'geladeira', marca: 'electrolux' },
  'B076B9ZB8C': { tipo: 'equipamento', categoria: 'geladeira', marca: 'consul' },

  // ── Geladeira Portátil / Frigobar ──
  'B000JLNBW4': { tipo: 'equipamento', categoria: 'geladeira-portatil', marca: 'polar' },
  'B0BPM7C8RT': { tipo: 'equipamento', categoria: 'geladeira-portatil', marca: 'bougerv' },
  'B075Z7RST7': { tipo: 'equipamento', categoria: 'geladeira-portatil', marca: 'black-decker' },
  'B0B3FCW6KQ': { tipo: 'equipamento', categoria: 'geladeira-portatil', marca: 'black-decker' },

  // ── Geladeira Inverter ──
  'B0D9P9V38B': { tipo: 'equipamento', categoria: 'geladeira', marca: 'electrolux' },
  'B0D1YP2X5W': { tipo: 'equipamento', categoria: 'geladeira', marca: 'electrolux' },
  'B0CL7XV8NN': { tipo: 'equipamento', categoria: 'geladeira', marca: 'electrolux' },
  'B00FB6JQB2': { tipo: 'equipamento', categoria: 'geladeira', marca: 'samsung' },

  // ── Ímãs de Geladeira ──
  'B0DFX7BQX9': { tipo: 'acessorio', categoria: 'ima-geladeira', marca: 'generica' },

  // ── Geladeira — novos silos 2026-05-06 ──
  'B076BCK5WX': { tipo: 'equipamento', categoria: 'geladeira', marca: 'consul' },
  'B07JGL1WH8': { tipo: 'equipamento', categoria: 'geladeira', marca: 'consul' },
  'B07K29F3SB': { tipo: 'equipamento', categoria: 'geladeira', marca: 'electrolux' },
  'B0DNR7TBTW': { tipo: 'equipamento', categoria: 'geladeira', marca: 'electrolux' },
  'B0B723VVR7': { tipo: 'equipamento', categoria: 'geladeira', marca: 'philco' },
  'B0F4RVF119': { tipo: 'equipamento', categoria: 'geladeira', marca: 'midea' },

  // ── Acessório elétrico para geladeira ──
  'B0C9DS7MCC': { tipo: 'acessorio', categoria: 'pecas-reposicao', marca: 'generica' },
};

// ───────────────────────────────────────
// Helpers
// ───────────────────────────────────────

export function getTaxonomia(asin: string): ProdutoTaxonomia | null {
  return taxonomia[asin] ?? null;
}

export function listAsinsByTipo(tipo: ProdutoTipo): string[] {
  return Object.entries(taxonomia)
    .filter(([, t]) => t.tipo === tipo)
    .map(([asin]) => asin);
}

export function listAsinsByCategoria(categoria: string): string[] {
  return Object.entries(taxonomia)
    .filter(([, t]) => t.categoria === categoria)
    .map(([asin]) => asin);
}

export function listAsinsByMarca(marca: string): string[] {
  return Object.entries(taxonomia)
    .filter(([, t]) => t.marca === marca)
    .map(([asin]) => asin);
}

export function listTiposComProdutos(): ProdutoTipo[] {
  const tipos = new Set<ProdutoTipo>();
  for (const t of Object.values(taxonomia)) tipos.add(t.tipo);
  return Object.keys(TIPOS).filter((k) => tipos.has(k as ProdutoTipo)) as ProdutoTipo[];
}

export function listCategoriasComProdutos(): string[] {
  const cats = new Set<string>();
  for (const t of Object.values(taxonomia)) cats.add(t.categoria);
  return Object.keys(CATEGORIAS).filter((k) => cats.has(k));
}

export function listMarcasComProdutos(): string[] {
  const ms = new Set<string>();
  for (const t of Object.values(taxonomia)) ms.add(t.marca);
  return Object.keys(MARCAS).filter((k) => ms.has(k));
}
