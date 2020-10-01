import xml.etree.ElementTree as ET

data ='''
<person>
 <name>chuck</name>
  <phone type='intl'>
     +1 890 492 3839
    </phone>s
    <email hide ="yes"/>
</person>'''

tree =ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
