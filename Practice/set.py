"""

### **Level 1 — Easy**

2. Convert a list `[1, 2, 2, 3, 4]` to a set and print it.
4. Add the element `10` to the set `{1, 2, 3}`.
6. Find the length of the set `{10, 20, 30, 40}`.
8. Clear all elements from the set `{1, 2, 3, 4}`.
# 10. Loop through the set `{10, 20, 30}` and print each element.

"""
# 1. Create a set with numbers from 1 to 5 and print it.
# myset = {1,2,3,4,5}
# for i in myset:
#     print(i)


# myset = {1,2,3,4,5}
# print(i for i in myset)

# 3. Check if the number `3` exists in the set `{1, 2, 3, 4}`.
# myset = {1, 2,  4}
# print(3 in myset)


# 5. Remove the element `2` from the set `{1, 2, 3}`.
# myset = {1, 2, 3}
# myset.remove(2) 
# print(myset)

# 7. Create an empty set and verify its type.
# myset = {}
# myset = set()
# print(type(myset))

# 9. Use a set to remove duplicate items from the list `[5, 5, 6, 7, 7]`.
# mylist =[5, 5, 6, 7, 7]
# convert set : 
# myset = set(mylist)
# print(myset)


"""

### **Level 2 — Intermediate**

1. Find the union of sets `{1, 2, 3}` and `{3, 4, 5}`.
3. Find the difference between `{1, 2, 3}` and `{2, 4}`.
5. Check if `{1, 2, 3}` is a superset of `{2, 3}`.
7. Remove an element from a set without causing an error if the element is missing.
9. Copy a set `{1, 2, 3}` into another variable and verify they are different objects.

"""
# 2. Find the intersection of `{1, 2, 3, 4}` and `{2, 4, 6}`.
# myset1 = {1,2,3,4}
# myset2 = {2,4,6}

# print(myset1.intersection(myset2))
# print(myset2.intersection(myset1))


# 4. Check if `{1, 2}` is a subset of `{1, 2, 3, 4}`.
# myset1 = {1,2}
# myset2 = {1,2,3,4}
# print(myset1.issubset(myset2))
# print(myset2.issubset(myset1))



# 6. Create a set from a string `"programming"` and print it.
# mystr = "programming"
# print(set(mystr))
# print(type(set(mystr)))


# 8. Find the symmetric difference between `{1, 2, 3}` and `{3, 4, 5}`.
# myset1 = {1,2,3}
# myset2 = {3,4,5}

# print(myset1.symmetric_difference(myset2))
# print(myset2.symmetric_difference(myset1))


# 10. Given `A = {1, 2, 3}` and `B = {3, 4}`, update `A` with elements of `B`.

# A = {1,2,3}
# B = {3,4}

# A.update(B)
# print(A)

"""

### **Level 3 — Advanced**

1. Write a program to find all elements that are present in exactly two out of three given sets.
2. Given a list of words, find all unique words ignoring case.
3. Find the common letters in two strings using sets.
4. Given a set of tuples `{(1, 2), (3, 4), (1, 2)}`, remove duplicates.
5. Count the number of vowels in a string using sets.

"""
# 6. Find all elements that are not common between three sets.
# myset1 = {1,2,3}
# myset2 = {1,3,4,5}
# myset3 = {1,3,6}

# myset1.update(myset2)
# myset1.symmetric_difference_update(myset3)
# print(myset1)

# 7. Given two lists, check if they have at least one element in common using sets.
# mylist1= [1,2,3]
# mylist2 = [4,5]

# print("Common Element Exist" if len(set(mylist1).intersection(set(mylist2)))>=1 else "Common element Not Exist")


# 8. Create a set comprehension to store squares of even numbers from 1 to 10.

# myset = set()
# for i in range(1,11):
#     myset.add(i*i) if i%2==0 else 2*2

# print(myset)

# 9. Write a program to check if two sets are disjoint.

# myset1 = {1,2,3,4}
# myset2 = {6}

# print(myset1.isdisjoint(myset2))

# 10. Given a dictionary, find all unique values using a set.
# mydict = {
#         "fname" : "Raj",
#         "lname" : "Shah",
#         "age"   : 12,
#         "yearsold" : 12
#     }

# print(set(mydict.values()))