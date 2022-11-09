import sys
import os
with open(sys.path[0]+"/drag_temple.html", "rt")as f:
    content = f.read()
new = ""

for cp, dns, fns in os.walk("/Volumes/Exchange/Programs/Projects_HTML/geraniol.github.io/Pages/Public/img/pv"):
    for fn in fns:
        new += '\n<img id="'+fn+'" src="'+cp+'/'+fn + \
            '" draggable="true" ondragstart="drag(event)">\n'

content = content.replace("<!-- Images -->", new)
with open(sys.path[0]+"/drag.html", "wt")as f:
    f.write(content)
