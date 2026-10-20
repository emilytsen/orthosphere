"""Gera o QR code do protótipo Orthosphere (PNG, fundo branco, módulos navy).

Uso:
    python gerar_qr.py https://SUA-URL-PUBLICADA

Requer:  pip install segno
Saída:   qr_orthosphere.png (ao lado deste script)
"""
import sys
from pathlib import Path

try:
    import segno
except ImportError:  # pragma: no cover
    sys.exit("Instale a dependência primeiro:  pip install segno")

if len(sys.argv) < 2:
    sys.exit("Informe a URL publicada:  python gerar_qr.py https://...")

url = sys.argv[1].strip()
out = Path(__file__).with_name("qr_orthosphere.png")

qr = segno.make(url, error="h")  # correção alta: lê bem mesmo projetado ou impresso pequeno
qr.save(str(out), scale=20, border=3, dark="#06102A", light="#FFFFFF")
print(f"QR gerado: {out}\nURL: {url}")
