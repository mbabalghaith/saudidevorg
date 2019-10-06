def myfunc():
    x = 20
    print (x)


x = 50
print (x)
myfunc()
print ('---------------')


def myfunc2():
    x = 70
    def myfun3():
        print (x)
    myfun3()


myfunc2()
print (x)

print ('---------------------')


m = 500

def myfunc4():
   
    m = 100

myfunc4()

print (m)
