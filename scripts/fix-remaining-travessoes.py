"""
Limpa os travessões restantes após o remove-travessoes.py:
- Linhas com **Negrito:** (começam com **) → divide no primeiro " — " em 2 parágrafos
- Células de tabela (começam com |) → substitui " — " por ", "
- Itens do frontmatter instrucoes (  - "...") → substitui " — " por ", "
- Cabeçalhos (começam com #) → substitui " — " por ": "
- description: no frontmatter → deixa como está (SEO)
"""

import re
import glob
import os

RECIPES_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'receitas')

def capitalize_first(text):
    text = text.strip()
    if not text:
        return text
    return text[0].upper() + text[1:]

def process_bold_line(line):
    """Linhas como '**Algo:** texto — mais texto'. Divide no primeiro —."""
    if '—' not in line:
        return line
    parts = re.split(r'\s*—\s*', line, maxsplit=1)
    para1 = parts[0].rstrip(' ,;')
    para2 = parts[1].strip() if len(parts) > 1 else ''

    if para1 and para1[-1] not in '.!?:':
        para1 += '.'

    para2 = capitalize_first(para2)
    # Remove travessões restantes no segundo parágrafo
    para2 = re.sub(r'\s*—\s*,?\s*', ', ', para2)

    if para2:
        return para1 + '\n\n' + para2
    return para1

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm_match = re.match(r'^(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if not fm_match:
        return 0

    frontmatter_raw = fm_match.group(1)
    body = fm_match.group(2)
    changes = 0

    # ── Frontmatter: instrucoes items ─────────────────────────
    # Substitui " — " por ", " dentro de strings YAML (  - "...")
    def fix_fm_item(m):
        nonlocal changes
        if '—' in m.group(0):
            changes += 1
            return re.sub(r'\s*—\s*', ', ', m.group(0))
        return m.group(0)

    new_frontmatter = re.sub(r'  - ".*?—.*?"', fix_fm_item, frontmatter_raw)

    # ── Body ───────────────────────────────────────────────────
    lines = body.split('\n')
    new_lines = []

    for line in lines:
        if '—' not in line:
            new_lines.append(line)
            continue

        stripped = line.strip()

        # Cabeçalhos: substitui " — " por ": "
        if stripped.startswith('#'):
            new_line = re.sub(r'\s*—\s*', ': ', line)
            changes += 1

        # Células de tabela: substitui " — " por ", "
        # MAS preserva "|  — |" (travessão sozinho = célula vazia)
        elif stripped.startswith('|'):
            if re.match(r'^\|\s*—\s*\|', stripped):
                new_line = line  # célula vazia de tabela — preserva
            else:
                new_line = re.sub(r'\s*—\s*', ', ', line)
                changes += 1

        # Linhas com **negrito** (começam com **): divide em dois parágrafos
        elif stripped.startswith('**'):
            new_line = process_bold_line(line)
            if new_line != line:
                changes += 1

        else:
            new_line = line

        new_lines.append(new_line)

    new_body = '\n'.join(new_lines)
    new_content = new_frontmatter + new_body

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changes

def main():
    pattern = os.path.join(RECIPES_DIR, '*.md')
    files = sorted(glob.glob(pattern))

    total = 0
    for filepath in files:
        name = os.path.basename(filepath)
        n = process_file(filepath)
        total += n
        if n:
            print(f'{name}: {n} substituições')

    print(f'\nTotal: {total} substituições feitas.')

if __name__ == '__main__':
    main()
