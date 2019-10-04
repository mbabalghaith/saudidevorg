class person:
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname

    def myfunc(self):
        print (self.fname , self.lname ,' you will be programmer if you work hard')

class student(person):
    pass


class student2(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)

x = person(input('Enter your first: '),input('Enter your last name: '))
x.myfunc()
print ('-----------------------------')
d = student(input('Enter your first: '),input('Enter your last name: '))
d.myfunc()
print ('-----------------------------')
b = student2(input('Enter your first name: '),input('Enter your last name: '))
b.myfunc()
