"""

## 🟢 **Easy Level (Basics of Tuple)**

> Focus: Tuple creation, indexing, basic operations

4. **Check** if an element exists in a tuple.
5. Find the **length of a tuple**.
6. **Count how many times** an element appears in a tuple.

8. Create a tuple with **mixed data types** (e.g., string, int, float, boolean).
9. **Concatenate two tuples** and print the result.

"""
# 1. **Create a tuple** of your 5 favorite fruits and print each one using a loop.
# for i in ("Good Apple","Small Apple","Big Apple","Kashmiri Apple","Bad Apple"):
#     print(i)


# 2. **Access the third element** in a given tuple.
# mytuple = ("Good Apple","Small Apple","Big Apple","Kashmiri Apple","Bad Apple")
# print(mytuple[2])

# 3. Write a Python program to **convert a list to a tuple**.
# mylist =["Good Apple","Small Apple","Big Apple","Kashmiri Apple","Bad Apple"]
# print(tuple(mylist))
# 7. **Get the index** of a specific value in a tuple.
# mytuple = ("Good Apple","Small Apple","Big Apple","Kashmiri Apple","Bad Apple")
# print(mytuple.index("Small Apple"))
# 10. **Convert a tuple to a string** (e.g., `('a','b','c')` → `'abc'`).
# mytuple = ('a','b','c')
# print("".join(mytuple))
# print(" ".join(mytuple))
# print(" || ".join(mytuple))





"""

## 🟡 **Intermediate Level (Tuple unpacking, nested tuple, logic)**

> Focus: Unpacking, nested tuples, immutability concepts

5. Create a program to **sort a tuple of numbers** in ascending order.
6. Write a program to **reverse a tuple**.

8. Create a nested tuple (e.g., students with (name, (math, science))) and **access subject marks**.
9. Given a tuple of numbers, **find the sum and average**.
10. Convert a tuple to a list, **modify it**, then convert it back to tuple.

"""
# 1. Unpack a tuple into **three separate variables**.
# mytuple = (11,12,13)

# n1,n2,n3 = mytuple
# print(n1)
# print(n2)
# print(n3)


# 2. **Swap two variables** using tuple unpacking.
# mytuple = (11,12)
# n1,n2 = mytuple
# mytuple = (n2,n1)
# print(mytuple)

# 3. **Loop through a list of tuples** (e.g., students with marks) and print in a readable format.

# mylist = [("Ajay",89,80),("Vijay",90,100)]
# for i in mylist:
#     n1,n2,n3 = i 
#     print("Student Name : {0} and Their Marks : {1},{2}".format(n1,n2,n3))

# 4. **Check if all elements** in a tuple are the same.
# mytuple = (11,11,11)
# print("All Same" if mytuple.count(mytuple[0]) == len(mytuple) else "Not Same")

# 7. Create a tuple from user input and **slice the last three elements**.
# mylist = []

# while True :
#     n = input("Enter Value or Exit :")
#     if(n == "Exit" or n == "exit"):
#         break
#     try : 
#         mylist.append(int(n))
#     except : 
#         print("Exit")
       
# print(tuple(mylist))
"""

## 🔴 **Advanced Level (Real-world logic with tuples)**

> Focus: Tuple usage in real scenarios, sorting, grouping, data extraction

1. Given a list of tuples representing (name, age), **sort by age**.
2. From a tuple of words, **create a tuple of word lengths**.
4. Accept student records as a list of tuples `(name, score)` and **find topper(s)**.
8. Accept details of products `(id, name, price)` as tuples and **filter those with price > 1000**.
9. Use a tuple of months and temperatures to **find the month with highest temperature**.


"""
# 3. Given a tuple of file names, **filter only `.txt` files**.
# mytuple = ("first.txt","data.json","last.css","app.py","second.c","all.txt")
# print(tuple(filter(lambda x : x.split('.')[1]=="txt",mytuple)))

# 5. Given a tuple of coordinates, **calculate Euclidean distance** between first and last point.
# import math
# mytuple  = ((30,40),(50,70),(60,90))

# print(math.sqrt(math.pow(mytuple[-1][0]-mytuple[0][0],2)+math.pow(mytuple[-1][1]-mytuple[0][1],2)))
# print(mytuple[0],mytuple[-1])



# 6. Given a tuple of tuples (e.g., `(‘A’, 80)`, `(‘B’, 60)`), **find grade with highest score**.

# mytuple = (("C",50),("A",80),("B",70))
# print(max(mytuple,key= lambda x : x[1]))

# 7. Write a function that accepts any tuple and **returns the tuple in reversed order** if it's numeric, else raise an error.

# def reversedata(mytuple):
#     if(type(mytuple[0])==type(1)):
#         print(tuple(list(reversed(list(mytuple)))))
#     else:
#         print(TypeError)

# reversedata(("R","A","J"))
# reversedata((11,12,13))

# 10. Create a **menu system using tuple** where each item is a tuple of (item_name, price), and allow user to calculate total bill.


# allitems = []
# while(1):
#     print("1. For Add a New Item.")
#     print("2. For calculate total bill.")
#     print("3. For exit.")
#     choice = int(input("Enter your Choice : "))
#     match(choice):
#         case 1 : 
#                 mytuple = (input("Enter Product Name : "),int(input("Enter Price :")))
#                 allitems.append(mytuple)

#         case 2 :  
#               totalbill = 0
#               for i in allitems:
#                     totalbill+=i[1]
#               print("Total Bill :",totalbill)
#               break
#         case 3 : break
