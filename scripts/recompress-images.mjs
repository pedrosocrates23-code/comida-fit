import sharp from 'sharp';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const RECEITAS_DIR = path.join(__dirname, '..', 'public', 'images', 'receitas');

// Todas as imagens das receitas — recomprime para quality 68 (menor peso, visual OK)
const files = fs.readdirSync(RECEITAS_DIR).filter(f => f.endsWith('.webp'));

console.log(`\n🗜  Recomprimindo ${files.length} imagens para quality=68\n`);

let saved = 0;
for (const file of files) {
  const filepath = path.join(RECEITAS_DIR, file);
  const before = fs.statSync(filepath).size;

  const tmp = filepath + '.tmp';
  await sharp(filepath)
    .resize(400, 300, { fit: 'cover', position: 'attention' })
    .webp({ quality: 68 })
    .toFile(tmp);

  const buf = fs.readFileSync(tmp);
  fs.unlinkSync(tmp);
  if (buf.length < before) {
    fs.writeFileSync(filepath, buf);
    const economy = before - buf.length;
    saved += economy;
    console.log(`✅ ${file}: ${Math.round(before/1024)}KB → ${Math.round(buf.length/1024)}KB (-${Math.round(economy/1024)}KB)`);
  } else {
    console.log(`⏭  ${file}: já otimizado (${Math.round(before/1024)}KB)`);
  }
}

console.log(`\n💾 Total economizado: ${Math.round(saved/1024)}KB\n`);
