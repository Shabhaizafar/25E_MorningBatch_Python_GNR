'''
class Classname :
    code

'''


# How to Create Empty Class : 
# class Person:
#     pass



# print(Person)
# print(type(Person))



# How to add default Data/Attributes/Property:

# class Person:
#     firstname = "Raj"     # Data/Attributes/Property
#     lastname = "Shah"     # Data/Attributes/Property



# How to access Data/Attributes/Property using class and without Object : 
# print(Person.firstname)

# print(Person['firstname'])   # error  # invalid




# How to Create a Method in a Class : 

class Person:
    firstname = "Raj"     # Data/Attributes/Property
    lastname = "Shah"     # Data/Attributes/Property

    def sayHello():       # Methods
        print("Hello Everyone")


# How to Access a Method in a Class : 
Person.sayHello()