# class Person:
#     pass


# # How to create an Object using class : 
# '''
# objname = classname()
# '''
# p1 = Person()
# print(p1)


# p2 = Person()
# print(p2)



# How to Access default Property/Attributes Value in Object : 

# class Shape : 
#     data1 = "Circle"
#     data2 = 5 


# s1 = Shape()
# print(s1.data1)

# s2 = Shape()
# print(s2.data2)



# How to Access default Methods Value in Object : 

class Shape : 
    data1 = "Circle"
    data2 = 5 

    def saySomthing(self): 
        print("default Method")



s1 = Shape()

s1.saySomthing()