import re, json, os

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
OUT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site\_dev\data\catalog.json"

cats = [
    ("christmas", "Christmas & Winter", "XMAS"),
    ("halloween", "Halloween & Spooky", "HWEN"),
    ("easter", "Easter & Spring", "EAST"),
    ("valentine", "Valentine's & Wedding", "VAL"),
    ("dragons-fantasy", "Dragons & Fantasy", "DRGN"),
    ("flexi-toys", "Flexi Toys & Learning", "FLXI"),
    ("lamps-lights", "Lamps & Night Lights", "LAMP"),
    ("organizers", "Desk & Home Organizers", "ORG"),
    ("keychains-accessories", "Keychains & Craft Tools", "KEY"),
    ("decor-planters", "Decor, Planters & Figurines", "DECO"),
    ("gothic-dark", "Gothic & Dark Aesthetic", "GOTH"),
    ("kawaii-cute", "Kawaii & Cute", "KAWA"),
]

intros = json.load(open(os.path.join(ROOT, "_dev", "data", "intros.json"), encoding="utf-8"))
flexi = json.load(open(os.path.join(ROOT, "_dev", "data", "flexi-toys.json"), encoding="utf-8"))

art_re = re.compile(r'<article class="product">(.*?)</article>', re.S)
img_re = re.compile(r'assets/img/([^"\\]+?)\.webp')
link_re = re.compile(r'https://www\.creativefabrica\.com/product/([^/]+)/ref/16881082/')
title_re = re.compile(r'<h2 class="p-title"><a[^>]*>([^<]+)</a></h2>')
desc_re = re.compile(r'<p class="p-desc">([^<]+)</p>')

catalog = {}
for slug, name, abbr in cats:
    html = open(os.path.join(ROOT, slug, "index.html"), encoding="utf-8").read()
    products = []
    for block in art_re.findall(html):
        imgs = img_re.findall(block)
        links = link_re.findall(block)
        titles = title_re.findall(block)
        descs = desc_re.findall(block)
        if not imgs or not links:
            continue
        pimg = imgs[0]
        lslug = links[0]
        p = {
            "slug": pimg,
            "img": pimg + ".webp",
            "link": "https://www.creativefabrica.com/product/%s/ref/16881082/" % lslug,
            "title": titles[0] if titles else "",
            "desc": descs[0] if descs else "",
            "note": intros.get(pimg, ""),
        }
        if pimg in flexi:
            p["title"] = flexi[pimg]["t"]
            p["desc"] = flexi[pimg]["d"]
        products.append(p)
    catalog[slug] = {"name": name, "abbr": abbr, "products": products}

total = sum(len(c["products"]) for c in catalog.values())
print("Total products:", total)
miss = 0
for slug, c in catalog.items():
    for p in c["products"]:
        if p["slug"] != p["link"].split("/product/")[1].split("/")[0]:
            miss += 1
            print("MISMATCH", slug, p["slug"], "vs", p["link"])
print("mismatches:", miss)
json.dump(catalog, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT)
