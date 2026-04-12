"""
Remove travessões (—) dos arquivos de receitas:
- Parágrafos normais: divide no PRIMEIRO " — ", criando dois parágrafos.
  Os travessões restantes (parentéticos) são substituídos por ", ".
- Blockquotes (> ...): substitui " — " por ", " sem dividir.
- Cabeçalhos, listas, tabelas, HR: intocados.
"""

import os
import re
import glob

RECIPES_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'receitas')

def capitalize_first(text: str) -> str:
    """Capitaliza a primeira letra de uma string."""
    text = text.strip()
    if not text:
        return text
    return text[0].upper() + text[1:]

def clean_junction(text: str) -> str:
    """Remove vírgula/ponto-e-vírgula soltos no início de um segmento."""
    return re.sub(r'^[,;]\s*', '', text.strip())

def process_paragraph(line: str) -> str:
    """
    Divide um parágrafo no PRIMEIRO travessão, formando dois parágrafos.
    Travessões restantes são substituídos por ', '.
    """
    if '—' not in line:
        return line

    # Divide no PRIMEIRO travessão
    first_cut = re.split(r'\s*—\s*', line, maxsplit=1)

    para1 = first_cut[0].rstrip(' ,;')
    para2 = clean_junction(first_cut[1]) if len(first_cut) > 1 else ''

    # Garante que para1 termina com ponto
    if para1 and para1[-1] not in '.!?:':
        para1 += '.'

    # Capitaliza início do segundo parágrafo
    para2 = capitalize_first(para2)

    # Substitui travessões restantes no segundo parágrafo por ', '
    # Consome também vírgula opcional logo após o travessão (evita ", ,")
    para2 = re.sub(r'\s*—\s*,?\s*', ', ', para2)

    if para2:
        return para1 + '\n\n' + para2
    return para1

def process_blockquote(line: str) -> str:
    """Substitui ' — ' por ', ' dentro de blockquotes."""
    return re.sub(r'\s*—\s*', ', ', line)

def is_plain_paragraph(line: str) -> bool:
    """Retorna True se a linha é um parágrafo de texto comum."""
    stripped = line.strip()
    if not stripped:
        return False
    # Não é cabeçalho, blockquote, lista, tabela, HR, ou código
    if stripped.startswith(('#', '>', '-', '*', '+', '|', '`', '~')):
        return False
    # Não é HR (---, ___, ***)
    if re.match(r'^[-_*]{3,}$', stripped):
        return False
    return True

def process_file(filepath: str) -> int:
    """Processa um arquivo .md. Retorna o número de substituições feitas."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Separa frontmatter do corpo
    # O conteúdo começa com "---\n...frontmatter...\n---\n"
    fm_match = re.match(r'^(---\n.*?\n---\n)(.*)', content, re.DOTALL)
    if not fm_match:
        return 0

    frontmatter = fm_match.group(1)
    body = fm_match.group(2)

    lines = body.split('\n')
    new_lines = []
    changes = 0

    for line in lines:
        stripped = line.strip()
        if '—' in line:
            if stripped.startswith('>'):
                new_line = process_blockquote(line)
                changes += 1
            elif is_plain_paragraph(line):
                new_line = process_paragraph(line)
                changes += 1
            else:
                new_line = line
        else:
            new_line = line
        new_lines.append(new_line)

    new_body = '\n'.join(new_lines)
    new_content = frontmatter + new_body

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changes

def main():
    pattern = os.path.join(RECIPES_DIR, '*.md')
    files = sorted(glob.glob(pattern))

    if not files:
        print(f'Nenhum arquivo encontrado em: {RECIPES_DIR}')
        return

    total_changes = 0
    for filepath in files:
        name = os.path.basename(filepath)
        n = process_file(filepath)
        total_changes += n
        status = f'{n:3d} substituições' if n else '  — sem travessões'
        print(f'{name}: {status}')

    print(f'\nTotal: {len(files)} arquivos processados, {total_changes} substituições feitas.')

if __name__ == '__main__':
    main()
