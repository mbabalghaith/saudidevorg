class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def myfunc(self):
        print ('my name is ' + self.name)
        print ('my age is ', self.age)

p1 = person('mohammed' , 25)
p1.myfunc()
p1.age = 40 

print ('------------------')

p1.myfunc()
p2= person('ali',47)

p2.myfunc()
del p2.age
