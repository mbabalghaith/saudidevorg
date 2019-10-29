print ('EX1: ')

a = input('Enter firest latter from your name: ')

b = input('Enter last latter from your name: ')

txt = 'First latter from your name is {} , last latter from your name is {}'

print (txt.format(a , b))

print ('-----------------------')
print ('EX2: ')
m = 'Ahmed Ali'

price = 53.44

txt2 = 'Dear {personname}, Your current balance is {price}$'

print (txt2.format(personname = 'Ahmed ali' , price = 53.44))
print ('-----------------------')

print ('EX3: ')

x = input('Enter number of matrix: ')

try:
    x = int(x)
    y = []
    print ('plese fill the matrix: ')
    for i in range(x):
        y.append(input())
    print ('your array: ' , y)
except:
    print ('something rong')


