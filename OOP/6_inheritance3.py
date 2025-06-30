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
# class Father :
#     fathername = "Rajesh"

#     def property(self):
#         print("honu : 1000kg\nGhar : 400 \njamin : 4000 viga")


# class Boy(Father) : 
#     childname = "Raj"

#     def biodata(self):
#         print(f"My name is {self.childname} {self.fathername}.")



# class Girl(Father) : 
#     childname= "Rina"
#     def biodata(self):
#         print(f"My name is {self.childname} {self.fathername}.")


# c1 = Boy()
# c2 = Girl()

# c1.property()
# c2.property()

# c1.biodata()
# c2.biodata()



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

class Company:
    companyname = "TATA SON & CO."

class Father(Company):
    fathername = "Rajesh"

    def Fatherwork(self):
        print(f'{self.fathername} is working in a {self.companyname}.')

class Mother:
    mothername = "Rina"

    def Motherprofile(self):
        print(f"{self.mothername} is a Housewife.")


class Child(Father, Mother): 
    childname = "Raj"

    def biodata(self):
        print(f"My name is {self.childname}.My Father is {self.fathername}.My  Mother name is {self.mothername}.")




c1 = Child()

c1.biodata()
c1.Fatherwork()
c1.Motherprofile()

print(c1.companyname)


'''


---





**Hierarchical Inheritance – Question:**
Create a Python program using hierarchical inheritance where a **base class `Vehicle`** is inherited by two subclasses: **`Car`** and **`Bike`**.
Each subclass should have its own method to display specific information.
Write a program to display the details of both `Car` and `Bike`.

---

**Hybrid Inheritance – Question:**
Create a Python program that demonstrates **hybrid inheritance** using a real-life scenario of a **`Person`**.

* `Person` is the base class.
* `Employee` and `Student` inherit from `Person`.
* `Intern` inherits from both `Employee` and `Student`.


'''


