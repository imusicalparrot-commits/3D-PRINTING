import re, os

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
AD = "https://rzekl.com/g/1e8d11449451da3d44eb16525dc3e8/?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fw%2Fwholesale-3D-Printer.html"

def new_banner(img_src):
    return (
        f'<a class="banner-bleed" href="{AD}" target="_blank" rel="nofollow sponsored noopener noreferrer" aria-label="Shop 3D printers on AliExpress">\n'
        f'  <img src="{img_src}" alt="3D printers" loading="lazy">\n'
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
        f'</a>'
    )

count = 0
for root, dirs, files in os.walk(ROOT):
    for f in files:
        if not f.endswith(".html"):
            continue
        p = os.path.join(root, f)
        c = open(p, encoding="utf-8").read()
        # match existing banner: <a class="banner-bleed" ...><img src="PATH" ...></a>
        pat = re.compile(r'<a class="banner-bleed"[^>]*>\s*<img src="([^"]+)"[^>]*>\s*</a>', re.S)
        if not pat.search(c):
            continue
        def repl(m):
            global count
            count += 1
            return new_banner(m.group(1))
        c2 = pat.sub(repl, c)
        open(p, "w", encoding="utf-8").write(c2)

print("banners upgraded:", count)
