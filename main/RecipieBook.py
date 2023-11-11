#Importing MYSQL Connector
import mysql.connector as cnt

#Establishing the connection with MYSQL
mysql = cnt.connect(host = 'localhost',
                               user = 'aurelius',
                               password = 'aurelius.141')

#Checking for the desired database and creating it otherwise
if mysql.is_connected():
    print("---------------------------------------------------------------------------------")
    print("|                 ### Connection Established with MYSQL ###                     |")
    print("---------------------------------------------------------------------------------")

else:
    print("### Connection Failed ###")
exe = mysql.cursor()

db = exe.execute("SHOW DATABASES")
db_r = exe.fetchall()

def database():
    print("Changing Database")
    global mydb
    mydb = cnt.connect(host = 'localhost',
                               user = 'aurelius',
                               password = 'aurelius.141',
                               database = 'Recipe_Book')
    if mydb.is_connected():
        print("---------------------------------------------------------------------------------")
        print("|               ### Connection Established with Recipie_Book ###                |")
        print("---------------------------------------------------------------------------------")
    else:
        print("Connection Failed")
   
if ('Recipe_Book',) in db_r:
    print('*Database Exists*')
    database()
else:
    print('*Database not found*')
    print('*Creating Database*')
    db_c = exe.execute('CREATE DATABASE Recipe_Book')
    database()

cur = mydb.cursor()
#CREATING TABLES
tables = cur.execute("SHOW TABLES")
tables_r = cur.fetchall()
if ('RECIPES',) not in tables_r :
    cur.execute("CREATE TABLE RECIPES(recipe_name varchar(255) primary key,cuisine varchar(255),country varchar(20))")

def CHOICES():
    print("---------------------------------------------------------------------------------")
    print('|                          WHAT ARE YOU HERE FOR TODAY?                         |')
    print('---------------------------------------------------------------------------------')
    print("|                   Enter VIEW for viewing existing Recipies                    |")
    print('|             Enter ADD if you want to save your personal recipes               |')
    print('|         Enter TRY if you want instructions to try a certain recipe            |')
    print('---------------------------------------------------------------------------------')
    print()
    choice = input("Enter your choice: ")

CHOICES()