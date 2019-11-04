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

#mycursor.execute('CREATE DATABASE py_database')

mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print (x)
print ('----------------------')

#mycursor.execute('CREATE TABLE Customers (name VARCHAR(100), address VARCHAR(150))')

mycursor.execute('SHOW TABLES')

for x in mycursor:
    print (x)
print ('------------------------')

mycursor.execute('ALTER TABLE Customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')