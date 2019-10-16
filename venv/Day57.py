import re

txt = 'You have to work hard'

x = re.search('^You.*hard$' , txt)

if (x):
    print ('YES! We have a match ..')
else:
    print ('No match')
print ('--------------------------')

y = re.findall("[You have]" , txt)
print (y)
