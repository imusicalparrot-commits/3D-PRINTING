import re, os, json

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
CAT = json.load(open(os.path.join(ROOT, "_dev", "data", "catalog.json"), encoding="utf-8"))

# For each category, the source HTML pairs image + link in one <article>.
# The generator copied both from the same article, so pairing is preserved by construction.
# Verify: total links == total images == total titles across all pages (one each per product).

total_links = 0
total_imgs = 0
total_titles = 0
per_cat = {}
for s, c in CAT.items():
    html = open(os.path.join(ROOT, s, "index.html"), encoding="utf-8").read()
    arts = re.findall(r'<article class="prod"[^>]*>(.*?)</article>', html, re.S)
    links = sum(len(re.findall(r'creativefabrica\.com/product/', a)) for a in arts)
    imgs = sum(len(re.findall(r'assets/img/[^"]+?\.webp', a)) for a in arts)
    titles = sum(len(re.findall(r'data-title=', a)) for a in arts)
    per_cat[s] = (len(arts), links, imgs, titles)
    total_links += links; total_imgs += imgs; total_titles += titles

print("Category pages — articles / links / images / titles:")
for s, v in per_cat.items():
    art, l, im, t = v
    ok = (art == l == im == t == len(CAT[s]["products"]))
    print(f"  {s:22} art={art} link={l} img={im} title={t}  {'OK' if ok else 'MISMATCH'}")

print()
print("TOTALS  links=%d imgs=%d titles=%d expected=%d" % (total_links, total_imgs, total_titles, 198))

# homepage featured (12) + theme kit cards (12) sanity
home = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
print("Home featured product cards:", len(re.findall(r'<article class="prod"', home)))
print("Home kit theme cards:", len(re.findall(r'class="kit"', home)))
print("Home images:", len(re.findall(r'assets/img/', home)), "Home cf links:", home.count("creativefabrica"))
# verify homepage featured cards each have 1 img + 1 link
arts = re.findall(r'<article class="prod"[^>]*>(.*?)</article>', home, re.S)
for i, a in enumerate(arts):
    im = re.search(r'assets/img/([^"]+?)\.webp', a)
    lk = re.search(r'creativefabrica\.com/product/([^/]+)/', a)
    print(f"  featured[{i}] img={bool(im)} link={bool(lk)}")
