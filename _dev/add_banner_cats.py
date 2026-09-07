import os

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
AD = "https://rzekl.com/g/1e8d11449451da3d44eb16525dc3e8/?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fw%2Fwholesale-3D-Printer.html"
IMG = "../assets/3DPrinterBanner_Indigo1OOO.webp"

def banner():
    return (
        f'<a class="banner-bleed" href="{AD}" target="_blank" rel="nofollow sponsored noopener noreferrer" aria-label="Shop 3D printers on AliExpress">\n'
        f'  <img src="{IMG}" alt="3D printers" loading="lazy">\n'
        f'  <span class="banner-overlay"></span>\n'
        f'  <div class="banner-content">\n'
        f'    <div class="banner-top">\n'
        f'      <div>\n'
        f'        <div class="banner-title">3D &#1055;&#1088;&#1080;&#1085;&#1090;&#1077;&#1088;&#1099;</div>\n'
        f'        <div class="banner-sub">Filaments &amp; accessories too</div>\n'
        f'      </div>\n'
        f'      <span class="banner-tag">AD</span>\n'
        f'    </div>\n'
        f'    <div class="banner-bottom">\n'
        f'      <span class="banner-pill">&#1050;&#1091;&#1087;&#1080; &#1087;&#1088;&#1080;&#1085;&#1090;&#1077;&#1088; &#1079;&#1076;&#1077;&#1089;&#1100; &#8594;</span>\n'
        f'      <div class="banner-dots"><i class="on"></i><i></i><i></i><i></i></div>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</a>\n'
    )

cats = ["christmas","halloween","easter","valentine","dragons-fantasy","flexi-toys",
        "lamps-lights","organizers","keychains-accessories","decor-planters","gothic-dark","kawaii-cute"]

MARK = '<div class="search-inline"'
for slug in cats:
    p = os.path.join(ROOT, slug, "index.html")
    c = open(p, encoding="utf-8").read()
    if "banner-bleed" in c:
        print("skip, already has:", slug); continue
    idx = c.find(MARK)
    if idx == -1:
        print("NO FILTER MARK:", slug); continue
    c2 = c[:idx] + banner() + "      " + c[idx:]
    open(p, "w", encoding="utf-8").write(c2)
    print("banner added above filter:", slug)
print("DONE")
