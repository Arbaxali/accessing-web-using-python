import json
input ='''[
            {
             "id": "001",
              "name": "chuck",
               "x" : "2"
               } ,
            {
             "id": "002",
             "name": "chucka",
             "x": "3"
            }
         ]'''
info=json.loads(input)
print("user count",len(info))
for i in info:
    print("name:",i['name'])
    print("id:",i['id'])
    print("attributes:",i['x'])
