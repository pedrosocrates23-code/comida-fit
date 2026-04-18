// @uraume - JSON-LD schema generation utilities
import type { CollectionEntry } from 'astro:content';

const SITE_URL  = 'https://melhoresreceitasfit.com.br';
const SITE_NAME = 'Melhores Receitas Fit';

const categoriaNomes: Record<string, string> = {
  'cafe-da-manha':      'Café da Manhã',
  'almoco-fit':         'Almoço Fit',
  'lanches-saudaveis':  'Lanches Saudáveis',
  'jantar-low-carb':    'Jantar Low Carb',
  'sobremesas-fit':     'Sobremesas Fit',
  'smoothies-e-sucos':  'Smoothies e Sucos',
  'pre-treino':         'Pré-Treino',
  'pos-treino':         'Pós-Treino',
};

/** Recipe schema - página individual */
export function buildRecipeSchema(receita: CollectionEntry<'receitas'>) {
  const { data, id: slug } = receita;
  const totalMinutos   = data.tempoPreparo + (data.tempoCozimento ?? 0);

  return {
    '@context': 'https://schema.org',
    '@type':    'Recipe',
    name:        data.title,
    description: data.description,
    image:       [`${SITE_URL}${data.image.src}`],
    author: {
      '@type': 'Organization',
      name:    SITE_NAME,
      url:     SITE_URL,
    },
    datePublished: data.publishDate.toISOString().split('T')[0],
    prepTime:  `PT${data.tempoPreparo}M`,
    ...(data.tempoCozimento && { cookTime: `PT${data.tempoCozimento}M` }),
    totalTime: `PT${totalMinutos}M`,
    recipeYield:    `${data.porcoes} ${data.porcoes === 1 ? 'porção' : 'porções'}`,
    recipeCategory: categoriaNomes[data.categoria] ?? data.categoria,
    recipeCuisine:  'Brasileira',
    keywords:       data.keywords.join(', '),
    url:            `${SITE_URL}/receitas/${slug}/`,
    nutrition: {
      '@type':              'NutritionInformation',
      calories:             `${data.calorias} calories`,
      proteinContent:       `${data.proteinas}g`,
      carbohydrateContent:  `${data.carboidratos}g`,
      fatContent:           `${data.gorduras}g`,
    },
    recipeIngredient:   data.ingredientes,
    recipeInstructions: data.instrucoes.map((text, i) => ({
      '@type':   'HowToStep',
      position:  i + 1,
      text,
    })),
    aggregateRating: {
      '@type':       'AggregateRating',
      ratingValue:   data.rating,
      reviewCount:   data.ratingCount,
      bestRating:    5,
      worstRating:   1,
    },
  };
}

/** WebSite schema + SearchBox - home */
export function buildWebSiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type':    'WebSite',
    name:       SITE_NAME,
    url:        SITE_URL,
    description: 'Site brasileiro de receitas saudáveis e fit com informações nutricionais completas.',
    inLanguage:  'pt-BR',
    potentialAction: {
      '@type':  'SearchAction',
      target: {
        '@type':       'EntryPoint',
        urlTemplate:   `${SITE_URL}/receitas/?q={search_term_string}`,
      },
      'query-input': 'required name=search_term_string',
    },
  };
}

/** BreadcrumbList - todas as páginas */
export function buildBreadcrumbSchema(items: { name: string; url: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type':    'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type':   'ListItem',
      position:  i + 1,
      name:      item.name,
      item:      item.url,
    })),
  };
}

/** CollectionPage - página de categoria */
export function buildCollectionPageSchema(
  categoriaSlug: string,
  total: number,
) {
  const nome = categoriaNomes[categoriaSlug] ?? categoriaSlug;
  const url  = `${SITE_URL}/categoria/${categoriaSlug}/`;
  return {
    '@context': 'https://schema.org',
    '@type':    'CollectionPage',
    name:       `Receitas de ${nome}: ${SITE_NAME}`,
    description: `${total} receitas fit de ${nome.toLowerCase()} com informações nutricionais completas.`,
    url,
    isPartOf: {
      '@type': 'WebSite',
      url:     SITE_URL,
      name:    SITE_NAME,
    },
  };
}
