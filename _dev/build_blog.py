import re, os, json

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
BLOG = os.path.join(ROOT, "blog")
GO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>'

BRAND = "3D PRINTING"
BANNER1 = "3DPrinterBanner_Indigo1OOO.webp"
BANNER2 = "3DPrinterBanner_Indigo3OOO.webp"

def nav(depth):
    # reuse homepage-style genesis nav
    cats = [
        ("christmas","Christmas & Winter","XMAS"),("halloween","Halloween & Spooky","HWEN"),
        ("easter","Easter & Spring","EAST"),("valentine","Valentine's & Wedding","VAL"),
        ("dragons-fantasy","Dragons & Fantasy","DRGN"),("flexi-toys","Flexi Toys & Learning","FLXI"),
        ("lamps-lights","Lamps & Night Lights","LAMP"),("organizers","Desk & Home Organizers","ORG"),
        ("keychains-accessories","Keychains & Craft Tools","KEY"),("decor-planters","Decor, Planters & Figurines","DECO"),
        ("gothic-dark","Gothic & Dark Aesthetic","GOTH"),("kawaii-cute","Kawaii & Cute","KAWA"),
    ]
    mega = "".join(
        f'<a class="mega-item" href="{depth}{s}/"><span class="mega-ico">{ab}</span><b>{n}</b><span>{cnt} models</span></a>'
        for s,n,ab in cats for cnt in [0]
    )
    # simpler mega build
    counts = {
        "christmas":17,"halloween":22,"easter":15,"valentine":9,"dragons-fantasy":18,"flexi-toys":17,
        "lamps-lights":10,"organizers":23,"keychains-accessories":28,"decor-planters":22,"gothic-dark":8,"kawaii-cute":9,
    }
    mega = "".join(
        f'<a class="mega-item" href="{depth}{s}/"><span class="mega-ico">{ab}</span><b>{n}</b><span>{counts[s]} models</span></a>'
        for s,n,ab in cats
    )
    drawer = "".join(
        f'<li><a href="{depth}{s}/">{n} <span class="cnt">{counts[s]}</span></a></li>'
        for s,n,ab in cats
    )
    return f"""
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="{depth}"><span class="brand-mark">3D&nbsp;</span><span class="brand-accent">PRINTING</span></a>
      <nav class="nav" aria-label="Main">
        <div class="mega">
          <button class="nav-link" type="button" aria-expanded="false">Themes <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
          <div class="mega-panel">{mega}</div>
        </div>
        <a class="nav-link" href="{depth}blog/">Blog</a>
        <div class="nav-actions"><a class="btn btn--secondary btn--sm" href="{depth}#themes">Browse</a></div>
        <button class="burger" id="burgerBtn" aria-expanded="false" aria-controls="mobileNav" aria-label="Menu">
          <span>Menu</span>
          <svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M7.33 16V0h1.34v16H7.33z"/><path d="M0 7.33V8.67h16V7.33H0z"/></svg>
        </button>
      </nav>
    </div>
  </header>
  <div class="drawer" id="mobileNav" aria-hidden="true">
    <div class="drawer-overlay" data-mnav-close></div>
    <div class="drawer-panel">
      <div style="display:flex;align-items:center;justify-content:space-between">
        <a class="brand" href="{depth}"><span class="brand-mark">3D&nbsp;</span><span class="brand-accent">PRINTING</span></a>
        <button class="drawer-close" data-mnav-close aria-label="Close"><svg viewBox="0 0 16 16" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M2 2l12 12M14 2L2 14"/></svg></button>
      </div>
      <ul class="drawer-list">
        <li><a href="{depth}">Home <span class="cnt">START</span></a></li>
        <li><a href="{depth}blog/">Blog <span class="cnt">GUIDES</span></a></li>
        <li class="drawer-sep" aria-hidden="true"></li>
        {drawer}
      </ul>
    </div>
  </div>"""

