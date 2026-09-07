import re

import os
ROOT = r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site"
for path in ["index.html", "christmas/index.html"]:
    path = os.path.join(ROOT, path)
    h = open(path, encoding="utf-8").read()
    print(path)
    print("  articles:", h.count('<article class="prod"'), "/", h.count("</article>"))
    print("  divs open/close:", h.count("<div"), h.count("</div>"))
    print("  sections:", h.count("<section"), "/", h.count("</section>"))
    print("  hero words:", h.count('class="word"'))
    print("  mega items:", h.count('class="mega-item"'))
    print()
