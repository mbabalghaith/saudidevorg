import json

x = '{"name" : "Mohammed" , "age" : 45 , "City" : "Riyadh"}'

y = json.loads(x)

print (y["age"])

m = {"name" : "Mohammed" , "age" : "45" , "City" : "Riyadh"}

c = json.dumps(x)

print (c)
print('---------------------------------')



print (json.dumps({'name':'ali' , 'age':'34'}))
print (json.dumps(['blue','red','yellow']))

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

f = json.dumps(g)

print (f)

