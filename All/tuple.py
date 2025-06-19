'''
#### 🔗 Tuple

21. Unpack a tuple of 3 values into 3 variables and swap the first and last.
22. Write a program to multiply all elements of a numeric tuple.
23. Create a tuple of 5 strings and sort them alphabetically.
24. Access a nested value in a tuple: `t = (1, 2, (3, 4, (5, 6)))`.
25. Convert a tuple of strings into a single string with commas.

'''
v1 = 11
v2 = 12
v3 = 13

mytuple = (v1,v2,v3)
print(mytuple)

mylist = list(mytuple)
temp = mylist[0]
mylist[0] = mylist[-1]
mylist[-1] = temp 

mytuple = tuple(mylist)
print(mytuple)