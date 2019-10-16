import json

g = {
    "name" : "Mohammed" ,
    "age" : "56" ,
    "married" : True,
    "children" : ("nasser","hamad"),
    "pets": None,
    "cars":[
        {"model": "bmw 230" , "mpg" : 27.5},
        {"model":"Ford Edge" , "mpg" : 22.9}
        ]
    }

print (json.dumps(g, indent = 5, separators = (". ", " = ")))
print ('------------------------------------------------')
print (json.dumps(g , indent = 4 , sort_keys = True))
