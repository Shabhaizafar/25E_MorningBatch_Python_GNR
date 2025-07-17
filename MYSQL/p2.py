import sqlite3   # sql impletemnt

mydb =  sqlite3.connect("mydb2.db")  # db create     in sql : create database dbname if doesn't exist

mycursor = mydb.cursor()     #  in SQL   : use dbname;

'''
in SQL : 

CREATE TABLE  EMPLOYEES  IF DOESN'T EXISTS(
    EMP_ID INT PRIMARY KEY,
    EMP_NAME VARCAR(50),
    SALARY INT DEFAULT 25000
)
'''

'''
# CREATE  TABLE
mycursor.execute("""
CREATE TABLE IF NOT EXISTS EMPLOYEES (
    EMP_ID INT PRIMARY KEY,
    EMP_NAME VARCAR(50),
    SALARY INT DEFAULT 25000
)
""")

ID = int(input("ENTER ID :"))
NAME = input("ENTER NAME :")
SALARY = int(input("ENTER SALARY :"))

# INSERT DATA
mycursor.execute('INSERT INTO EMPLOYEES VALUES (?,?,?)',(ID,NAME,SALARY))
# mycursor.execute(f'INSERT INTO EMPLOYEES VALUES ({0},{1},{2})',(ID,NAME,SALARY))   # DON'T USE THIS METHOD
mydb.commit()

'''

# READ :

mycursor.execute('SELECT * FROM EMPLOYEES')
ALLDATA = mycursor.fetchall()

# print(ALLDATA)

for I in ALLDATA: 
    print(I)


mycursor.close()