'''

## 🟢 **Easy Level (Basics of List)**

> Focus: Creation, indexing, simple operations

1. **Create a list** of 5 favorite colors and print each color using a loop.
2. **Find the sum** of all elements in a list of numbers.
4. **Count** how many times the number `7` appears in a list.
7. **Print only even numbers** from a list of integers.
8. **Find the maximum and minimum** values in a list.
'''
# 3. **Reverse** a list without using built-in reverse method.
"""
# Method : 1
mylist = [11,12,13,14]
mylist2 = []
for i in range(len(mylist)-1,-1,-1):
    mylist2.append(mylist[i])
print(mylist2)

# Method : 2
mylist = [11,12,13,14]
print(list(reversed(mylist)))

# Method : 3 
mylist = [11,12,13,14]
mylist.reverse()
print(mylist)

"""


# 5. **Check** if a given element exists in a list or not.
"""
mylist = [11,12,13,14]
print(15 in mylist)
"""
# 6. **Append** a user-input value to an existing list.
"""
mylist = [11,12,13,14]
value = int(input("Enter Value : "))
mylist.append(value)
print(mylist)
"""
# 9. **Create a new list** that contains square of each element from another list.
"""
mylist = [11,12,13,14]
print(list(map(lambda x : x*x,mylist)))
"""

# 10. **Join two lists** and print the result.
"""
mylist = [11,12,13,14]
mylist2 = [1,2,3,4]
mylist.extend(mylist2)
print(mylist)
"""
'''

## 🟡 **Intermediate Level (List Methods, Nested Lists, Logic)**

> Focus: List methods, slicing, comprehensions, multiple lists

1. **Remove all duplicates** from a list.
2. Write a program to **insert an element at a specific index** in a list.
4. Given a list of student marks, **find the average** and all marks **above average**.
9. Accept 5 names from user and **sort them alphabetically**.
10. Find the **second largest** number in a list.

'''
# 3. **Rotate a list to the right** by `k` positions.
"""
mylist = [11,12,13,14]
k=1
final = mylist[k:]
final.extend(mylist[:k])
print(final)
"""
# 5. **Flatten a nested list** (e.g., `[[1, 2], [3, 4]]` → `[1, 2, 3, 4]`)

"""
mylist = [[1, 2], [3, 4]]
flattern = []
for i in mylist:
    if(type(i) == type([])):
        for j in i:
            flattern.append(j)
    else:
        flattern.append(i)

print(flattern)
"""
# 6. **Sort a list** of tuples based on the second value.
#    *(e.g., `[(‘a’, 3), (‘b’, 1), (‘c’, 2)]` → `[(‘b’, 1), (‘c’, 2), (‘a’, 3)]`)*
# 7. **Create a list of all prime numbers** between 1 and 50.
# 8. From a list of words, **create a list of words with length > 5**.
'''

## 🔴 **Advanced Level (Real-world-like, List Comprehensions, Complex Logic)**

> Focus: Deep logic, nested structures, higher-order operations

1. **Group words by their length** from a given list.
   *(e.g., `["cat", "dog", "apple", "bat"]` → `{3: ['cat', 'dog', 'bat'], 5: ['apple']}`)*
2. Given a list of strings, **filter all palindromes**.
3. **Implement a shopping cart** using a list where you can add, remove, view items.
4. Given a matrix (nested list), **transpose the matrix**.
5. Accept a sentence from user and **return list of unique words**.
6. **Split a list into chunks** of size `n`. (e.g., `[1,2,3,4,5,6], n=2` → `[[1,2],[3,4],[5,6]]`)
7. **Create a frequency dictionary** from a list.
   *(e.g., `[‘a’, ‘b’, ‘a’, ‘c’, ‘b’]` → `{'a': 2, 'b': 2, 'c': 1}`)*
8. Create a list of student dictionaries and **sort them by marks**.
9. Given a list of transactions with positive and negative integers, **separate credits and debits**.
10. Create a program that accepts multiple sentences and **returns the top 5 most common words** using lists and logic.
'''