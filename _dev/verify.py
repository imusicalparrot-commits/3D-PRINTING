import re, os, json

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
CAT = json.load(open(os.path.join(ROOT, "_dev", "data", "catalog.json"), encoding="utf-8"))
expected = {}
for s, c in CAT.items():
    for p in c["products"]:
        expected[p["slug"]] = "https://www.creativefabrica.com/product/%s/ref/16881082/" % p["link"].split("/product/")[1].split("/")[0]

problems = 0
total = 0
for s, c in CAT.items():
    html = open(os.path.join(ROOT, s, "index.html"), encoding="utf-8").read()
    arts = re.findall(r'<article class="prod"[^>]*>(.*?)</article>', html, re.S)
    for art in arts:
        img = re.search(r'assets/img/([^"]+?)\.webp', art)
        link = re.search(r'creativefabrica\.com/product/([^/]+)/', art)
        if not img or not link:
            continue
        total += 1
        slug = img.group(1)
        lslug = link.group(1)
        want = "https://www.creativefabrica.com/product/%s/ref/16881082/" % lslug
        if slug != lslug or expected.get(slug) != want:
            problems += 1
            print("PROBLEM", s, slug, lslug)

print("category cards checked:", total, "problems:", problems)

home = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
hp = re.findall(r'<article class="prod"[^>]*>(.*?)</article>', home, re.S)
print("homepage featured cards:", len(hp))
print("home links cf:", len(re.findall(r'creativefabrica', home)), "home imgs:", len(re.findall(r'assets/img/', home)))
print("kit theme cards (home):", len(re.findall(r'class="kit"', home)))
