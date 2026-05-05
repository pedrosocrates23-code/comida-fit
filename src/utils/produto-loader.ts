// ───────────────────────────────────────────────────────────────
// Loader compartilhado de produtos
// ───────────────────────────────────────────────────────────────
//
// Centraliza a coleta + dedupe (por ASIN) + slug long-tail dos
// produtos extraídos de src/content/blog/*.md, anexando a taxonomia.
// Usado por /produtos/index, /produtos/[slug], sitemap e páginas
// de taxonomia (/produtos/tipo/*, /categoria/*, /marca/*).
// ───────────────────────────────────────────────────────────────

import { getCollection, type CollectionEntry } from 'astro:content';
import { slugify } from '@utils/slugify';
import { getTaxonomia, type ProdutoTaxonomia } from '@data/produto-taxonomy';

export interface Produto {
  asin:        string;
  titulo:      string;
  imagem?:     string;
  preco?:      number | null;
  rating?:     number | null;
  ratingCount?: number | null;
  link:        string;
  vendedor?:   string;
  destaque:    boolean;
}

export interface ProdutoEntry {
  produto:    Produto;
  post:       CollectionEntry<'blog'>;
  slug:       string;
  taxonomia:  ProdutoTaxonomia | null;
}

export async function loadAllProdutos(): Promise<ProdutoEntry[]> {
  const posts = await getCollection('blog');
  const seenAsins = new Set<string>();
  const seenSlugs = new Set<string>();
  const out: ProdutoEntry[] = [];

  for (const post of posts) {
    if (!post.data.produtos?.length) continue;
    for (const produto of post.data.produtos as Produto[]) {
      if (seenAsins.has(produto.asin)) continue;
      seenAsins.add(produto.asin);

      let slug = slugify(produto.titulo);
      if (seenSlugs.has(slug)) slug = `${slug}-${produto.asin.slice(-6).toLowerCase()}`;
      seenSlugs.add(slug);

      out.push({
        produto,
        post,
        slug,
        taxonomia: getTaxonomia(produto.asin),
      });
    }
  }
  return out;
}

/** Score = rating * log10(ratingCount + 1) — produtos mais avaliados primeiro. */
export function sortProdutos(entries: ProdutoEntry[]): ProdutoEntry[] {
  return [...entries].sort((a, b) => {
    const rA = (a.produto.rating ?? 0) * Math.log10((a.produto.ratingCount ?? 1) + 1);
    const rB = (b.produto.rating ?? 0) * Math.log10((b.produto.ratingCount ?? 1) + 1);
    return rB - rA;
  });
}
