import sqlite3 
import random


mydb = sqlite3.connect("BankManagement.db") 
mycursor = mydb.cursor()


mycursor.execute("""
CREATE TABLE IF NOT EXISTS ACCOUNT (
    account_no INTEGER PRIMARY KEY,
    account_holder VARCHAR(50),
    balance INTEGER NOT NULL
)
""")
mydb.commit()

print("\t\t\t\t--------------------------")
print("\t\t\t\t| Bank Management System |")
print("\t\t\t\t--------------------------")

print("Welcome to Our Bank !!")
choice = int(input("How can i Help you ?\n1. New Account\n2. Coming Soon\n3.Update Details\n4.Deactivate Account\n\nchoice your Topic : "))
match choice:
    case 1 :    
        account_no = int(random.random()*100000000000)
        account_holder = input("Enter Your Full Name :")
        balance = int(input("Add Amount : "))
        mycursor.execute('INSERT INTO ACCOUNT VALUES (?,?,?)',(account_no,account_holder,balance))
        mydb.commit()
        print("Successfully Added !!!")
    case 2 :    print("Coming Soon !!")
    case 3 :    
        account_holder = input("Enter Your Name : ")
        mycursor.execute("SELECT account_no FROM ACCOUNT WHERE account_holder = '{0}'".format(account_holder))
        data = mycursor.fetchone()
        if(data != None):
            account_no = data[0]
            account_holder = input("Update Name Here :")
            balance = int(input("Update Balance here : "))
            mycursor.execute("UPDATE ACCOUNT SET account_holder = '{0}',balance = {1} WHERE account_no = {2}".format(account_holder,balance,account_no))
            mydb.commit()
            print("Updated  Successfully !!")
        else:
            print("Account Doesn't Exist")

    case 4 :    
        account_holder = input("Enter Your Name : ")
        mycursor.execute("SELECT account_no FROM ACCOUNT WHERE account_holder = '{0}'".format(account_holder))
        data = mycursor.fetchone()
        if(data != None):
            if(input("Do you want to deactivate Your Account(yes)/(no) ?")=="yes"):
                account_no = data[0]
                mycursor.execute('DELETE FROM ACCOUNT WHERE account_no = {0}'.format(account_no))
                mydb.commit()
                print("Deactivate Successfully !!")
            else:
                print("Operation Cancelled !!!")
        else:
            print("Account Doesn't Exist")


# mycursor.execute('SELECT * FROM ACCOUNT')
# ALLDATA = mycursor.fetchall()

# print(ALLDATA)


# mycursor.execute("SELECT account_no FROM ACCOUNT WHERE account_holder = 'Raj RakeshBhai Shah'")

# data = mycursor.fetchone()
# print(data[0])
