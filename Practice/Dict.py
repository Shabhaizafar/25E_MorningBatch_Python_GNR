"""

# 📘 **Easy Level (Basics of Dict in Python)**

1. Create a dictionary of 5 fruits with their prices. Print the price of "apple".
2. Add a new key `"grapes": 60` to an existing dictionary.
3. Remove a key `"banana"` from a dictionary using `pop()`.
5. Get all keys of a dictionary using `keys()` method.
6. Get all values of a dictionary using `values()` method.


"""


# 4. Write a program to check if a key `"mango"` exists in a dictionary. 
# fruits = {
#     "Mango" : 3,
#     "Apple" : 2
# }
# print("Mango" in fruits)
# 7. Merge two dictionaries into one.
# extra = {
#     "Banana" : 4
# }
# fruits.update(extra)
# print(fruits)


# 8. Write a program to create a dictionary with student names as keys and their marks as values. Print marks of "Rahul".

# students = {
#     "Rahul" : 67,
#     "Ramesh" : 90
# }
# print(students.get("Rahul"))

# 9. Write a program to find the length of a dictionary.
# students = {
#     "Rahul" : 67,
#     "Ramesh" : 90
# }
# print(len(students))

# 10. Clear all elements of a dictionary.
# students = {
#     "Rahul" : 67,
#     "Ramesh" : 90
# }
# print(students)
# del students
# print(students)


"""


# 📗 **Intermediate Level (Operations & Loops with Dict)**

2. Write a program to create a dictionary of squares of numbers from 1 to 10.
3. Write a program to iterate through all keys and values in a dictionary.
4. Write a program to find the maximum value in a dictionary.
5. Write a program to sort a dictionary by its keys.
6. Write a program to sort a dictionary by its values.


"""
# 1. Write a program to count the frequency of each character in a string using a dictionary.

# Method : 1 
# mystr = "Hello everyone,Welcome to Python !!!"
# mydict = {}
# for i in list(map(lambda x : {x : mystr.count(x)},mystr)):
#     mydict.update(i)
# print(mydict)

# Method : 2
# mystr = "Hello everyone,Welcome to Python !!!"
# mylist = list(map(lambda x : {x : mystr.count(x)},mystr))
# mydict = {}
# for i in mylist:
#     mydict.update(i)
# print(mydict)

# Method : 3 
# mystr = "Hello everyone,Welcome to Python !!!"
# mylist1 = list(map(lambda x : x,mystr))
# mylist2 = list(map(lambda x : mystr.count(x),mystr))
# mydisct = {}
# for i in range(0,len(mylist1)):
#     mydisct.update({mylist1[i] : mylist2[i]})

# print(mydisct)

# Method : 4 
# mydict = {}
# for i in mystr:
#     cout = 0
#     for j in mystr:
#         if(i==j):
#             cout+=1
#     mydict.update({i:cout})

# print(mydict)


# 7. Write a program to update the value of a key if it exists, else add it.
# students = {
#     "Rahul" : 67,
#     "Ramesh" : 90
# }

# students.update({"Ramesh":50})
# students.update({"Rakesh":50})

# print(students)

# 8. Write a program to swap keys and values in a dictionary.
# students = {
#     "Rahul" : 67,
#     "Ramesh" : 90
# }
# newdict = {}
# for i in students:
#     newdict.update({students[i]:i})

# print(newdict)


# 9. Write a program to create a dictionary from two lists (keys list and values list).
# mylist1 = ['Rahul', 'Ramesh']
# mylist2 = [67, 90]

# mydict = {} 

# for i in range(0,len(mylist1)):
#     mydict.update({mylist1[i]:mylist2[i]})

# print(mydict)

# 10. Write a program to check if two dictionaries are equal.
# mydict1 = {'Rahul': 67, 'Ramesh': 90}
# mydict2 = {'Rahul': 67, 'Ramesh': 90}

# print(mydict1 == mydict2)

"""


# 📙 **Advanced Level (Applications & Nested Dictionaries)**

1. Write a program to create a nested dictionary for 3 students with name, age, and marks.
2. Write a program to merge two dictionaries and add values for common keys.
4. Write a program to find the top 3 highest values in a dictionary.
5. Write a program to group words by their first letter using a dictionary.
9. Write a program to check if a dictionary is empty without using `len()`.

"""
# 3. Write a program to remove duplicate values from a dictionary.
# students = {
#     "Rahul" : 67,
#     "Ramesh" : 67,
#     "Raj" : 90
# }

# changedict = {}


# for i in set(students.values()):
#     counter = 0
#     for j in students:
#         if(i==students[j] and counter==0):
#             counter = 1
#             changedict.update({j:students[j]})
#         elif(i==students[j] and counter==1):
#             changedict.update({j:None})
# print(changedict)



# 6. Write a program to create an inverted index of words from a paragraph using a dictionary.
# mystr = "Hello Everyone Welcome to JS"
# mydict = {}

# for i in range(0,len(mystr.split(' '))):
#     mydict.update({-(i+1):mystr.split(' ')[-(i+1)]})

# print(mydict)


# 7. Write a program to convert a list of dictionaries into a single dictionary (merge).
# mylist = [{"Ramesh":40},{"Rajesh":70},{"Raj":10}]
# finaldict = {}

# for i in mylist:
#     finaldict.update(i)

# print(finaldict)



# 8. Write a program to count the frequency of words in a sentence using a dictionary.
# mystr = "Hello Everyone Welcome to JS Everyone to Welcome to JS JS"
# mydict = {}
# for i in mystr.split(' '):
#     mydict.update({i:mystr.count(i)})

# print(mydict)

# 10. Write a program to convert a dictionary into JSON string and back.

import json  as js

ok = js 



students = {
    "Rahul" : 67,
    "Ramesh" : 67,
    "Raj" : 90
}

print(ok.JSONDecoder())
