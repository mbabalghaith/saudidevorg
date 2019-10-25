price = 56

txt = 'The price is {} dollars'

print (txt.format(price))

print ('-----------------------')

txt = 'The price is {:.3f} dollars'

print (txt.format(price))

print ('---------------------------')

q = 5

item = 435

pr = 123

order = 'I want {} pieces of item number {} for {:.2f} dollars.'

print (order.format( q , item , pr))
