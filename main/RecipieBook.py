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
    cur.execute("CREATE TABLE RECIPES(recipe_name varchar(255) primary key,cuisine varchar(255),country varchar(20)),calories(kcal) numeric")

choice = ''
def CHOICES():
    print()
    print("---------------------------------------------------------------------------------")
    print('|                          WELCOME TO RECIPIE_BOOK                              |')
    print('---------------------------------------------------------------------------------')
    print("|                   Enter VIEW for viewing existing Recipies                    |")
    print('|             Enter ADD if you want to save your personal recipes               |')
    print('---------------------------------------------------------------------------------')
    print()
    global choice
    choice = input("Enter your choice: ")

CHOICES()

def VIEW():
    recipies = cur.execute('SELECT * FROM RECIPES')
    recipies_r = cur.fetchall()
    print(recipies_r)
    filter = input('Do you want to filter the recipes? Y/N')
    if filter.upper() == 'Y':
        filter_2 = input("Enter Based On COUNTRY or CUISINE??  ")
        print(filter_2)
        if filter_2.upper() == 'CUISINE':
            cuisine_i = input('ENTER CUISINE: ')
            cuisine_i.upper()
            cuisine_e = cur.execute("SELECT * FROM RECIPES") #WHERE cuisine = cuisine_i
            cuisine_r = cur.fetchall()
            print(cuisine_r)
        if filter_2.upper() == 'COUNTRY' :
            country_i = input("Enter COUNTRY: ")
            country_i.upper()
            country_e = cur.execute("SELECT * FROM RECIPES WHERE country = 'country_i")
            country_r = cur.fetchall()
            print(country_r)

    

if choice == 'VIEW':
    VIEW()
'''elif choice == 'ADD':
    ADD()
elif choice == 'TRY':
    TRY()'''
