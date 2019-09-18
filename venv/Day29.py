for x in 'Mohammed':
    print (x)
print ('-----------------------')

y = ['Mohammed','ali','khalid','ahmed']

for x in y:
    print (x)
    if x == 'khalid':
        break

print ('---------------------------')

for x in y:
    if x == 'khalid':
        continue
    print (x)
