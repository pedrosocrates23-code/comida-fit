// @uraume - Dynamic sitemap endpoint
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async () => {
  const receitas = await getCollection('receitas');
  const blogPosts = await getCollection('blog');

  const categorias = [
    'cafe-da-manha', 'almoco-fit', 'lanches-saudaveis',
    'jantar-low-carb', 'sobremesas-fit',
    'smoothies-e-sucos', 'pre-treino', 'pos-treino',
  ];

  // Produtos (extraidos dos posts do blog)
  const seenAsins = new Set<string>();
  const produtoPages: Array<{ url: string; priority: string; changefreq: string; lastmod: string }> = [];
  for (const post of blogPosts) {
    if (!post.data.produtos?.length) continue;
    for (const produto of post.data.produtos) {
      if (seenAsins.has(produto.asin)) continue;
      seenAsins.add(produto.asin);
      produtoPages.push({
        url:        `/produtos/${produto.asin}/`,
        priority:   '0.8',
        changefreq: 'weekly',
        lastmod:    post.data.publishDate.toISOString().split('T')[0],
      });
    }
  }

  const blogPages = blogPosts.map((p) => ({
    url:        `/blog/${p.slug}/`,
    priority:   '0.8',
    changefreq: 'weekly',
    lastmod:    p.data.publishDate.toISOString().split('T')[0],
  }));

  const staticPages = [
    { url: '/',          priority: '1.0', changefreq: 'weekly',  lastmod: '' },
    { url: '/receitas/', priority: '0.9', changefreq: 'weekly',  lastmod: '' },
    { url: '/blog/',     priority: '0.9', changefreq: 'weekly',  lastmod: '' },
    { url: '/produtos/', priority: '0.9', changefreq: 'weekly',  lastmod: '' },
    { url: '/sobre/',    priority: '0.5', changefreq: 'monthly', lastmod: '' },
  ];

  const categoriaPages = categorias.map((slug) => ({
    url:        `/categoria/${slug}/`,
    priority:   '0.8',
    changefreq: 'weekly',
    lastmod:    '',
  }));

  const receitaPages = receitas.map((r) => ({
    url:        `/receitas/${r.slug}/`,
    priority:   '0.7',
    changefreq: 'weekly',
    lastmod:    r.data.publishDate.toISOString().split('T')[0],
  }));

  const allPages = [...staticPages, ...categoriaPages, ...receitaPages, ...blogPages, ...produtoPages];
  const base     = 'https://melhoresreceitasfit.com.br';
  const today    = new Date().toISOString().split('T')[0];

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset
  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
    http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
${allPages
  .map(
    (p) => `  <url>
    <loc>${base}${p.url}</loc>
    <lastmod>${p.lastmod || today}</lastmod>
    <changefreq>${p.changefreq}</changefreq>
    <priority>${p.priority}</priority>
  </url>`,
  )
  .join('\n')}
</urlset>`;

  return new Response(xml, {
    headers: {
      'Content-Type':  'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=86400',
    },
  });
};
