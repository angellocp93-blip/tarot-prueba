import requests
import os
import re
import time

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

card_names = sorted(list(set(re.findall(r'img/cartas/([a-z0-9_-]+\.webp)', html))))
print(f"Total cards to download: {len(card_names)}")

os.makedirs("assets/cards", exist_ok=True)
os.makedirs("assets/bonus", exist_ok=True)
os.makedirs("assets/maps", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://mapasmentales.onnexusbr.com/"
}

# Download cards
downloaded = 0
for name in card_names:
    path = os.path.join("assets/cards", name)
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        url = f"https://mapasmentales.onnexusbr.com/img/cartas/{name}"
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
                downloaded += 1
            else:
                print(f"Failed {name}: {r.status_code}")
        except Exception as e:
            print(f"Error {name}: {e}")
        time.sleep(0.05)
    else:
        downloaded += 1

print(f"Cards ready: {downloaded}/{len(card_names)}")

# Download bonus images
bonus_imgs = [
    "regalo-tiradas.webp",
    "regalo-combinaciones.webp",
    "regalo-baraja.webp",
    "regalo-invertidas.webp"
]
for b in bonus_imgs:
    path = os.path.join("assets/bonus", b)
    if not os.path.exists(path):
        url = f"https://mapasmentales.onnexusbr.com/img/{b}"
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
                print(f"Bonus downloaded: {b}")
        except Exception as e:
            print(f"Error bonus {b}: {e}")

# Download sample hq maps
maps = ["loco", "luna", "rcopas", "rueda", "mago", "rbastos", "muerte", "respadas", "sol", "enam", "roros", "diablo"]
for m in maps:
    path = os.path.join("assets/maps", f"hq-{m}-1200.webp")
    if not os.path.exists(path):
        url = f"https://mapasmentales.onnexusbr.com/img/hq-{m}-1200.webp"
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
                print(f"Sample map downloaded: {m}")
        except Exception as e:
            print(f"Error map {m}: {e}")

print("Download complete.")
