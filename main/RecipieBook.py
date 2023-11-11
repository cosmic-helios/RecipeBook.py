#Importing MYSQL Connector
import mysql.connector as cnt

#Establishing the connection with MYSQL
mysql = cnt.connect(host = 'localhost',
                               user = 'aurelius',
                               password = 'aurelius.141')

#Checking for the desired database and creating it otherwise
if mysql.is_connected():
    print ("### Connection Established with MYSQL ###")
else:
    print("### Connection Failed ###")
exe = mysql.cursor()

db = exe.execute("SHOW DATABASES")
db_r = exe.fetchall()

def database():
    print("Changing Database")
    mydb = cnt.connect(host = 'localhost',
                               user = 'aurelius',
                               password = 'aurelius.141',
                               database = 'Recipe_Book')
    if mydb.is_connected():
        print("Connection Established with Recipie_Book")
    else:
        print("Connection Failed")
    
if ('Recipe_Book',) in db_r:
    print('*Database Exists*')
    database()
else:
    print('*Database not found*')
    print('*Creating Database*')
    db_c = exe.execute('CREATE DATABASE Recipe_Book')