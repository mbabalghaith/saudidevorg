import re


text = 'Please, I want {} sandwishes and {} donutes'
print (text)
print ('--------------------')
print ('ex1: replace i with we')

text = text.replace('I' , 'We')

print (text)

z = 5
y = 7
       
print ('---------------------')
print('ex2: use format')      

text = text.format(z,y)

print (text)

print ('---------------------')

print ('ex3: use uppercase to convert a to A ')

change_to_upper = 'a'
text = re.sub(change_to_upper, change_to_upper.upper(), text)

print (text)


  
