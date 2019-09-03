names = ['Mohammed' , 'Khaled', 'Ali' , 'Maha' , 'Wafa' , 'Hassan' , 'Waleed' ,'Lena']

print ( 'Print some elements from the list ' , names[3:7])

print('----------------------')

dep = ['HR', 'IT' , 'SR','EM']

print ('Print some element from 2 lists together', names[0:3] + dep[0:2])

print ('----------------------')

print ('Now start search some names from the list')
def findone(x):
    if x in names:
        print ('Yes' , x ,'is there')
        main()
    else:
        print ('NO' , x , 'is not there')
        main()

def main():
    y = input('Enter name:  ')
    findone(y)

main()
