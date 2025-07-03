# public / protacted  / Private  with variable :
# ==============================================
# public : 

# class Myclass1:
#     def __init__(self):
#         self.firstname = "Rajendra"   # firstname : public

# myobj1 = Myclass1()
# print(myobj1.firstname)

# protected : 
# class Myclass2:
#         def __init__(self):
#             self._firstname = "Rajendra"

# class A(Myclass2) : 
#       def __init__(self):
#             super().__init__()

# class B(A):
#       def __init__(self):
#             super().__init__()
      

# myobj2 = Myclass2()
# print(myobj2._firstname)

# myD = B()
# print(dir(myD))

# private : 
# class Myclass3:
#     def __init__(self):
#         self.__fname = "Raj"

#     def getData(self):
#         return self.__fname



# myobj3 = Myclass3()

# print(myobj3.__fname)
# print(myobj3.getData())
'''------------------------------------------------------------------------------------------'''
# public / protected  / Private  with method :
# ==============================================

class MyClass1:
    def public_method(self):
        print("Public Method")

    def _protected_method(self):
        print("protected Method")

    def __private_method(self):
        print("Private Method")


obj1  = MyClass1()

# print(dir(obj1))

# obj1.public_method()
# obj1._protected_method()
# obj1.__private_method()
obj1._MyClass1__private_method()




'''

### 🧠 **Question:**

You are designing a system for a **Bank Account Management** system in Python.

* Every **Account** has a public method to display account info, a protected method to calculate interest, and a private method to generate a secret PIN.
* Variables: `account_holder` (public), `_balance` (protected), `__pin` (private).

**Write a Python class** to represent this scenario and demonstrate:

1. Access to the public, protected, and private variables and methods from:

   * Inside the class
   * A subclass
   * Outside the class

Also, explain what happens when you try to access the private variable or method directly from outside the class.

'''