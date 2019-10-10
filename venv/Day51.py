import mymodule as mx
import platform

a = mx
m = input("Enter you name: ")

a.greeting(m)

print ('--------------')

x = platform.system()
print (x)
print (platform.python_version())
print ('-----------------')

print (dir(platform))