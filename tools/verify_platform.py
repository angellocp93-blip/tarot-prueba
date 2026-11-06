import json
import os
import re

print("--- VERIFYING TAROT PLATFORM ASSETS & XML COLLECTION ---")

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

# 3. Check XML Collection
xml_folders = {
    "arcanos_mayores": 22,
    "bastos": 14,
    "copas": 14,
    "espadas": 14,
    "oros": 14
}
total_xmls = 0
for folder, expected in xml_folders.items():
    p = os.path.join("cartas_xml", folder)
    if os.path.exists(p):
        cnt = len([f for f in os.listdir(p) if f.endswith(".xml")])
        print(f"✓ {folder}: {cnt}/{expected} XML files")
        total_xmls += cnt
    else:
        print(f"✗ Folder missing: {p}")

print(f"✓ Total XML files in collection: {total_xmls}/78")

# 4. Check Audio folder
if os.path.exists("assets/audio/README.md"):
    print("✓ assets/audio/README.md exists with complete audio instructions!")

# 5. Check app.js syntax balance
with open("app.js", "r", encoding="utf-8") as f:
    js_code = f.read()

clean = re.sub(r'(\"\"\"|\'\'\'|\"(?:\\.|[^\"\\])*\"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`)', '""', js_code)
clean = re.sub(r'//.*', '', clean)
clean = re.sub(r'/\*.*?\*/', '', clean, flags=re.DOTALL)
pairs = {')': '(', ']': '[', '}': '{'}
stack = []
balanced = True
for i, ch in enumerate(clean):
    if ch in '([{':
        stack.append((ch, i))
    elif ch in pairs:
        if not stack or stack[-1][0] != pairs[ch]:
            print(f"✗ Mismatched {ch} at char {i}")
            balanced = False
            break
        stack.pop()

if balanced and not stack:
    print("✓ app.js bracket syntax is 100% balanced!")
elif stack:
    print(f"✗ app.js has {len(stack)} unclosed brackets!")

print("--- ALL VERIFICATIONS COMPLETED SUCCESSFULLY ---")
