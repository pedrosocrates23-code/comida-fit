# -*- coding: utf-8 -*-
"""
Varredura completa: remove travessoes (U+2014) de todos os arquivos do projeto.

Regras de substituicao:
  - Em titles (title=, <title>, title={): " - " (hifen com espacos)
  - Em description: (frontmatter YAML): ". " ou ", " dependendo do contexto
  - Em aria-label: ", "
  - Em texto visivel body (.astro): ", " ou ": " conforme contexto
  - Em comentarios de codigo (// , /* , <!-- ): " - "
  - Em strings de schema/utils: ": "
"""
import os, re, glob

BASE = os.path.join(os.path.dirname(__file__), '..')

def fix(text, filepath):
    ext = os.path.splitext(filepath)[1]
    lines = text.split('\n')
    out = []
    for line in lines:
        if '\u2014' not in line:
            out.append(line)
            continue

        s = line.strip()

        # Comentarios de codigo — substitui por " - "
        if s.startswith('//') or s.startswith('/*') or s.startswith('*') or s.startswith('<!--'):
            line = line.replace(' \u2014 ', ' - ')

        # Frontmatter YAML: description: "..." ou title: "..."
        elif re.match(r'\s*(description|title)\s*:', s):
            # Em descriptions: substitui por ". " capitalizado
            line = re.sub(r'\s*\u2014\s*', '. ', line)

        # aria-label com travessao
        elif 'aria-label' in line:
            line = line.replace(' \u2014 ', ', ')

        # title= prop em .astro (ex: title="Blog — Algo")
        elif re.search(r'title\s*=\s*[`"\']', line) or re.search(r'title\s*=\s*\{', line):
            line = line.replace(' \u2014 ', ': ')

        # Strings de schema/utils (name: `...—...`)
        elif 'schema' in filepath.lower() or 'utils' in filepath.lower():
            line = line.replace(' \u2014 ', ': ')

        # Texto visivel em .astro (nao e comentario, nao e atributo)
        elif ext == '.astro':
            # Se parece um titulo ou heading
            if re.search(r'<h[1-6]|\.title|siteName', line):
                line = line.replace(' \u2014 ', ': ')
            else:
                line = line.replace(' \u2014 ', ', ')

        # Fallback: substitui por ", "
        else:
            line = line.replace(' \u2014 ', ', ')

        out.append(line)
    return '\n'.join(out)


def process(pattern):
    files = glob.glob(pattern, recursive=True)
    changed = 0
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            original = fh.read()
        if '\u2014' not in original:
            continue
        fixed = fix(original, f)
        if fixed != original:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(fixed)
            rel = os.path.relpath(f, BASE)
            n = original.count('\u2014') - fixed.count('\u2014')
            print(f"  {rel}: {n} substituicoes")
            changed += 1
    return changed


print("\nVarrendo arquivos .astro, .ts, .md...\n")
total = 0
total += process(os.path.join(BASE, 'src', '**', '*.astro'))
total += process(os.path.join(BASE, 'src', '**', '*.ts'))
total += process(os.path.join(BASE, 'src', '**', '*.md'))

print(f"\n{total} arquivos alterados.")

# Verifica se sobrou algum
remaining = []
for pattern in ['src/**/*.astro', 'src/**/*.ts', 'src/**/*.md']:
    for f in glob.glob(os.path.join(BASE, pattern), recursive=True):
        with open(f, 'r', encoding='utf-8') as fh:
            if '\u2014' in fh.read():
                remaining.append(os.path.relpath(f, BASE))

if remaining:
    print("\nAinda com travessoes:")
    for r in remaining:
        print(f"  {r}")
else:
    print("\nNenhum travessao restante em src/.")
