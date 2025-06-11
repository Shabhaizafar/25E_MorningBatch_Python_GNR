# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# mylist = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# mylist.pop(4)
# mylist.pop(3)
# mylist.pop(0)

# print(mylist)


# Write a Python program to generate a 3*4*6 3D array whose each element is *.

# [
#    [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]  ,
#    [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]] ,
#    [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
# ]

# mylist = []

# v1 = 3
# v2 = 4 
# v3 = 6 

# for i in range(0,v1):
#     mylist.append([])
#     for j in range(0,v2):
#         mylist[i].append([])
#         for k in range(0,v3):
#             mylist[i][j].append(k)


# for i in mylist:
#     print(i)









# ---------------------------
# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

# mylist = [1, 5, 3]
# flag = False
# for j in mylist : 
#     if(j<=2):
#         flag = True
#         break
#     v1 = j
#     for i in range(2,v1):
#         if v1%i==0:
#             flag = True
#             break
#     if(flag):
#         break

# print(not flag)


'''
21. Convert List to String

Write a Python program to convert a list of characters into a string.
Click me to see the sample solution

22. Find Index of List Item

Write a Python program to find the index of an item in a specified list.

24. Append One List to Another

Write a Python program to append a list to the second list.

27. Find Second Smallest Number in List

Write a Python program to find the second smallest number in a list.
Click me to see the sample solution

28. Find Second Largest Number in List

Write a Python program to find the second largest number in a list.
Click me to see the sample solution

29. Get Unique Values from List

Write a Python program to get unique values from a list.
Click me to see the sample solution

30. Count Frequency of List Elements

Write a Python program to get the frequency of elements in a list.

31. Count Elements in List Within Range

Write a Python program to count the number of elements in a list within a specified range.

35. Create List with Range Concatenation

Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

37. Find Common Items in Lists

Write a Python program to find common items in two lists.
'''