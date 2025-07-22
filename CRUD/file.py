import sqlite3  

mydb = sqlite3.connect("school.db") 

mycursor =  mydb.cursor()

mycursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT NOT NULL,                 
    email TEXT UNIQUE NOT NULL
)
''')
mydb.commit()


while(True):
    print("Welcome to the Student Management System")
    print("-----------------------------------------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Info")
    print("5. Delete Student")
    print("6. Out")

    choice = int(input("Enter Your Choice(1-6) :"))

    match choice:
        case 1 :   
                name = input("Enter Student name : ")
                age = int(input("Enter Student age : "))
                gender = input("Enter Student gender : ")
                email = input("Enter Student email : ")
                mycursor.execute("INSERT INTO students(name,age,gender,email) VALUES (?,?,?,?)",(name,age,gender,email))
                mydb.commit()
                print("Added !!")
        case 2 :   
                ch = int(input("1. View a student by id\n2. View students by gender \n Enter Your Choice :"))
                mycursor.execute("select * from students")
                alldata = mycursor.fetchall()
                for i in alldata : 
                       print(i)
                # match ch:
                #     case 1 :
                #             ch2 = int(input("1. Acending \n2. Descending \n Enter Your Choice : "))
                #             match ch2 :
                #                    case 1 :print()
                #                    case 2 :print()
                #     case 2 :
                #             ch2 = int(input("1. Acending \n2. Descending \n Enter Your Choice : "))
                #             match ch2 :
                #                    case 1 :print()
                #                    case 2 :print()
        case 4 :           
                  id = int(input("Enter Student Id : "))
                  name = input("Enter Student name : ")
                  age = int(input("Enter Student age : "))
                  gender = input("Enter Student gender : ")
                  email = input("Enter Student email : ")
                  sql = "UPDATE students SET name = ?, age = ?, gender = ?,email=? WHERE id = ?"
                  val = (name, age, gender,email, id)
                  mycursor.execute(sql, val)
                  mydb.commit()
                  print("Updated !!")
        case 5 :   
                id = int(input("Enter Student Id : "))
                if input("Are you sure ?").lower()== "yes" :
                       mycursor.execute('DELETE FROM students WHERE id = {0}'.format(id))
                       mydb.commit()
                       print("Deleted Successfully !!")
                else:
                       print("Delete Operation Abort !!")
                       
        case 6 :       
                print("Exit !!!")    
                break
        

mycursor.close()












