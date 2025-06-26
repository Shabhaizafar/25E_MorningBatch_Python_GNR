'''

### 🔹 2. **Multiple Inheritance**

* A child class inherits from **more than one** parent class.

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

'''

# class Father : 
#     def __init__(self,fname):
#         self.fathername = fname 

#     def brave(self): 
#         print("I am Brave !!")

# class Mother : 
#     def __init__(self,mname):
#         self.mothername = mname 

#     def loving():
#         print("Loving Nature !!")


# class Child(Father,Mother):
#     def __init__(self,cname,fname,mname):
#         Father.__init__(self,fname)
#         Mother.__init__(self,mname)
#         self.childname = cname 

#     def display(self):
#         print("My name is {}.My Father name is {}. My Mother name is {}.".format(self.childname,self.fathername,self.mothername))


# c1 = Child("Raj","Rajesh","Ramila")
# c1.display()

'''

### 🔹 3. **Multilevel Inheritance**

* A class is derived from a child class, which is itself derived from another parent class.

```python
class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass
```

'''

# class Grandfather : 
#     def __init__(self,gname,lname):
#         self.grandfathername = gname 
#         self.surname = lname

# class Father(Grandfather) : 
#     def __init__(self,fname,gname,lname):
#         super().__init__(gname,lname)
#         self.fathername = fname 

# class Child(Father) : 
#     def __init__(self,cname,fname,gname,lname):
#         super().__init__(fname,gname,lname)
#         self.childname = cname
    
#     def display(self):
#         print("My name is {} {}.My Father name is {} {}. My GrandFather name is {} {}".format(self.childname,self.surname,self.fathername,self.surname,self.grandfathername,self.surname))


# c1 = Child("Raj","Rajesh","Rajendra","Shrama")

# c1.display()





'''

### 🔹 4. **Hierarchical Inheritance**

* Multiple child classes inherit from a single parent class.

```python
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass
```

'''

'''

### 🔹 5. **Hybrid Inheritance**

* A combination of two or more types of inheritance (e.g., multiple + multilevel).

```python
class A:
    pass

class B(A):
    pass

class C:
    pass

class D(B, C):  # Combines multiple and multilevel
    pass
'''

######################################
"""

### **1. Multilevel Inheritance**

**Question:**
Create a Python program using multilevel inheritance to model a **Library System**, where:

* `Library` class has general library info.
* `BookSection` inherits from `Library` and adds section info.
* `Book` inherits from `BookSection` and has details about individual books.

Demonstrate how data flows through all three levels.

---

### **2. Multiple Inheritance**

**Question:**
Design a Python program using multiple inheritance to simulate a **Smartphone**:

* `Camera` class handles photo and video functionality.
* `MusicPlayer` class handles song playback.
* `Smartphone` inherits from both and integrates both features.

Show how the `Smartphone` class can use methods from both parents.

"""