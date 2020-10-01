import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input("enter:")
url_op=urllib.request.urlopen(url).read()
summ=0
tree=ET.fromstring(url_op)
counts = tree.findall('.//count')
for i in counts :
    count = int(i.text)
    summ+= count
print('count:',len(counts))
print('sum:',summ)
