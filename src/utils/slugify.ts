/**
 * Converte um texto em slug SEO-friendly (long-tail).
 * Remove acentos, caracteres especiais e limita o comprimento.
 */
export function slugify(text: string, maxLen = 80): string {
  const slug = text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // remove acentos
    .replace(/[^a-z0-9]+/g, '-')     // não alfanumérico → hífen
    .replace(/^-+|-+$/g, '');        // trim hífens das pontas

  if (slug.length <= maxLen) return slug;

  // Trunca no limite respeitando palavra completa
  const truncated = slug.slice(0, maxLen);
  const lastDash  = truncated.lastIndexOf('-');
  return lastDash > maxLen * 0.6 ? truncated.slice(0, lastDash) : truncated;
}
