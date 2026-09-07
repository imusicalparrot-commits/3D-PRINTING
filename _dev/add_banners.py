import re, os

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
B1 = "3D Printer Banner _ Indigo (1)OOO.webp"
B2 = "3D Printer Banner _ Indigo (3)OOO.webp"
AD = "https://rzekl.com/g/1e8d11449451da3d44eb16525dc3e8/?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fw%2Fwholesale-3D-Printer.html"

def banner(depth, img):
    return (f'\n  <a class="banner-bleed" href="{AD}" target="_blank" rel="nofollow sponsored noopener noreferrer" aria-label="Shop 3D printers on AliExpress">'
            f'<img src="{depth}assets/{img}" alt="3D printers" loading="lazy"></a>\n')

# homepage: depth ""
pages = [("", os.path.join(ROOT, "index.html"))]
for slug in ["christmas","halloween","easter","valentine","dragons-fantasy","flexi-toys",
             "lamps-lights","organizers","keychains-accessories","decor-planters","gothic-dark","kawaii-cute"]:
    pages.append((f"{slug}/", os.path.join(ROOT, slug, "index.html")))

for depth, path in pages:
    h = open(path, encoding="utf-8").read()
    # idempotency: skip if already has a banner
    if "Banner _ Indigo" in h:
        print("skip (has banner):", path); continue
    # inject banner1 right after <body>
    h = re.sub(r'(<body>\s*)', lambda m: m.group(1) + banner(depth, B1), h, count=1)
    # inject banner2 right before </footer> (so it's full-width before footer) or before </main>
    if "</footer>" in h:
        h = h.replace("</footer>", banner(depth, B2) + "</footer>", 1)
    else:
        h = h.replace("</main>", banner(depth, B2) + "</main>", 1)
    open(path, "w", encoding="utf-8").write(h)
    print("banners added:", path)
print("DONE")
