#WebScrapping using Regular Expression.

import re,urllib
import urllib.request
sites=["https://google.co.in","https://rediff.com"]
for s in sites:
    u=urllib.request.urlopen(s)
    print("searching...",s)
    text=u.read()
    title=re.findall('<title>.*</title>',str(text),re.IGNORECASE)
    print("Extracting title for",s)
    print(title)
