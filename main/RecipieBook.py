#Importing MYSQL Connector
import mysql.connector as cnt

#Establishing the connection with database
mydb = cnt.connect(host = 'localhost',
                               user = 'aurelius',
                               password = 'aurelius.141')
#Checking the connection
if mydb.is_connected():
    print ("### Connection Established ###")
else:
    print("### Connection Failed ###")

#Creating a cursor object
exe = mydb.cursor()

db = exe.execute("SHOW DATABASES")
db_r = exe.fetchall()

if ('Recipie_Book',) in db_r:
    print('*Database Exists*')
else:
    print('*Database not found*')
    print('*Creating Database*')
    db_c = exe.execute('CREATE DATABASE Recipie_Book')

