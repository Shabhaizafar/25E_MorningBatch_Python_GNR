'''

#### 🧺 Set

16. Write a program to find missing elements from one list compared to another using sets.
17. Remove duplicates from a list without using `set()` directly in the final result.
18. Create a set from user input and check if any element is a number.
19. Use set operations to identify students who play both cricket and football.
20. Check if two sets have any elements in common (intersection check).

'''

# mylist =  [11,12,13,14,15,16,12,13,14]
# myset = {''}

# for i in mylist:
#     myset.add(i)
# else:
#     myset.remove('')
# print(myset)

n = int(input("Number of Element"))
myset = set()
counter = 0
for i in range (0,n): 
    v = input("Value :")
    if(ord(v[0])>=47 and ord(v[0])<=57):
        myset.add(int(v))
        counter = 1
    else:
        myset.add(v)

if(counter):
    print("Number Exist")
else:
    print("Number Doesn't Exist")