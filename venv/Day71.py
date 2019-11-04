import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'py_database'
)
if con:
    print ('Connection was secsasfull')
    mycursor = con.cursor()

sql = 'INSERT INTO Customers (name , address) VALUES(%s, %s)'
#val = [
    #('Shorog Mohammed','Salheiya'),
   # ('Ibrahim khalid' , 'Olaya'),
    #('Abdullah ahmed','Mansorah'),
    #('Maha ali ','khaldia')
 # ]
#mycursor.executemany(sql , val)

#con.commit()
#print ('1 record inserted, ID:' , mycursor.lastrowid)

#mycursor.execute('SELECT * FROM Customers')
#result = mycursor.fetchall()
#for x in result:
    #print (x)

print ('-------------------------')

mycursor.execute('SELECT name FROM Customers')
result = mycursor.fetchall()

for x in result:
    print (x)

print ('--------------------------')
mycursor.execute('SELECT * FROM Customers WHERE address = "Olaya" ')

result = mycursor.fetchall()

for x in result:
    print (x)