import re

h = open(r"C:\Users\1999d\OneDrive\Documents\Default Project\3d-prinr-site\index.html", encoding="utf-8").read()
for tag in ["div", "section", "article", "a", "main", "header", "footer", "ul", "li", "nav"]:
    o = len(re.findall(r"<%s(\s|>)" % tag, h))
    c = h.count("</%s>" % tag)
    flag = "OK" if o == c else "MISMATCH!"
    print(f"{tag:10} open={o} close={c} {flag}")
print("len:", len(h))
