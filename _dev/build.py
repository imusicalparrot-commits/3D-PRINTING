import json, os, datetime

ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
CAT = json.load(open(os.path.join(ROOT, "_dev", "data", "catalog.json"), encoding="utf-8"))

ASSET = "../assets/"   # from subpages
HOME = ""              # from homepage

SVG_GO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>'

def nav(active=None, depth=""):
    items = "".join(
        f'<a class="nav-link" href="{depth}{slug}/">{c["name"]}</a>'
        for slug, c in CAT.items()
    )
    mega_items = "".join(
        f'<a class="mega-item" href="{depth}{slug}/">'
        f'<span class="mega-ico">{c["abbr"]}</span><b>{c["name"]}</b>'
        f'<span>{len(c["products"])} models</span></a>'
        for slug, c in CAT.items()
    )
    drawer_items = "".join(
        f'<li><a href="{depth}{slug}/">{c["name"]} <span class="cnt">{len(c["products"])}</span></a></li>'
        for slug, c in CAT.items()
    )
    return f"""
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="{depth}"><span class="brand-mark">3D&nbsp;</span><span class="brand-accent">PRINT</span></a>
      <nav class="nav" aria-label="Main">
        <div class="mega">
          <button class="nav-link" type="button" aria-expanded="false">Themes <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
          <div class="mega-panel">{mega_items}</div>
        </div>
        <a class="nav-link" href="{depth}blog/">Blog</a>
        <div class="nav-actions">
          <a class="btn btn--secondary btn--sm" href="{depth}#themes">Browse</a>
        </div>
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
        <a class="brand" href="{depth}"><span class="brand-mark">3D&nbsp;</span><span class="brand-accent">PRINT</span></a>
        <button class="drawer-close" data-mnav-close aria-label="Close"><svg viewBox="0 0 16 16" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M2 2l12 12M14 2L2 14"/></svg></button>
      </div>
      <ul class="drawer-list">
        <li><a href="{depth}">Home <span class="cnt">START</span></a></li>
        <li><a href="{depth}blog/">Blog <span class="cnt">GUIDES</span></a></li>
        <li class="drawer-sep" aria-hidden="true"></li>
        {drawer_items}
      </ul>
    </div>
  </div>"""

