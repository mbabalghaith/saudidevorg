def myfunc(n):
    return lambda a : a * n


def myfunc2(n,m):
    return lambda a : a + n + m



z = 2
c =3
d = 4
m = myfunc(3)

print (m(5))
print ('------------------')
y = myfunc2(z,c)
print (y(d))
