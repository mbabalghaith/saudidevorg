import datetime

x = datetime.datetime.now()
print (x)
print (x.year)
print (x.strftime("%A"))
print ('--------------')

m = datetime.datetime(2030 , 1 , 1)
print (m)
print (m.strftime("%B"))
print (m.strftime("%Y"))
print (m.strftime("%M"))