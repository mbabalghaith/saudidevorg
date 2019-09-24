def myfunc(names):
    for x in names:
        print (x)

def myfunc2(x):
    return x * 5


def myfunc3(*key):
    print ("The youngest kid is " + key[3])


def myfunc4(x):
    if (x>0):
        result = x + myfunc4(x-1)
        print (result)
    else:
        result = 0
    return result


#---------------------------------------------------



x = ['mohammed','ali','ahmed','khaled']
myfunc(x)
print ('----------------------')

print (myfunc2(3))
print (myfunc2(5))

print ('---------------------')

myfunc3('mohammed','ali','khaled','ahmed','nasser')

print ('---------------------')

print ("Resursion Example Results")
print (myfunc4(6))