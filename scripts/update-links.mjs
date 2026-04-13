/**
 * Substitui os links de afiliado nos arquivos de blog
 * conforme a planilha atualizada.
 */
import { readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const BLOG_DIR  = join(__dirname, '..', 'src', 'content', 'blog');

// Mapa ASIN → novo link (conforme planilha)
const LINKS = {
  B0CLTNBWFL: 'https://amzn.to/4eqsMqe',
  B07L5WJPXR: 'https://amzn.to/3Q9bd47',
  B07MFM36QT: 'https://amzn.to/4mpsHVU',
  B0DFQN5MT4: 'https://amzn.to/4tJESiW',
  B07MC12N2N: 'https://amzn.to/3OwWFe9',
  B08525PHGW: 'https://amzn.to/3Q9sdan',
  B0DFQM2GJZ: 'https://amzn.to/48uLFog',
  B081QQFXMK: 'https://amzn.to/4dLgQiS',
  B0CF71CJ2L: 'https://amzn.to/48uLHwo',
  B089PGDWG5: 'https://amzn.to/4vpDXpm',
  B0D9MPQ9CP: 'https://amzn.to/4mqeMPz',
  B00TF3XT4M: 'https://amzn.to/4mqeMPz',
  B0F2NBXXRS: 'https://amzn.to/3Ql9w3w',
  B0FJTCRZNK: 'https://amzn.to/4tLfcCy',
  B0DTV6JSNK: 'https://amzn.to/4mnEkMY',
  B0DV788XG4: 'https://amzn.to/4cM1J6H',
  B09SJT7751: 'https://amzn.to/4cn4f2G',
  B0FTGBXH71: 'https://amzn.to/4cM1J6H',
  B0GS7JG1P5: 'https://amzn.to/4cluA1d',
  B0FY3Z98MM: 'https://amzn.to/3QD0DT1',
  B0CLB2QLZ2: 'https://amzn.to/3OeB7mv',
  B07NF8X53B: 'https://amzn.to/42aPAD3',
  B082XF3PMP: 'https://amzn.to/4mM0JUJ',
  B0DLB9H9MD: 'https://amzn.to/47ZcXTG',
  B0FY8HCG1V: 'https://amzn.to/4tdi0se',
  B0DLLG9YQK: 'https://amzn.to/4clYNgN',
  B09XJMX44T: 'https://amzn.to/3ODcQXi',
  B0FGFQM6QM: 'https://amzn.to/4t9hhYS',
  B0D5FM7B2D: 'https://amzn.to/480WeiR',
  B0CZ2JQY3W: 'https://amzn.to/3OG0nlH',
  B0DHWFK43F: 'https://amzn.to/4tCcMWw',
  B0FQHLZZF3: 'https://amzn.to/4tMiYvj',
};

const FILES = [
  'melhores-proteinas-2026.md',
  'melhores-creatinas-2026.md',
  'melhores-pre-treino-2026.md',
  'melhores-aminoacidos-2026.md',
  'melhores-vitaminas-2026.md',
];

let totalSubst = 0;

for (const file of FILES) {
  const path = join(BLOG_DIR, file);
  let content = readFileSync(path, 'utf8');
  let changed = 0;

  for (const [asin, newLink] of Object.entries(LINKS)) {
    // Substitui qualquer link amazon antigo que contenha o ASIN
    // tanto no frontmatter (link: "...") quanto no body (href="...")
    const pattern = new RegExp(
      `https?://www\\.amazon\\.com\\.br/dp/${asin}[^"'\\s]*`,
      'g'
    );

    const before = content;
    content = content.replace(pattern, newLink);
    if (content !== before) {
      const count = (before.match(pattern) || []).length;
      changed += count;
      console.log(`  [${asin}] ${count}x substituído em ${file}`);
    }
  }

  if (changed > 0) {
    writeFileSync(path, content, 'utf8');
    totalSubst += changed;
    console.log(`✅  ${file} — ${changed} substituição(ões)\n`);
  } else {
    console.log(`—  ${file} sem alterações\n`);
  }
}

console.log(`\n📊  Total: ${totalSubst} links atualizados`);