def footer(depth):
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">3D<span>PRINTING</span></div>
          <p>A curated index of 198 printable 3D models across the seasons and the home. Pick a theme, find a model, and start printing.</p>
        </div>
        <div class="footer-col"><h4>Seasons</h4><a href="{depth}christmas/">Christmas & Winter</a><a href="{depth}halloween/">Halloween & Spooky</a><a href="{depth}easter/">Easter & Spring</a><a href="{depth}valentine/">Valentine's & Wedding</a></div>
        <div class="footer-col"><h4>Collections</h4><a href="{depth}dragons-fantasy/">Dragons & Fantasy</a><a href="{depth}flexi-toys/">Flexi Toys</a><a href="{depth}lamps-lights/">Lamps & Lights</a><a href="{depth}decor-planters/">Decor & Planters</a></div>
        <div class="footer-col"><h4>For the desk</h4><a href="{depth}organizers/">Organizers</a><a href="{depth}keychains-accessories/">Keychains</a><a href="{depth}gothic-dark/">Gothic & Dark</a><a href="{depth}kawaii-cute/">Kawaii & Cute</a></div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 3D PRINTING — an index, not a store. Every link goes to the model's own page.</span>
        <span><a href="{depth}privacy/">Privacy</a> &middot; <a href="{depth}terms/">Terms</a> &middot; <a href="{depth}blog/">Blog</a></span>
      </div>
    </div>
  </footer>"""

def banner_full(depth, img):
    return f'<a class="banner-bleed" href="https://rzekl.com/g/1e8d11449451da3d44eb16525dc3e8/?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fw%2Fwholesale-3D-Printer.html" target="_blank" rel="nofollow sponsored noopener noreferrer" aria-label="Shop 3D printers on AliExpress">\n  <img src="{depth}assets/{img}" alt="3D printers" loading="lazy">\n  <span class="banner-overlay"></span>\n  <div class="banner-content">\n    <div class="banner-top">\n      <div>\n        <div class="banner-title">3D &#1055;&#1088;&#1080;&#1085;&#1090;&#1077;&#1088;&#1099;</div>\n        <div class="banner-sub">Filaments &amp; accessories too</div>\n      </div>\n      <span class="banner-tag">AD</span>\n    </div>\n    <div class="banner-bottom">\n      <span class="banner-pill">&#1050;&#1091;&#1087;&#1080; &#1087;&#1088;&#1080;&#1085;&#1090;&#1077;&#1088; &#1079;&#1076;&#1077;&#1089;&#1100; &#8594;</span>\n      <div class="banner-dots"><i class="on"></i><i></i><i></i><i></i></div>\n    </div>\n  </div>\n</a>'

HEAD = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{{TITLE}}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{CSS}}assets/genesis.css">
<script src="{{CSS}}assets/genesis.js" defer></script>
</head>
<body>
{{NAV}}
<main>'''

TAIL = '''</main>
{{FOOTER}}
</body>
</html>'''

def post_files():
    out = []
    for d in sorted(os.listdir(BLOG)):
        p = os.path.join(BLOG, d, "index.html")
        if os.path.isfile(p) and d != "index.html":
            out.append(d)
    return out

def parse_post(d):
    html = open(os.path.join(BLOG, d, "index.html"), encoding="utf-8").read()
    tm = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
    title = tm.group(1) if tm else d.replace("-", " ").title()
    m = re.search(r'<span>(\d{4}-\d{2}-\d{2})</span><span>([^<]+)</span>', html)
    date, read = (m.group(1), m.group(2)) if m else ("2026-09-04", "5 min read")
    m = re.search(r'<div class="a-body">(.*?)</div>\s*<div class="a-nav">', html, re.S)
    if not m:
        m = re.search(r'<div class="a-body">(.*?)</div>\s*</div>', html, re.S)
    body = m.group(1) if m else "<p>Guide content unavailable.</p>"
    nav_prev = re.search(r'<a href="\.\./([^"]+)">←', html)
    nav_next = re.search(r'<a href="\.\./([^"]+)">([^<]+) →', html)
    prev = (nav_prev.group(1), nav_prev.group(0).split(">")[1].strip()) if nav_prev else None
    # related themes
    rel = re.findall(r'<a class="rt-card" href="\.\./([^"]+)"><b>([^<]+)</b><span>([^<]+)</span></a>', html)
    return title, date, read, body, prev, rel

posts = post_files()
meta = {d: parse_post(d) for d in posts}

# ---- BLOG INDEX ----
lead = posts[0]
lead_title, lead_date, lead_read, lead_body, _, _ = meta[lead]
lead_desc = re.search(r'<p>([^<]{20,})</p>', lead_body)
lead_desc = lead_desc.group(1) if lead_desc else ""
# first paragraph stripped of tags for lead
lead_first = re.sub(r'<[^>]+>', '', lead_body.split('</p>')[0])[:160]

cards = []
for d in posts[1:]:
    title, date, read, body, _, _ = meta[d]
    desc = re.sub(r'<[^>]+>', '', body.split('</p>')[0])
    if len(desc) > 150: desc = desc[:150].rstrip() + "…"
    cards.append(f'''
        <a class="pcard" href="{d}/">
          <div class="pcard-body">
            <span class="pcard-kicker">Guide</span>
            <h3>{title}</h3>
            <p>{desc}</p>
            <div class="pcard-foot"><span class="pmeta">{read}</span><span class="pgo">Read {GO}</span></div>
          </div>
        </a>''')

# related themes strip on index
rel_cards = """
  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head"><span class="overline">Practice</span><h2>Put it into practice</h2><p>Each collection pairs naturally with the guides above.</p></div>
      <div class="rt-grid">
        <a class="rt-card" href="../keychains-accessories/"><b>Keychains & Craft Tools</b><span>28 models</span></a>
        <a class="rt-card" href="../flexi-toys/"><b>Flexi Toys & Learning</b><span>17 models</span></a>
        <a class="rt-card" href="../organizers/"><b>Desk & Home Organizers</b><span>23 models</span></a>
        <a class="rt-card" href="../lamps-lights/"><b>Lamps & Night Lights</b><span>10 models</span></a>
      </div>
    </div>
  </section>"""

index_html = (HEAD
  .replace("{TITLE}", '<title>Blog &amp; Guides — 3D Printing Tips | 3D PRINTING</title>\n<meta name="description" content="Practical 3D printing guides: model preparation, software, first-week plans and finishing tips.">')
  .replace("{CSS}", "../")
  .replace("{NAV}", nav("../"))
  + f'''
  <section class="blog-hero">
    <div class="wrap">
      <span class="overline">Blog &amp; guides</span>
      <h1>Guides for better 3D prints</h1>
      <p class="lede">Short, practical reads — no fluff, no filler. Model preparation, the software stack explained, and a first-week plan that ends with objects you actually keep. Every guide links straight back to the model collections you can practice on.</p>
      <span class="hero-count"><span class="chip chip--indigo">{len(posts)} guides</span><span class="chip">updated 2026-09-04</span></span>
    </div>
  </section>
  <div class="wrap">{banner_full("../", BANNER1)}</div>
  <section class="section">
    <div class="wrap">
      <a class="lead-post" href="{lead}/">
        <div class="lead-body">
          <span class="overline">Featured</span>
          <h2>{lead_title}</h2>
          <p>{lead_first}…</p>
          <span class="btn">Read the guide {GO}</span>
        </div>
      </a>
      <div class="postlist-grid">
        {''.join(cards)}
      </div>
    </div>
  </section>
  {rel_cards}
'''
  + banner_full("../", BANNER2)
  + TAIL.replace("{{FOOTER}}", footer("../")))

open(os.path.join(BLOG, "index.html"), "w", encoding="utf-8").write(index_html)
print("blog/index.html ->", len(posts), "posts")

# ---- POSTS ----
for d in posts:
    title, date, read, body, prev, rel = meta[d]
    prev_html = ""
    if prev:
        prev_html = f'<a href="../{prev[0]}">← {prev[1]}</a>'
    rel_html = ""
    if rel:
        items = "".join(f'<a class="rt-card" href="../{s}"><b>{b}</b><span>{s2}</span></a>' for s,b,s2 in rel)
        rel_html = f'''
      <section class="related-themes">
        <h2>Put it into practice</h2>
        <div class="rt-grid">{items}</div>
      </section>'''
    desc = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', body.split('</p>')[0])).strip()[:150]
    post_html = (HEAD
      .replace("{TITLE}", f'<title>{title} | 3D PRINTING</title>\n<meta name="description" content="{desc}">')
      .replace("{CSS}", "../../")
      .replace("{NAV}", nav("../../"))
      + f'''
  <section class="section">
    <div class="wrap">
      <article class="article">
        <a class="a-back" href="../">← All guides</a>
        <span class="overline">Guide</span>
        <h1>{title}</h1>
        <div class="a-meta"><span>{date}</span><span>{read}</span></div>
        {banner_full("../../", BANNER1)}
        <div class="a-body">
          {body}
          <div class="a-callout"><b>The one rule:</b> print something you will actually keep every single day. Motivation does not come from calibration cubes.</div>
        </div>
        <div class="a-nav">
          {prev_html or '<span></span>'}
          <a href="../3d-printing-software-explained/">3D Printing Software, Explained →</a>
        </div>
        {rel_html}
      </article>
    </div>
  </section>
'''
      + banner_full("../../", BANNER2)
      + TAIL.replace("{{FOOTER}}", footer("../../")))
    open(os.path.join(BLOG, d, "index.html"), "w", encoding="utf-8").write(post_html)
    print("post", d)
print("DONE")
