import sqlite3   # sql impletemnt

mydb =  sqlite3.connect("mydb2.db")  # db create     in sql : create database dbname if doesn't exist

mycursor = mydb.cursor()     #  in SQL   : use dbname;



# DELETE
# mycursor.execute('DELETE FROM EMPLOYEES WHERE EMP_ID = 5')
# mydb.commit()
# ID = int(input("ID : "))
# # mycursor.execute('DELETE FROM EMPLOYEES WHERE EMP_ID = {0}'.format(ID))
# mycursor.execute(F'DELETE FROM EMPLOYEES WHERE EMP_ID = {0}'.format(ID))

# mydb.commit()

# UPDATE 
mycursor.execute('UPDATE EMPLOYEES SET EMP_NAME = "RAJAN" WHERE EMP_ID = 3')
mydb.commit()

# READ 
mycursor.execute('SELECT * FROM EMPLOYEES')

ALLDATA = mycursor.fetchall()
print(ALLDATA)  # USE LOOP FOR PRINT SINGLE SINGLE ROWS




mycursor.close()
