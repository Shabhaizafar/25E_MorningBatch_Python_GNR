# inheritance in a Python : 
'''
Inheritance is an Object-Oriented Programming (OOP) feature that allows one class (called child class or subclass) to inherit properties and behaviors (methods) from another class (called parent class or superclass).
'''

"""
| Inheritance Type                | Description                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------- |
| 1. **Single Inheritance**       | A child class inherits from one parent class.                                     |
| 2. **Multiple Inheritance**     | A child class inherits from more than one parent class.                           |
| 3. **Multilevel Inheritance**   | A child class inherits from a parent, which in turn inherits from another parent. |
| 4. **Hierarchical Inheritance** | Multiple child classes inherit from a single parent class.                        |
| 5. **Hybrid Inheritance**       | A combination of two or more types of inheritance.                                |

"""

# Single Level Inheritance : 

'''
class parent:
    pass 

class child(parent):
    pass 
'''

# class Father : 
#     def __init__(self,fname,lname):
#         self.fathername = fname 
#         self.surname = lname
    
#     def father_display_data(self):
#         print(f"Name : {self.fathername} \nSurname : {self.surname}.")

# Object using only father class : 
# f1 = Father("Rajesh","Sharma")
# f1.father_display_data()

# class Child(Father) : 
#     def __init__(self,cname,fname,lname):
#         super().__init__(fname,lname)
#         self.childname = cname


# c1 = Child("Raj","Rajesh","Sharma")

# c1.father_display_data()








'''
Employee Details
Create a class Employee with details like name, id, and salary.
Inherit it in a class Manager that adds a method to assign_task().
'''