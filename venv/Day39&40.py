def firstex(x,y):
   if y == 0:
       return 1
   else:
       return x * (firstex(x,y-1))

print (firstex(5,3))

print ('----------------')



a = [-4 , -6 , -5 , -1 , 2 ,3 , 7 , 9 , 88]

result = list(filter(lambda x: (x > 0), a))

print (result)
