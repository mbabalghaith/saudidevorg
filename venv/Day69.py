import os

f = open('demo.txt', 'r')

print (f.readline())
f.close()

print ('------------------------')



y = open('demo.txt' , 'r')

print (y.read())

print ('---------------------------')

m = open('demo.txt' , 'a')
m.write('Now the file has more content!')
m.close()
m = open('demo.txt','r')
print (m.read())
print ('---------------------------')

r = open('newfile1.txt' , 'x')
w = open('newfile1.txt' , 'a')
w.write('This is new file')
w.close()
r = open('newfile1.txt' , 'r')
print (r.read())

