import { defineConfig } from 'astro/config';
import { visit } from 'unist-util-visit';

// Plugin rehype: adiciona target="_blank" rel="noopener noreferrer" apenas em links externos
function rehypeExternalLinksNewTab() {
  return (tree) => {
    visit(tree, 'element', (node) => {
      if (node.tagName === 'a' && node.properties?.href) {
        const href = String(node.properties.href);
        if (href.startsWith('http') || href.startsWith('//')) {
          node.properties.target = '_blank';
          node.properties.rel = 'noopener noreferrer';
        }
      }
    });
  };
}

export default defineConfig({
  markdown: {
    rehypePlugins: [rehypeExternalLinksNewTab],
  },
  site: 'https://melhoresreceitasfit.com.br',
  output: 'static',
  trailingSlash: 'ignore',
  integrations: [],
  image: {
    domains: ['melhoresreceitasfit.com.br'],
  },
  build: {
    assets: '_assets',
    inlineStylesheets: 'always',
  },
  compressHTML: true,
  redirects: {
    // 301 redirects: URLs antigas (raiz) para nova arquitetura (/receitas/)
    // Gerado a partir do Coverage Drilldown do Google Search Console — 2026-04-15
    // Nota: trailing slash tratado por trailingSlash: 'ignore' — apenas uma entrada por URL
    '/panquecas-fininhas-sem-gluten-e-lactose-free': { destination: '/receitas/panquecas-fininhas-sem-gluten-e-lactose-free/', status: 301 },
    '/mini-pizza-de-abobrinha':                       { destination: '/receitas/mini-pizza-de-abobrinha/', status: 301 },
    '/bolo-de-limao-lowcarb':                         { destination: '/receitas/bolo-de-limao-lowcarb/', status: 301 },
    '/suco-para-desinchar':                           { destination: '/receitas/suco-para-desinchar/', status: 301 },
    '/shake-detox-de-banana':                         { destination: '/receitas/shake-detox-de-banana/', status: 301 },
    '/bolo-de-chocolate-low-carb':                    { destination: '/receitas/bolo-de-chocolate-low-carb/', status: 301 },
    '/receitas-fitness':                              { destination: '/receitas/receitas-fitness/', status: 301 },
    '/bolo-mousse-de-chocolate':                      { destination: '/receitas/bolo-mousse-de-chocolate/', status: 301 },
    '/mousse-de-maracuja-fit':                        { destination: '/receitas/mousse-de-maracuja-fit/', status: 301 },
    '/pudim-de-coco-low-carb':                        { destination: '/receitas/pudim-de-coco-low-carb/', status: 301 },
    '/receita-de-torta-salgada-low-carb':             { destination: '/receitas/receita-de-torta-salgada-low-carb/', status: 301 },
    '/receita-low-carb-facil':                        { destination: '/receitas/receita-low-carb-facil/', status: 301 },
    '/como-fazer-cuscuz-fit':                         { destination: '/receitas/como-fazer-cuscuz-fit/', status: 301 },
    '/receita-de-bolo-low-carb-facil':                { destination: '/receitas/receita-de-bolo-low-carb-facil/', status: 301 },
    '/receitas-low-carb-com-espinafre':               { destination: '/receitas/receitas-low-carb-com-espinafre/', status: 301 },
    '/receita-de-bolo-de-aniversario-low-carb':       { destination: '/receitas/receita-de-bolo-de-aniversario-low-carb/', status: 301 },
    '/danette-low-carb':                              { destination: '/receitas/danette-low-carb/', status: 301 },
    '/mousse-de-morango-fit':                         { destination: '/receitas/mousse-de-morango-fit/', status: 301 },
    '/receita-de-vitamina-saudavel':                  { destination: '/receitas/receita-de-vitamina-saudavel/', status: 301 },
    '/casadinho-fit':                                 { destination: '/receitas/casadinho-fit/', status: 301 },
    '/receita-de-bolo-low-carb':                      { destination: '/receitas/receita-de-bolo-low-carb/', status: 301 },
    '/receita-de-bolo-de-chocolate-low-carb':         { destination: '/receitas/receita-de-bolo-de-chocolate-low-carb/', status: 301 },
    '/receitas-saudaveis-e-rapidas':                  { destination: '/receitas/receitas-saudaveis-e-rapidas/', status: 301 },
    '/bolo-de-coco-gelado':                           { destination: '/receitas/bolo-de-coco-gelado/', status: 301 },
    '/bolo-fit-saboroso':                             { destination: '/receitas/bolo-fit-saboroso/', status: 301 },
    '/5-receitas-de-quiche-low-carb':                 { destination: '/receitas/5-receitas-de-quiche-low-carb/', status: 301 },
    '/receita-fit-e-saudavel':                        { destination: '/receitas/receita-fit-e-saudavel/', status: 301 },
    '/receitas-fit-com-batata-doce':                  { destination: '/receitas/receitas-fit-com-batata-doce/', status: 301 },
    '/barrinha-de-chocolate-com-coco-low-carb':       { destination: '/receitas/barrinha-de-chocolate-com-coco-low-carb/', status: 301 },
    '/enroladinho-de-banana':                         { destination: '/receitas/enroladinho-de-banana/', status: 301 },
    '/bolo-de-chocolate-fit':                         { destination: '/receitas/bolo-de-chocolate-fit/', status: 301 },
    '/bolo-de-maca-canela-e-frutas-secas':            { destination: '/receitas/bolo-de-maca-canela-e-frutas-secas/', status: 301 },
    '/chips-de-banana':                               { destination: '/receitas/chips-de-banana/', status: 301 },
    '/bolo-de-caneca-low-carb-de-chocolate':          { destination: '/receitas/bolo-de-caneca-low-carb-de-chocolate/', status: 301 },
    '/10-receitas-de-bolo-de-banana-fit':             { destination: '/receitas/10-receitas-de-bolo-de-banana-fit/', status: 301 },
    '/bolo-de-laranja-fit':                           { destination: '/receitas/bolo-de-laranja-fit/', status: 301 },
    '/macarrao-de-abobrinha-com-molho-branco':        { destination: '/receitas/macarrao-de-abobrinha-com-molho-branco/', status: 301 },

    // Novas receitas criadas — Coverage Drilldown 2026-05-06
    '/receitas-de-escondidinho-fit-e-low-carb':       { destination: '/receitas/receitas-de-escondidinho-fit-e-low-carb/', status: 301 },
    '/receitas-de-cafe-da-manha-low-carb-7-opcoes':   { destination: '/receitas/receitas-de-cafe-da-manha-low-carb-7-opcoes/', status: 301 },
    '/receitas-de-salgados-low-carb':                 { destination: '/receitas/receitas-de-salgados-low-carb/', status: 301 },
    '/pao-low-carb':                                  { destination: '/receitas/pao-low-carb/', status: 301 },
    '/salpicao-low-carb':                             { destination: '/receitas/salpicao-low-carb/', status: 301 },
    '/bolo-de-coco-fit':                              { destination: '/receitas/bolo-de-coco-fit/', status: 301 },
    '/7-receitas-de-bolo-de-cenoura-fit':             { destination: '/receitas/7-receitas-de-bolo-de-cenoura-fit/', status: 301 },
    '/brownie-fit-3-receitas-deliciosas':             { destination: '/receitas/brownie-fit-3-receitas-deliciosas/', status: 301 },
    '/nuggets-caseiro-fit':                           { destination: '/receitas/nuggets-caseiro-fit/', status: 301 },
    '/crepioca-com-crosta-de-queijo':                 { destination: '/receitas/crepioca-com-crosta-de-queijo/', status: 301 },
    '/guacamole':                                     { destination: '/receitas/guacamole/', status: 301 },
    '/torta-de-frango-com-queijo-fit':                { destination: '/receitas/torta-de-frango-com-queijo-fit/', status: 301 },
    '/omelete-de-espinafre':                          { destination: '/receitas/omelete-de-espinafre/', status: 301 },
    '/omelete-de-forno-com-queijo':                   { destination: '/receitas/omelete-de-forno-com-queijo/', status: 301 },
    '/receita-de-coxinha-fit':                        { destination: '/receitas/receita-de-coxinha-fit/', status: 301 },
    '/pao-low-carb-delicioso':                        { destination: '/receitas/pao-low-carb-delicioso/', status: 301 },
    '/mousse-de-abacate-proteico':                    { destination: '/receitas/mousse-de-abacate-proteico/', status: 301 },
    '/paozinho-crocante-low-carb':                    { destination: '/receitas/paozinho-crocante-low-carb/', status: 301 },
    '/bolo-de-cenoura-low-carb':                      { destination: '/receitas/bolo-de-cenoura-low-carb/', status: 301 },
    '/hamburguer-de-cenoura-e-abobrinha':             { destination: '/receitas/hamburguer-de-cenoura-e-abobrinha/', status: 301 },

    // Categorias do WordPress antigo — redirecionam para categorias equivalentes
    '/blog/categoria/emagrecimento':                  { destination: '/categoria/jantar-low-carb/', status: 301 },
    '/blog/categoria/dicas-fit':                      { destination: '/categoria/lanches-saudaveis/', status: 301 },
    '/blog/categoria/saude':                          { destination: '/categoria/sobremesas-fit/', status: 301 },

    // Feed WordPress — redireciona para home
    '/ensopado-de-lentilha-com-salsa-verde/feed':     { destination: '/receitas/ensopado-de-lentilha-com-salsa-verde/', status: 301 },
  },
});
