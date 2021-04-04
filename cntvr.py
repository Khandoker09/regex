import re

m = """xzcxzcxzcxzcz cxz https://some-url.domain asd sadfsa   safdafaf
            xzc zxcxzc
 xzcx zczxfcdsfgdjkhh io shooijsapidaohfodldfc
xfdfgdsftdsfgdsgdsgds
https://adf-url.domain  sdafsfdsgfsdgdsfgds 
https://some-url.com  sdfdgfsd gds g
www.somel.com    dsfdsf dsf 
dsf dsfds fdsf dsf d fsdadasdsa +
adad sadas dsad
sad s
"""

#print(re.search("(?P<url>https?://[^\s]+)", myString).group("url"))
print(re.sub(r'(https?:\/\/(?!.*:\/\/)\S+)', r'[[\1]]',m),file=open("header.md", "a"))
