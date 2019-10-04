class person:
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname

    def myfunc(self):
        print (self.fname , self.lname ,' you will be programmer if you work hard')

class student2(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = person(input('Enter your first: '),input('Enter your last name: '))
x.myfunc()
print ('-----------------------------')
d = student2(input('Enter your first: '),input('Enter your last name: '))
d.myfunc()
