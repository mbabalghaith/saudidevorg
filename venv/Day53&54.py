import module5354 , datetime

a = module5354

print ("EX1:")
print (a.addfun(8 , 1))
print (a.subfun(4,2))
print (a.mulfun(6 , 6))
print (a.devfun(8 , 2))

print ('---------------------')
print ('EX2:')
b = datetime.datetime.now()


print (b.strftime("%Y"))
print (b)
print (b.strftime("%B"))
print (b.strftime("%A"))

print ('----------------------')
print ('EX3:')
c = datetime.datetime(2019 , 10 , 9)
d = datetime.datetime(2019 , 10 , 11)
print ('Date of yesterday: ', c)
print ('Date of tomorrow: ', d)