def footer(depth=""):
    groups = [
        ("Seasons", ["christmas", "halloween", "easter", "valentine"]),
        ("Collections", ["dragons-fantasy", "flexi-toys", "lamps-lights", "decor-planters"]),
        ("For the desk", ["organizers", "keychains-accessories", "gothic-dark", "kawaii-cute"]),
    ]
    cols = ""
    for title, slugs in groups:
        links = "".join(f'<a href="{depth}{s}/">{CAT[s]["name"]}</a>' for s in slugs)
        cols += f'<div class="footer-col"><h4>{title}</h4>{links}</div>'
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">3D<span>PRINT</span></div>
          <p>A curated index of {sum(len(c['products']) for c in CAT.values())} printable 3D models across the seasons and the home. Pick a theme, find a model, and start printing.</p>
        </div>
        {cols}
      </div>
      <div class="footer-bottom">
        <span>&copy; {datetime.date.today().year} 3D PRINT — an index, not a store. Every link goes to the model's own page.</span>
        <span><a href="{depth}privacy/">Privacy</a> &middot; <a href="{depth}terms/">Terms</a> &middot; <a href="{depth}blog/">Blog</a></span>
      </div>
    </div>
  </footer>"""

def product_card(p, depth="", num=""):
    chip = f'<span class="prod-chip">{num or "3D"}</span>'
    a = f'{depth}assets/img/{p["img"]}'
    return f'''
        <article class="prod" data-cat-item data-title="{p["title"]}">
          <a class="prod-media" href="{p["link"]}" target="_blank" rel="nofollow sponsored noopener noreferrer" aria-label="{p["title"]}">
            <img src="{a}" alt="{p["title"]}" loading="lazy" decoding="async" onerror="this.onerror=null;this.src='{depth}assets/ph-christmas.svg'">
            {chip}
          </a>
          <div class="prod-body">
            <span class="prod-meta">3D Model</span>
            <a class="prod-title" href="{p["link"]}" target="_blank" rel="nofollow sponsored noopener noreferrer">{p["title"]}</a>
            <p class="prod-desc">{p["desc"]}</p>
            <div class="prod-foot"><a class="btn btn--sm" href="{p["link"]}" target="_blank" rel="nofollow sponsored noopener noreferrer">Download Design{SVG_GO}</a></div>
          </div>
        </article>'''

# ---- HOMEPAGE ----
def build_home():
    # featured: one hero tile per category (first product)
    tiles = []
    for slug, c in CAT.items():
        p = c["products"][0]
        tiles.append(f'''
          <div class="hero-tile">
            <img src="assets/img/{p["img"]}" alt="{p["title"]}" loading="eager">
            <span class="tag">{c["abbr"]}</span>
          </div>''')
    tiles_html = "".join(tiles[:4])

    # theme cards (bento: first card spans 2 cols occasionally)
    cards = []
    for i, (slug, c) in enumerate(CAT.items()):
        n = len(c["products"])
        extra = ' style="grid-column: span 2"' if i == 0 else ""
        cards.append(f'''
          <a class="kit" href="{slug}/" {extra}>
            <div class="kit-media"><img src="assets/img/{c['products'][0]['img']}" alt="{c['name']}" loading="lazy" decoding="async" onerror="this.onerror=null;this.src='assets/ph-{slug}.svg'"></div>
            <div class="kit-body">
              <h3>{c["name"]}</h3>
              <p class="kit-note">{c['products'][0]['note']}</p>
              <div class="kit-foot"><span class="count">{n} models</span><span class="go">Explore {SVG_GO}</span></div>
            </div>
          </a>''')
    cards_html = "".join(cards)

    # popular strip: 8 evenly spread products
    flat = [(slug, c, p) for slug, c in CAT.items() for p in c["products"]]
    popular = flat[::max(1, len(flat)//12)][:12]
    pop_html = "".join(product_card(p, "", str(i+1).zfill(2)) for i,(s,c,p) in enumerate(popular))

    # stats
    total = sum(len(c["products"]) for c in CAT.values())
    cats = len(CAT)
    stats = f'''
      <div class="stats">
        <div class="stat"><b>{total}</b><span>printable models indexed</span></div>
        <div class="stat"><b>{cats}</b><span>curated theme collections</span></div>
        <div class="stat"><b>FDM</b><span>hobby-printer friendly</span></div>
        <div class="stat"><b>0</b><span>paywalls, 0 accounts</span></div>
      </div>'''

    swap_words = "printed|displayed|finished|on your shelf|in one sitting"
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>3D PRINT — Printable 3D Models for Every Season &amp; Room</title>
<meta name="description" content="A curated index of {total} printable 3D models: Christmas, Halloween, dragons, flexi toys, organizers, planters and more. Guides included — pick a theme and start printing.">
<meta property="og:title" content="3D PRINT — Printable 3D Models for Every Season & Room">
<meta property="og:description" content="A curated index of {total} printable 3D models with direct links to every source file.">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/genesis.css">
<script src="assets/genesis.js" defer></script>
</head>
<body>
{nav(active="home", depth="")}
<main>
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <span class="overline hero-eyebrow">3D PRINT &middot; Print it yourself</span>
        <h1>Real 3D models, ready to be <span class="swap" data-swap="{swap_words}"><span class="word">printed</span><span class="word">displayed</span><span class="word">finished</span><span class="word">on your shelf</span><span class="word">in one sitting</span></span>.</h1>
        <p class="hero-lede">No accounts, no paywalls, no filler. A calm index of printable 3D models — articulated dragons, festive decor, desk organizers — each linked straight to its source file. Pick a theme, hit print, watch it appear.</p>
        <div class="hero-cta">
          <a class="btn btn--lg" href="#themes">Browse the themes {SVG_GO}</a>
          <a class="btn btn--lg btn--secondary" href="blog/">Read the guides</a>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-dots"></div>
        <div class="hero-tiles">{tiles_html}</div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="overline">By the numbers</span>
        <h2>A catalog you can actually trust.</h2>
        <p>Every card is a direct link to the model's own page. Nothing re-hosted, nothing gated.</p>
      </div>
      {stats}
    </div>
  </section>

  <section class="section section--alt" id="themes">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="overline">Collections</span>
        <h2>Browse by theme</h2>
        <p>Twelve collections, each a self-contained set of printable models with direct links to every source file.</p>
      </div>
      <div class="card-grid reveal">{cards_html}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="overline">Featured</span>
        <h2>Models worth a first print</h2>
        <p>A spread pulled from across the catalog — festive, functional, and a few that are just fun to watch come off the bed.</p>
      </div>
      <div class="prod-grid reveal">{pop_html}</div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="steps reveal">
        <div class="step"><span class="step-n">01</span><h3>Pick a theme</h3><p>Browse the twelve collections and find the model that fits your shelf, desk or party.</p></div>
        <div class="step"><span class="step-n">02</span><h3>Open the model</h3><p>Every card links straight to the model page — files, license and price live on the source, never gated here.</p></div>
        <div class="step"><span class="step-n">03</span><h3>Slice &amp; print</h3><p>Run the file through our preparation checklist and press print. The first layer is the only one you watch.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cta-banner reveal">
        <div>
          <span class="overline" style="color:var(--primary)">Start here</span>
          <h2>The shelf-settlers</h2>
          <p>Planters with personality, quiet statues, and a few internet-famous figurines that round out a home collected rather than decorated.</p>
        </div>
        <a class="btn" href="decor-planters/">Explore Decor &amp; Planters {SVG_GO}</a>
      </div>
    </div>
  </section>
</main>
{footer(depth="")}
</body>
</html>'''
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
    print("home -> index.html")

# ---- CATEGORY PAGES ----
def build_cat(slug, c):
    cards = "".join(product_card(p, "../", str(i+1).zfill(2)) for i, p in enumerate(c["products"]))
    n = len(c["products"])
    lede = c["products"][0]["note"]
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["name"]} — 3D Print Models | 3D PRINT</title>
<meta name="description" content="{c['name']}: {n} printable 3D models with direct links. {lede}">
<meta property="og:title" content="{c['name']} — 3D Print Models | 3D PRINT">
<meta property="og:description" content="{n} printable 3D models with direct links to every source file.">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/genesis.css">
<script src="../assets/genesis.js" defer></script>
</head>
<body>
{nav(active=slug, depth="../")}
<main>
  <section class="cat-hero">
    <div class="wrap">
      <div class="crumbs"><a href="../">Home</a> / <span>{c["name"]}</span></div>
      <h1>{c["name"]}</h1>
      <p class="lede">{lede}</p>
      <div class="cat-count">
        <span class="chip chip--indigo">{n} printable models</span>
        <span class="chip">direct links</span>
        <span class="chip">free to browse</span>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="search-inline" style="margin-bottom:24px">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <input type="search" data-search-input placeholder="Filter {n} models by name…" aria-label="Filter models">
        <span class="kbd">⌘K</span>
      </div>
      <div class="prod-grid" data-filter-group>{cards}</div>
    </div>
  </section>
</main>
{footer(depth="../")}
</body>
</html>'''
    d = os.path.join(ROOT, slug)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    print(f"{slug} -> {n} products")

for slug, c in CAT.items():
    build_cat(slug, c)
build_home()
print("DONE")
