import re, os

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"

# pages to STRIP banners from: homepage + 12 categories (NOT blog)
strip_dirs = [
    ROOT,  # index.html
    "christmas","halloween","easter","valentine","dragons-fantasy","flexi-toys",
    "lamps-lights","organizers","keychains-accessories","decor-planters","gothic-dark","kawaii-cute",
]
pat = re.compile(r'<a class="banner-bleed"[\s\S]*?</a>')

removed = 0
for d in strip_dirs:
    p = os.path.join(ROOT, d, "index.html") if d != ROOT else os.path.join(ROOT, "index.html")
    if not os.path.isfile(p):
        continue
    c = open(p, encoding="utf-8").read()
    c2 = pat.sub("", c)
    n = c.count('<a class="banner-bleed"')
    if n:
        # also strip the surrounding blank line
        c2 = re.sub(r'\n\s*\n\s*\n', '\n\n', c2)
        open(p, "w", encoding="utf-8").write(c2)
        removed += n
        print(f"removed {n} from {d}/index.html")

print("total removed:", removed)
