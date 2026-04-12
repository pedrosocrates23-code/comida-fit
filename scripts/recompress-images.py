"""
Recomprime todas as imagens WebP das receitas para quality=68
usando Pillow. Reduz tamanho sem perda visual perceptível.
"""
import os
import glob
import subprocess
import sys

# Verifica se Pillow está instalado
try:
    from PIL import Image
except ImportError:
    print("Instalando Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])
    from PIL import Image

RECEITAS_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'images', 'receitas')
files = sorted(glob.glob(os.path.join(RECEITAS_DIR, '*.webp')))

print(f"\n[compress]  Recomprimindo {len(files)} imagens para quality=68\n")

total_before = 0
total_after  = 0

for filepath in files:
    before = os.path.getsize(filepath)
    total_before += before

    try:
        img = Image.open(filepath).convert('RGB')
        img = img.resize((400, 300), Image.LANCZOS)

        # Salva com qualidade 68
        img.save(filepath, 'WEBP', quality=68, method=6)

        after = os.path.getsize(filepath)
        total_after += after

        economy = before - after
        name = os.path.basename(filepath)

        if economy > 0:
            print(f"OK {name}: {before//1024}KB → {after//1024}KB (-{economy//1024}KB)")
        else:
            print(f"--  {name}: {before//1024}KB (sem ganho)")

    except Exception as e:
        print(f"ERRO {os.path.basename(filepath)}: {e}")
        total_after += before

print(f"\nTotal Total: {total_before//1024}KB → {total_after//1024}KB (economizou {(total_before-total_after)//1024}KB)\n")
