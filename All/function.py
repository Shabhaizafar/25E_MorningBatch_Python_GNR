'''

#### 🛠️ Function

31. Define a function to return the largest of three numbers.
32. Write a function that accepts a list and returns a new list with only positive numbers.
33. Create a function that takes a number and returns a dictionary of its multiplication table (1 to 10).
34. Write a recursive function to compute the power of a number (x^y).
35. Create a function that checks if all elements in a list are unique.

'''

# 34. Write a recursive function to compute the power of a number (x^y).
'''
base = 2
power = 5


def find_power(b,p):
    if(p==1):
        return b 
    b *=base   # 5*5  = 25  * 5 = 125 
    return find_power(b,p-1) #  25 ,2   125,1

print(find_power(base,power))
'''

# 35. Create a function that checks if all elements in a list are unique.

'''
mylist = [11,1,2,3,4,11,5]

def checklist(l):
    if(len(l)==len(set(l))):
        print("All Unique")
    else:
        print("Not Unique")

checklist(mylist)
'''