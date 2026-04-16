/**
 * add-internal-links.mjs
 * Adiciona seção "Leia também" com links internos em todos os artigos de receita.
 * - Mínimo 2 links por página
 * - Links receita↔receita temáticos + links para blog de suplementos onde relevante
 * - Não modifica páginas de blog/afiliados
 * - Idempotente: pula arquivos que já têm "Leia também"
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const RECEITAS_DIR = path.join(__dirname, '..', 'src', 'content', 'receitas');

// ── Títulos amigáveis para anchor text ────────────────────────────────────────
const TITLES = {
  // Receitas
  'agua-detox-de-pepino-e-hortela':        'Agua Detox de Pepino e Hortela',
  'arroz-integral-com-feijao-carioca':     'Arroz Integral com Feijao Carioca',
  'banana-com-pasta-de-amendoim':          'Banana com Pasta de Amendoim',
  'barrinha-de-cereal-caseira':            'Barrinha de Cereal Caseira',
  'barrinha-de-chocolate-com-coco-low-carb': 'Barrinha de Chocolate com Coco Low Carb',
  'batata-doce-assada-com-mel':            'Batata Doce Assada com Mel',
  'biscoito-de-aveia-e-banana':            'Biscoito de Aveia e Banana',
  'bolinho-de-atum-assado':                'Bolinho de Atum Assado',
  'bolo-de-caneca-low-carb-de-chocolate':  'Bolo de Caneca Low Carb de Chocolate',
  'bolo-de-chocolate-fit':                 'Bolo de Chocolate Fit',
  'bolo-de-chocolate-low-carb':            'Bolo de Chocolate Low Carb',
  'bolo-de-coco-gelado':                   'Bolo de Coco Gelado',
  'bolo-de-laranja-fit':                   'Bolo de Laranja Fit',
  'bolo-de-limao-lowcarb':                 'Bolo de Limao Low Carb',
  'bolo-de-maca-canela-e-frutas-secas':    'Bolo de Maca com Canela e Frutas Secas',
  'bolo-fit-saboroso':                     'Bolo Fit Saboroso',
  'bolo-mousse-de-chocolate':              'Bolo Mousse de Chocolate',
  'brownie-de-batata-doce':                'Brownie de Batata Doce',
  'camarao-grelhado-com-salada-verde':     'Camarao Grelhado com Salada Verde',
  'carne-moida-com-abobrinha':             'Carne Moida com Abobrinha',
  'casadinho-fit':                         'Casadinho Fit',
  'chips-de-banana':                       'Chips de Banana Fit Assados',
  'chips-de-batata-doce-assada':           'Chips de Batata Doce Assada',
  'como-fazer-cuscuz-fit':                 'Como Fazer Cuscuz Fit',
  'crepioca-de-ovos':                      'Crepioca de Ovos',
  'danette-low-carb':                      'Danette Low Carb Caseiro',
  'enroladinho-de-banana':                 'Enroladinho de Banana',
  'frango-ao-molho-de-iogurte':            'Frango ao Molho de Iogurte',
  'frango-desfiado-com-arroz-integral':    'Frango Desfiado com Arroz Integral',
  'frango-grelhado-com-legumes-no-vapor':  'Frango Grelhado com Legumes no Vapor',
  'fruta-com-castanhas-pre-treino':        'Fruta com Castanhas Pre-Treino',
  'gelatina-proteica-de-morango':          'Gelatina Proteica de Morango',
  'hamburguer-de-grao-de-bico':            'Hamburguer de Grao de Bico',
  'iogurte-grego-com-granola-caseira':     'Iogurte Grego com Granola Caseira',
  'iogurte-proteico-com-frutas':           'Iogurte Proteico com Frutas',
  'macarrao-de-abobrinha-com-molho-branco':'Macarrao de Abobrinha com Molho Branco',
  'mingau-de-aveia-com-frutas-vermelhas':  'Mingau de Aveia com Frutas Vermelhas',
  'mini-pizza-de-abobrinha':               'Mini Pizza de Abobrinha',
  'mousse-de-maracuja-fit':                'Mousse de Maracuja Fit',
  'mousse-de-morango-fit':                 'Mousse de Morango Fit',
  'muffin-de-proteina-de-chocolate':       'Muffin de Proteina de Chocolate',
  'omelete-de-espinafre-e-queijo-cottage': 'Omelete de Espinafre com Queijo Cottage',
  'omelete-pos-treino-de-clara':           'Omelete Pos-Treino de Clara',
  'omelete-recheada-de-legumes':           'Omelete Recheada de Legumes',
  'ovos-mexidos-com-abacate':              'Ovos Mexidos com Abacate',
  'palito-de-cenoura-com-homus':           'Palito de Cenoura com Homus',
  'panqueca-de-banana-sem-farinha':        'Panqueca de Banana Sem Farinha',
  'panquecas-fininhas-sem-gluten-e-lactose-free': 'Panquecas Fininhas Sem Gluten e Lactose',
  'pudim-de-coco-low-carb':               'Pudim de Coco Low Carb',
  'pudim-fit-sem-lactose':                 'Pudim Fit Sem Lactose',
  'quinoa-com-legumes-grelhados':          'Quinoa com Legumes Grelhados',
  'receita-de-bolo-de-aniversario-low-carb':'Bolo de Aniversario Low Carb',
  'receita-de-bolo-de-chocolate-low-carb': 'Receita de Bolo de Chocolate Low Carb',
  'receita-de-bolo-low-carb-facil':        'Receita de Bolo Low Carb Facil',
  'receita-de-bolo-low-carb':              'Receita de Bolo Low Carb',
  'receita-de-torta-salgada-low-carb':     'Torta Salgada Low Carb',
  'receita-de-vitamina-saudavel':          'Receita de Vitamina Saudavel',
  'receita-fit-e-saudavel':                'Receita Fit e Saudavel',
  'receita-low-carb-facil':               'Receita Low Carb Facil',
  'receitas-fit-com-batata-doce':          'Receitas Fit com Batata Doce',
  'receitas-fitness':                      'Receitas Fitness para o Dia a Dia',
  'receitas-low-carb-com-espinafre':       'Receitas Low Carb com Espinafre',
  'receitas-saudaveis-e-rapidas':          'Receitas Saudaveis e Rapidas',
  'risoto-de-couve-flor-com-frango':       'Risoto de Couve-Flor com Frango',
  'salada-de-atum-com-grao-de-bico':       'Salada de Atum com Grao de Bico',
  'salmao-assado-com-aspargos':            'Salmao Assado com Aspargos',
  'sanduiche-de-atum-integral':            'Sanduiche de Atum Integral',
  'shake-de-aveia-pre-treino':             'Shake de Aveia Pre-Treino',
  'shake-detox-de-banana':                 'Shake Detox de Banana',
  'shake-proteico-de-chocolate':           'Shake Proteico de Chocolate',
  'shake-whey-com-banana':                 'Shake de Whey com Banana',
  'smoothie-bowl-de-acai-fit':             'Smoothie Bowl de Acai Fit',
  'smoothie-de-morango-com-iogurte':       'Smoothie de Morango com Iogurte',
  'smoothie-verde-detox':                  'Smoothie Verde Detox',
  'sopa-de-legumes-proteica':              'Sopa de Legumes Proteica',
  'sorvete-de-banana-com-pasta-de-amendoim':'Sorvete de Banana com Pasta de Amendoim',
  'strogonoff-fit-de-frango':              'Strogonoff Fit de Frango',
  'suco-de-beterraba-com-gengibre':        'Suco de Beterraba com Gengibre',
  'suco-para-desinchar':                   'Suco para Desinchar',
  'tapioca-de-frango-desfiado':            'Tapioca de Frango Desfiado',
  'tilapia-assada-com-ervas':              'Tilapia Assada com Ervas',
  'torrada-integral-com-ovos':             'Torrada Integral com Ovos',
  'trufa-de-chocolate-com-oleo-de-coco':   'Trufa de Chocolate com Oleo de Coco',
  'vitamina-de-mamao-com-linhaca':         'Vitamina de Mamao com Linhaca',
  'wrap-de-frango-com-alface':             'Wrap de Frango com Alface',
  'zoodles-com-pesto-de-manjericao':       'Zoodles com Pesto de Manjericao',
  '5-receitas-de-quiche-low-carb':         '5 Receitas de Quiche Low Carb',
  '10-receitas-de-bolo-de-banana-fit':     '10 Receitas de Bolo de Banana Fit',
  // Blog (suplementos)
  'blog/melhores-proteinas-2026':          'Melhores Whey Proteins 2025: Comparativo Completo',
  'blog/melhores-pre-treino-2026':         'Melhores Pre-Treinos 2025: Comparativo Completo',
  'blog/melhores-creatinas-2026':          'Melhores Creatinas 2025: Comparativo Completo',
  'blog/melhores-aminoacidos-2026':        'Melhores BCAAs e Aminoacidos 2025',
  'blog/proteinas-na-dieta-fit':           'Proteinas na Dieta Fit: Quanto Voce Precisa?',
  'blog/carboidratos-bons-e-ruins':        'Carboidratos Bons e Ruins: O Que a Ciencia Diz',
};

// Converte slug/blog-path para href absoluta
function href(key) {
  if (key.startsWith('blog/')) return `/${key}`;
  return `/receitas/${key}`;
}

// ── Mapa slug → links [chave, chave, chave] ───────────────────────────────────
const LINKS_MAP = {
  'agua-detox-de-pepino-e-hortela': [
    'suco-para-desinchar',
    'smoothie-verde-detox',
    'suco-de-beterraba-com-gengibre',
  ],
  'arroz-integral-com-feijao-carioca': [
    'frango-grelhado-com-legumes-no-vapor',
    'receitas-saudaveis-e-rapidas',
    'blog/proteinas-na-dieta-fit',
  ],
  'banana-com-pasta-de-amendoim': [
    'panqueca-de-banana-sem-farinha',
    'chips-de-banana',
    'sorvete-de-banana-com-pasta-de-amendoim',
  ],
  'barrinha-de-cereal-caseira': [
    'barrinha-de-chocolate-com-coco-low-carb',
    'fruta-com-castanhas-pre-treino',
    'blog/melhores-proteinas-2026',
  ],
  'barrinha-de-chocolate-com-coco-low-carb': [
    'barrinha-de-cereal-caseira',
    'trufa-de-chocolate-com-oleo-de-coco',
    'blog/melhores-proteinas-2026',
  ],
  'batata-doce-assada-com-mel': [
    'chips-de-batata-doce-assada',
    'receitas-fit-com-batata-doce',
    'brownie-de-batata-doce',
  ],
  'biscoito-de-aveia-e-banana': [
    'panqueca-de-banana-sem-farinha',
    '10-receitas-de-bolo-de-banana-fit',
    'barrinha-de-cereal-caseira',
  ],
  'bolinho-de-atum-assado': [
    'salada-de-atum-com-grao-de-bico',
    'sanduiche-de-atum-integral',
    'blog/proteinas-na-dieta-fit',
  ],
  'bolo-de-caneca-low-carb-de-chocolate': [
    'bolo-de-chocolate-fit',
    'bolo-de-chocolate-low-carb',
    'danette-low-carb',
  ],
  'bolo-de-chocolate-fit': [
    'bolo-de-caneca-low-carb-de-chocolate',
    'receita-de-bolo-de-chocolate-low-carb',
    'bolo-mousse-de-chocolate',
  ],
  'bolo-de-chocolate-low-carb': [
    'bolo-de-chocolate-fit',
    'receita-de-bolo-de-chocolate-low-carb',
    'brownie-de-batata-doce',
  ],
  'bolo-de-coco-gelado': [
    'pudim-de-coco-low-carb',
    'bolo-fit-saboroso',
    'receita-de-bolo-low-carb',
  ],
  'bolo-de-laranja-fit': [
    'bolo-de-limao-lowcarb',
    'bolo-fit-saboroso',
    'receita-de-bolo-de-aniversario-low-carb',
  ],
  'bolo-de-limao-lowcarb': [
    'bolo-de-laranja-fit',
    'bolo-fit-saboroso',
    '10-receitas-de-bolo-de-banana-fit',
  ],
  'bolo-de-maca-canela-e-frutas-secas': [
    'bolo-de-laranja-fit',
    '10-receitas-de-bolo-de-banana-fit',
    'receita-de-bolo-low-carb-facil',
  ],
  'bolo-fit-saboroso': [
    'bolo-de-laranja-fit',
    'receita-de-bolo-low-carb',
    'bolo-de-chocolate-fit',
  ],
  'bolo-mousse-de-chocolate': [
    'danette-low-carb',
    'mousse-de-morango-fit',
    'bolo-de-chocolate-fit',
  ],
  'brownie-de-batata-doce': [
    'batata-doce-assada-com-mel',
    'chips-de-batata-doce-assada',
    'bolo-de-chocolate-low-carb',
  ],
  'camarao-grelhado-com-salada-verde': [
    'salmao-assado-com-aspargos',
    'tilapia-assada-com-ervas',
    'blog/proteinas-na-dieta-fit',
  ],
  'carne-moida-com-abobrinha': [
    'macarrao-de-abobrinha-com-molho-branco',
    'mini-pizza-de-abobrinha',
    'zoodles-com-pesto-de-manjericao',
  ],
  'casadinho-fit': [
    'barrinha-de-chocolate-com-coco-low-carb',
    'trufa-de-chocolate-com-oleo-de-coco',
    'bolo-de-coco-gelado',
  ],
  'chips-de-banana': [
    'enroladinho-de-banana',
    'banana-com-pasta-de-amendoim',
    '10-receitas-de-bolo-de-banana-fit',
  ],
  'chips-de-batata-doce-assada': [
    'batata-doce-assada-com-mel',
    'receitas-fit-com-batata-doce',
    'palito-de-cenoura-com-homus',
  ],
  'como-fazer-cuscuz-fit': [
    'receita-low-carb-facil',
    'receitas-saudaveis-e-rapidas',
    'arroz-integral-com-feijao-carioca',
  ],
  'crepioca-de-ovos': [
    'omelete-pos-treino-de-clara',
    'tapioca-de-frango-desfiado',
    'panquecas-fininhas-sem-gluten-e-lactose-free',
  ],
  'danette-low-carb': [
    'pudim-de-coco-low-carb',
    'mousse-de-morango-fit',
    'bolo-mousse-de-chocolate',
  ],
  'enroladinho-de-banana': [
    'chips-de-banana',
    'banana-com-pasta-de-amendoim',
    'biscoito-de-aveia-e-banana',
  ],
  'frango-ao-molho-de-iogurte': [
    'frango-grelhado-com-legumes-no-vapor',
    'frango-desfiado-com-arroz-integral',
    'blog/proteinas-na-dieta-fit',
  ],
  'frango-desfiado-com-arroz-integral': [
    'frango-ao-molho-de-iogurte',
    'tapioca-de-frango-desfiado',
    'wrap-de-frango-com-alface',
  ],
  'frango-grelhado-com-legumes-no-vapor': [
    'frango-ao-molho-de-iogurte',
    'frango-desfiado-com-arroz-integral',
    'blog/proteinas-na-dieta-fit',
  ],
  'fruta-com-castanhas-pre-treino': [
    'barrinha-de-cereal-caseira',
    'shake-de-aveia-pre-treino',
    'blog/melhores-pre-treino-2026',
  ],
  'gelatina-proteica-de-morango': [
    'mousse-de-morango-fit',
    'pudim-fit-sem-lactose',
    'smoothie-de-morango-com-iogurte',
  ],
  'hamburguer-de-grao-de-bico': [
    'salada-de-atum-com-grao-de-bico',
    'quinoa-com-legumes-grelhados',
    'blog/proteinas-na-dieta-fit',
  ],
  'iogurte-grego-com-granola-caseira': [
    'iogurte-proteico-com-frutas',
    'mingau-de-aveia-com-frutas-vermelhas',
    'smoothie-bowl-de-acai-fit',
  ],
  'iogurte-proteico-com-frutas': [
    'iogurte-grego-com-granola-caseira',
    'smoothie-de-morango-com-iogurte',
    'blog/melhores-proteinas-2026',
  ],
  'macarrao-de-abobrinha-com-molho-branco': [
    'mini-pizza-de-abobrinha',
    'zoodles-com-pesto-de-manjericao',
    'carne-moida-com-abobrinha',
  ],
  'mingau-de-aveia-com-frutas-vermelhas': [
    'iogurte-grego-com-granola-caseira',
    'biscoito-de-aveia-e-banana',
    'smoothie-bowl-de-acai-fit',
  ],
  'mini-pizza-de-abobrinha': [
    'macarrao-de-abobrinha-com-molho-branco',
    'carne-moida-com-abobrinha',
    '5-receitas-de-quiche-low-carb',
  ],
  'mousse-de-maracuja-fit': [
    'mousse-de-morango-fit',
    'pudim-fit-sem-lactose',
    'gelatina-proteica-de-morango',
  ],
  'mousse-de-morango-fit': [
    'mousse-de-maracuja-fit',
    'gelatina-proteica-de-morango',
    'smoothie-de-morango-com-iogurte',
  ],
  'muffin-de-proteina-de-chocolate': [
    'bolo-de-caneca-low-carb-de-chocolate',
    'biscoito-de-aveia-e-banana',
    'blog/melhores-proteinas-2026',
  ],
  'omelete-de-espinafre-e-queijo-cottage': [
    'omelete-pos-treino-de-clara',
    'receitas-low-carb-com-espinafre',
    'ovos-mexidos-com-abacate',
  ],
  'omelete-pos-treino-de-clara': [
    'omelete-de-espinafre-e-queijo-cottage',
    'crepioca-de-ovos',
    'blog/melhores-pre-treino-2026',
  ],
  'omelete-recheada-de-legumes': [
    'omelete-de-espinafre-e-queijo-cottage',
    'ovos-mexidos-com-abacate',
    'quinoa-com-legumes-grelhados',
  ],
  'ovos-mexidos-com-abacate': [
    'omelete-de-espinafre-e-queijo-cottage',
    'torrada-integral-com-ovos',
    'crepioca-de-ovos',
  ],
  'palito-de-cenoura-com-homus': [
    'chips-de-batata-doce-assada',
    'fruta-com-castanhas-pre-treino',
    'salada-de-atum-com-grao-de-bico',
  ],
  'panqueca-de-banana-sem-farinha': [
    'biscoito-de-aveia-e-banana',
    'panquecas-fininhas-sem-gluten-e-lactose-free',
    '10-receitas-de-bolo-de-banana-fit',
  ],
  'panquecas-fininhas-sem-gluten-e-lactose-free': [
    'panqueca-de-banana-sem-farinha',
    'crepioca-de-ovos',
    'receitas-saudaveis-e-rapidas',
  ],
  'pudim-de-coco-low-carb': [
    'pudim-fit-sem-lactose',
    'bolo-de-coco-gelado',
    'danette-low-carb',
  ],
  'pudim-fit-sem-lactose': [
    'pudim-de-coco-low-carb',
    'gelatina-proteica-de-morango',
    'mousse-de-maracuja-fit',
  ],
  'quinoa-com-legumes-grelhados': [
    'arroz-integral-com-feijao-carioca',
    'omelete-recheada-de-legumes',
    'hamburguer-de-grao-de-bico',
  ],
  'receita-de-bolo-de-aniversario-low-carb': [
    'bolo-de-laranja-fit',
    'receita-de-bolo-low-carb-facil',
    'bolo-de-chocolate-fit',
  ],
  'receita-de-bolo-de-chocolate-low-carb': [
    'bolo-de-chocolate-low-carb',
    'bolo-de-chocolate-fit',
    'brownie-de-batata-doce',
  ],
  'receita-de-bolo-low-carb-facil': [
    'receita-de-bolo-low-carb',
    'bolo-fit-saboroso',
    'receita-de-bolo-de-aniversario-low-carb',
  ],
  'receita-de-bolo-low-carb': [
    'receita-de-bolo-low-carb-facil',
    'bolo-de-chocolate-low-carb',
    'bolo-fit-saboroso',
  ],
  'receita-de-torta-salgada-low-carb': [
    '5-receitas-de-quiche-low-carb',
    'mini-pizza-de-abobrinha',
    'receita-low-carb-facil',
  ],
  'receita-de-vitamina-saudavel': [
    'shake-detox-de-banana',
    'smoothie-verde-detox',
    'suco-para-desinchar',
  ],
  'receita-fit-e-saudavel': [
    'receitas-saudaveis-e-rapidas',
    'receitas-fitness',
    'receita-low-carb-facil',
  ],
  'receita-low-carb-facil': [
    'receitas-saudaveis-e-rapidas',
    'receita-fit-e-saudavel',
    'macarrao-de-abobrinha-com-molho-branco',
  ],
  'receitas-fit-com-batata-doce': [
    'batata-doce-assada-com-mel',
    'chips-de-batata-doce-assada',
    'brownie-de-batata-doce',
  ],
  'receitas-fitness': [
    'receitas-saudaveis-e-rapidas',
    'receita-fit-e-saudavel',
    'blog/proteinas-na-dieta-fit',
  ],
  'receitas-low-carb-com-espinafre': [
    'omelete-de-espinafre-e-queijo-cottage',
    'receita-low-carb-facil',
    'macarrao-de-abobrinha-com-molho-branco',
  ],
  'receitas-saudaveis-e-rapidas': [
    'receita-fit-e-saudavel',
    'receitas-fitness',
    'receita-low-carb-facil',
  ],
  'risoto-de-couve-flor-com-frango': [
    'carne-moida-com-abobrinha',
    'frango-grelhado-com-legumes-no-vapor',
    'blog/proteinas-na-dieta-fit',
  ],
  'salada-de-atum-com-grao-de-bico': [
    'bolinho-de-atum-assado',
    'sanduiche-de-atum-integral',
    'hamburguer-de-grao-de-bico',
  ],
  'salmao-assado-com-aspargos': [
    'tilapia-assada-com-ervas',
    'camarao-grelhado-com-salada-verde',
    'blog/proteinas-na-dieta-fit',
  ],
  'sanduiche-de-atum-integral': [
    'bolinho-de-atum-assado',
    'salada-de-atum-com-grao-de-bico',
    'wrap-de-frango-com-alface',
  ],
  'shake-de-aveia-pre-treino': [
    'shake-proteico-de-chocolate',
    'shake-whey-com-banana',
    'blog/melhores-pre-treino-2026',
  ],
  'shake-detox-de-banana': [
    'smoothie-verde-detox',
    'receita-de-vitamina-saudavel',
    'agua-detox-de-pepino-e-hortela',
  ],
  'shake-proteico-de-chocolate': [
    'shake-whey-com-banana',
    'muffin-de-proteina-de-chocolate',
    'blog/melhores-proteinas-2026',
  ],
  'shake-whey-com-banana': [
    'shake-proteico-de-chocolate',
    'shake-de-aveia-pre-treino',
    'blog/melhores-proteinas-2026',
  ],
  'smoothie-bowl-de-acai-fit': [
    'smoothie-de-morango-com-iogurte',
    'iogurte-grego-com-granola-caseira',
    'smoothie-verde-detox',
  ],
  'smoothie-de-morango-com-iogurte': [
    'smoothie-bowl-de-acai-fit',
    'mousse-de-morango-fit',
    'iogurte-proteico-com-frutas',
  ],
  'smoothie-verde-detox': [
    'agua-detox-de-pepino-e-hortela',
    'suco-para-desinchar',
    'shake-detox-de-banana',
  ],
  'sopa-de-legumes-proteica': [
    'carne-moida-com-abobrinha',
    'quinoa-com-legumes-grelhados',
    'blog/proteinas-na-dieta-fit',
  ],
  'sorvete-de-banana-com-pasta-de-amendoim': [
    'banana-com-pasta-de-amendoim',
    'chips-de-banana',
    'enroladinho-de-banana',
  ],
  'strogonoff-fit-de-frango': [
    'frango-ao-molho-de-iogurte',
    'frango-grelhado-com-legumes-no-vapor',
    'risoto-de-couve-flor-com-frango',
  ],
  'suco-de-beterraba-com-gengibre': [
    'agua-detox-de-pepino-e-hortela',
    'suco-para-desinchar',
    'smoothie-verde-detox',
  ],
  'suco-para-desinchar': [
    'agua-detox-de-pepino-e-hortela',
    'smoothie-verde-detox',
    'suco-de-beterraba-com-gengibre',
  ],
  'tapioca-de-frango-desfiado': [
    'crepioca-de-ovos',
    'frango-desfiado-com-arroz-integral',
    'wrap-de-frango-com-alface',
  ],
  'tilapia-assada-com-ervas': [
    'salmao-assado-com-aspargos',
    'camarao-grelhado-com-salada-verde',
    'blog/proteinas-na-dieta-fit',
  ],
  'torrada-integral-com-ovos': [
    'ovos-mexidos-com-abacate',
    'omelete-de-espinafre-e-queijo-cottage',
    'iogurte-grego-com-granola-caseira',
  ],
  'trufa-de-chocolate-com-oleo-de-coco': [
    'casadinho-fit',
    'barrinha-de-chocolate-com-coco-low-carb',
    'bolo-de-caneca-low-carb-de-chocolate',
  ],
  'vitamina-de-mamao-com-linhaca': [
    'receita-de-vitamina-saudavel',
    'smoothie-verde-detox',
    'shake-detox-de-banana',
  ],
  'wrap-de-frango-com-alface': [
    'sanduiche-de-atum-integral',
    'tapioca-de-frango-desfiado',
    'frango-desfiado-com-arroz-integral',
  ],
  'zoodles-com-pesto-de-manjericao': [
    'macarrao-de-abobrinha-com-molho-branco',
    'mini-pizza-de-abobrinha',
    'carne-moida-com-abobrinha',
  ],
  '5-receitas-de-quiche-low-carb': [
    'receita-de-torta-salgada-low-carb',
    'mini-pizza-de-abobrinha',
    'receita-low-carb-facil',
  ],
  '10-receitas-de-bolo-de-banana-fit': [
    'panqueca-de-banana-sem-farinha',
    'biscoito-de-aveia-e-banana',
    'bolo-de-laranja-fit',
  ],
};

// ── Gera o bloco markdown de links ────────────────────────────────────────────
function buildLinksBlock(keys) {
  const lines = keys.map((key) => {
    const title = TITLES[key] || key;
    const link = href(key);
    return `- [${title}](${link})`;
  });
  return `\n---\n\n## Leia Tambem\n\n${lines.join('\n')}\n`;
}

// ── Insere antes de "## Perguntas Frequentes" ou no final ─────────────────────
function insertLinks(content, block) {
  const faqPattern = /\n## Perguntas Frequentes/;
  if (faqPattern.test(content)) {
    return content.replace(faqPattern, `${block}\n## Perguntas Frequentes`);
  }
  return content.trimEnd() + '\n' + block;
}

// ── Main ───────────────────────────────────────────────────────────────────────
function main() {
  const files = fs.readdirSync(RECEITAS_DIR).filter((f) => f.endsWith('.md'));
  let updated = 0;
  let skipped = 0;
  let noMap = 0;

  for (const file of files) {
    const slug = file.replace('.md', '');
    const filePath = path.join(RECEITAS_DIR, file);
    const content = fs.readFileSync(filePath, 'utf8');

    // Pula se já tem a seção
    if (content.includes('## Leia Tambem')) {
      skipped++;
      continue;
    }

    const keys = LINKS_MAP[slug];
    if (!keys) {
      console.log(`⚠  Sem mapa: ${slug}`);
      noMap++;
      continue;
    }

    const block = buildLinksBlock(keys);
    const newContent = insertLinks(content, block);
    fs.writeFileSync(filePath, newContent, 'utf8');
    console.log(`✅ ${slug} (${keys.length} links)`);
    updated++;
  }

  console.log(`\n📊 Resultado: ${updated} atualizados, ${skipped} ja tinham links, ${noMap} sem mapa`);
}

main();
