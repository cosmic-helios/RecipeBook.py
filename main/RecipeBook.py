#Importing MYSQL Connector
import mysql.connector as cnt

#Establishing the connection with MYSQL
mysql = cnt.connect(host = 'localhost',
                               user = 'root',
                               password = 'root')

#Checking for the desired database and creating it otherwise
if mysql.is_connected():
    print("+-------------------------------------------------------------------------------+")
    print("|                 ### Connection Established with MYSQL ###                     |")
    print("+-------------------------------------------------------------------------------+")

else:
    print("|                    ### Connection Failed with MYSQL ###                       |")
exe = mysql.cursor()

db = exe.execute("SHOW DATABASES")
db_r = exe.fetchall()

def database():
    print("### Changing Database ###")
    global mydb
    mydb = cnt.connect(host = 'localhost',
                               user = 'root',
                               password = 'root',
                               database = 'recipe_book')
    if mydb.is_connected():
        print("+-------------------------------------------------------------------------------+")
        print("|                ### Connection Established with recipe_book ###                |")
        print("+-------------------------------------------------------------------------------+")
    else:
        print("### Connection Failed ###")
   
if ('recipe_book',) in db_r:
    print('### Database Exists ###')
    database()
else:
    print('### Database not found ###')
    print('### Creating Database ###')
    db_c = exe.execute('CREATE DATABASE recipe_book')
    print('### Database Created ###')
    database()

cur = mydb.cursor()
#CREATING TABLES
tables = cur.execute("SHOW TABLES")
tables_r = cur.fetchall()
if ('RECIPES',) not in tables_r :
    cur.execute("CREATE TABLE RECIPES(recipe_name varchar(255) primary key,cuisine varchar(255),country varchar(20),calories_kcal int)")

choice = ''
def CHOICES():
    print()
    print("+-------------------------------------------------------------------------------+")
    print('|                          WELCOME TO RECIPIE_BOOK                              |')
    print('+-------------------------------------------------------------------------------+')
    print("|                   Enter VIEW for viewing existing Recipies                    |")
    print('|             Enter ADD if you want to save your personal recipes               |')
    print('|                        Enter X if you want to quit                            |')
    print('+-------------------------------------------------------------------------------+')
    print()
    global choice
    choice = input("Enter your choice: ")
    choice.upper()

CHOICES()

def fetch_recipes(r):
    for i in range(len(r)):   
            print("---------------------------------------------------------------------------------")
            print("                                RECIPE #",i+1,"                                  ")
            print("---------------------------------------------------------------------------------")
            print('  Recipe Name: ',r[i][0],'                                                       ')
            print('  Cuisine: ',r[i][1],'                                                           ')
            print('  Country: ',r[i][2],'                                                           ')
            print('  Calories(kcal): ',r[i][3],'                                                    ')
            print("---------------------------------------------------------------------------------") 

def VIEW():
    print()
    print("-------------------------The Calories are in KCAL (100g)-------------------------")
    print()
    recipies = cur.execute('SELECT * FROM RECIPES')
    recipies_r = cur.fetchall()
    fetch_recipes(recipies_r)
    filter = input('Do you want to filter the recipes? Y/N: ')
    f = ['COUNTRY', 'CUISINE']
    print()
    if filter.upper() == 'Y':
        f = ['COUNTRY', 'CUISINE']
        print()
        print('Available Filters:',f)
        filter_2 = input("Enter A Filter: ")
        if filter_2.upper() == 'CUISINE':
            print()
            cuisine_i = input('ENTER CUISINE: ')
            cuisine_i.upper()
            cuisine_e = cur.execute(f"SELECT * FROM RECIPES WHERE cuisine = '{cuisine_i}'")
            cuisine_r = cur.fetchall()
            fetch_recipes(cuisine_r)
        if filter_2.upper() == 'COUNTRY' :
            country_i = input("Enter COUNTRY: ")
            country_i.upper()
            country_e = cur.execute(f"SELECT * FROM RECIPES WHERE country = '{country_i}'")
            country_r = cur.fetchall()
            fetch_recipes(country_r)
    

def ADD():
    print("---------------------------------------------------------------------------------")
    print("                         Enter the calories in kcal (100g)                       ")
    print("---------------------------------------------------------------------------------")
    print()
    name = input(' Enter Recipe Name: ')
    print()
    cuisine = input(" Enter cuisine of the recipe: ")
    cuisine.upper()
    print()
    country = input(" Enter the origin of the recipe: ")
    country.upper()
    print()
    calories = int(input(" Enter calories in kcal: "))
    print()
    print("---------------------------------------------------------------------------------")
    add_recipe = f"INSERT INTO RECIPES VALUES('{name}', '{cuisine}', '{country}', {calories})"
    add = cur.execute(add_recipe)
    print()
    print("                              Recipe Added :)                                    ")
    print()
    recipe_c = input("Would you like to view all the Added Recipes? Y/N")
    if recipe_c.upper() == 'Y':
        recipes_a = f"SELECT * FROM RECIPES WHERE recipe_name = '{name}'"
        recipes_ae = cur.execute(recipes_a)
        recipe_ar = cur.fetchall(recipes_ae)
        print(recipe_ar)

    mydb.commit()

def DEL():
    recipies = cur.execute('SELECT * FROM RECIPES')
    recipies_r = cur.fetchall()
    fetch_recipes(recipies_r)
    recipe_d = input("Enter name of the Recipe to Delete")
    del_exe = f"DELETE FROM RECIPES WHERE recipe_name = '{recipe_d}'"
    cur.execute(del_exe)
    print("Recipe Deleted :(")
    mydb.commit()

def tq():
    print(" Arigato :)")

choice.upper()
if choice == 'VIEW':
    VIEW()
elif choice == 'ADD':
    ADD()
elif choice == 'X':
    print()
    print(" Arigato :)")
elif choice == 'DEL':
    DEL()
else:
    ("                                Enter A Valid Option                                  ")
    CHOICES()