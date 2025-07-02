# # Method Overloading:
# # Method overloading refers to the ability to define multiple methods within the same class that share the same name but differ in their parameters (number or type). Python, however, does not directly support method overloading in the traditional sense, as it is dynamically typed. If multiple methods with the same name are defined in a class, the last defined method will effectively "overwrite" previous definitions.



# # def add(n1,n2,n3=0):
# #     print(n1+n2+n3)
    


# # add(12,13)


# # add(12,13,1)


# # class Calculate : 
# #     def add(self,n1,n2):
# #         print(n1+n2)

# #     def add(self,n1,n2,n3):
# #         print(n1+n2+n3)



# # c1 = Calculate()

# # c1.add(12,13)
# # c1.add(12,13,1)


# # Method Overriding:
# # Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. The method in the subclass must have the same name and parameters as the method in the superclass. When an instance of the subclass calls this method, the subclass's implementation is executed instead of the superclass's. This allows for specialized behavior in derived classes while maintaining a common interface. 


# class Person:
#     def property(self):
#         print("1000kg gold")


# class Child(Person):
#     def property(self):
#         print("10000kg Gold")

# c1 = Child()

# # c1.property()

# print(dir(c1))







# Constructor Overloading:
# class Person:
#     def __init__(self,fname):
#         self.fname = fname
    
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname

# p1 = Person("Rajesh","12")


# print(p1.fname)

# Constructor Overriding:

# class Person:
#     def __init__(self):
#         print("Person Constructor")


# class Child(Person):
#     def __init__(self):
#         print("Child Constructor") 

# c1 = Child()    