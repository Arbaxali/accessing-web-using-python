import xml.etree.ElementTree as ET

input ='''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>002</id>
<name>brent</name>
</user>
</users>
<stuff>
'''
stuff = ET.fromstring(input)
lst=stuff.findall('users/user')
print('user count:',len(lst))
for item in lst:
    print('Name:',stuff.find('name').text)
    print('Id',stuff.find('id').text)
    print('Attr',item.get("x"))
