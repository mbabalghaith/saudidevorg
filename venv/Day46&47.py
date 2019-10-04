class library:
    def __init__(self):
        self.shelf = 45
        self.book = 300

class science_section(library):
    def __init__(self):
        super().__init__()
        self.name = 'Pysics books'

cla1 = library()
cla2 = science_section()
print ('Ex1: type content of science section class:')
print ('Number of book = ' , cla2.book)
print ('Number of shlefs = ',cla2.shelf)
print ('------------------')

print ('Ex2: change values of science setion and type it:')
cla2.book = 20
cla2.shelf = 4
print ('Number of book = ' , cla2.book)
print ('Number of shlefs = ',cla2.shelf)