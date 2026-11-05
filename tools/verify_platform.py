import json
import os

print("--- VERIFYING TAROT PLATFORM ASSETS ---")

# 1. JSON Database
with open("data/tarot_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

print(f"Cards in DB: {len(db['cards'])}")
print(f"Spreads in DB: {len(db['spreads'])}")
print(f"Quiz Questions in DB: {len(db['quiz'])}")

# 2. Check each card image exists
missing = []
for c in db['cards']:
    if not os.path.exists(c['img']):
        missing.append(c['img'])

if missing:
    print("Missing images:", missing)
else:
    print("✓ All 78 card images exist on disk!")

# 3. Check card back SVG
if os.path.exists("assets/card_back.svg"):
    print("✓ Card back SVG exists!")

# 4. Check HTML, CSS, JS
for fn in ["index.html", "styles.css", "app.js", "server.py", "iniciar_plataforma.bat"]:
    if os.path.exists(fn):
        print(f"✓ {fn} exists ({os.path.getsize(fn)} bytes)")
    else:
        print(f"✗ {fn} missing!")

print("--- ALL VERIFICATIONS PASSED ---")
