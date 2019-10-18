import re , json


tuple = ('Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday')
print ('Ex1:')
x = json.dumps(tuple)

print (x)

print ('----------------------')

txt = 'data is the new oil'
print('Ex2:')
y = re.search('data', txt)

print (y)

if (y):
    print("Yes it is there")
else:
    print ("No match")