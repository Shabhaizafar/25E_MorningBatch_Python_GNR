# Tuple

# Definition: A tuple is an ordered, immutable (unchangeable) collection of items.

# Syntax: Defined using parentheses ( ).

# Example:


# Order : 
# input data : 11,12,13
# Output :     11,12,13

# UnOrdered : 
# input data : 11,12,13
# Output :     11,12,13     12,11,13    12,13,11  etc


# Properties:

# Immutable → Once created, you cannot modify elements (no add/remove).

# Allows duplicate values.

# Can store mixed data types.

# Has fewer methods than lists (mainly .count() and .index()).



# https://www.w3resource.com/python-exercises/tuple/



# Empty Tuple :

# Method : 1
# mytuple = ()
# print(mytuple)
# print(type(mytuple))
# Method : 2
# mytuple = tuple()
# print(mytuple)
# print(type(mytuple))



# fullfil tuple :
# mytuple = (11,12,13)
# print(mytuple)
# print(type(mytuple))




# -------------------------------------------------------- #

# mytuple = (11,1,2,23,45,1,5,6,7,1,2,7,9,0,1)
# print(mytuple)


# 1. index: 
# return : index of element if exist else gives an error  "ValueError: tuple.index(x): x not in tuple"
# print(mytuple.index(3))


# 2. count : 
# return : count of value if it's exist else : 0
# print(mytuple.count(1))
# print(mytuple.count(3))




mytuple = (11,23,45,67,89,64,21)

print(len(mytuple))

print(mytuple[2])

# for i in mytuple:
#     print(i)

for i in range(0,len(mytuple)):
    print(i,mytuple[i])