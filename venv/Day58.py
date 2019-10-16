import re

txt = 'You will be Programmer soon ..'

x = re.findall('o' , txt)
print (x)
print ('-------------------')

str = 'Many teams had won in asian cup'

y = re.findall('Alnasser' , txt)
print (y)
if (y):
    print (' I do not think .. ')
else:
    print ('That what i know :)')
print ('--------------------')



s = re.search("\s" , txt)

print ('The first white-space character is located in position:' , s.start())
