import sqlite3 

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
    case 1 :    print("Account Created !!")
    case 2 :    print("Coming Soon !!")
    case 3 :    print("Update Details !!")
    case 4 :    print("Deactivate")
