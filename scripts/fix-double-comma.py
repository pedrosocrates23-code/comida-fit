import re, glob, os

files = glob.glob('src/content/receitas/*.md')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    new = re.sub(r',\s*,', ',', content)
    if new != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new)
        print('Corrigido:', os.path.basename(f))
print('Pronto.')
