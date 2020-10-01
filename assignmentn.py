import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode =ssl.CERT_NONE

url=input('ENTER -')
html =urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('span')
for tag in tags:
    y=str(tags)
    x=re.findall("[0-9]+",y)
print(x)
summ=0
for i in x:
    i=int(i)
    summ=summ+i
print(summ)
