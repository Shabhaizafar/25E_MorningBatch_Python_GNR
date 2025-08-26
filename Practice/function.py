"""

## **Easy (10 Questions)**

1. Write a function that prints "Hello, World!".
3. Write a function that takes two numbers and returns their sum.
7. Write a function that prints all numbers from 1 to 10.
9. Write a function that returns `True` if a number is even, otherwise `False`.
10. Write a function that converts Celsius to Fahrenheit.

"""
# 2. Write a function that takes a name as input and prints "Hello, \[name]!".
# def sayHello(fname):
    # print(f"Hello, {fname}!")

# sayHello("Rajesh")
# sayHello("Raj")

# 4. Write a function that takes a number and returns its square.

# def printsquare(n):
    # return n*n 
    # return pow(n,2)

# print(printsquare(4))


# 5. Write a function that takes a string and prints its length.
# def lenstr(mystr):
#     print(len(mystr))

# lenstr("Rajesh")


# 6. Write a function that takes two numbers and returns the larger one.
# def largerNumber(n1,n2):
#     if(n1>n2):
#         return n1
#     return n2 
# print(largerNumber(14,13))

# 8. Write a function that takes a list and prints each element.
# def printData(mylist):
#     for i in mylist:
#         print(i)

# printData([45,63,86,13])


"""


## **Intermediate (10 Questions)**

1. Write a function that takes a list of numbers and returns the sum of all numbers.
3. Write a function that returns the reverse of a string.
4. Write a function that counts the number of vowels in a string.
9. Write a function that accepts any number of arguments and returns their average.
10. Write a function that finds the second largest number in a list.

"""
# 2. Write a function that finds the factorial of a given number.
def findFact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i 

    print(fact)

# findFact(5)


# 5. Write a function that checks whether a number is prime.

def checkPrime(n):
    counter = 0
    for i in range(1,n):
        if(n % i == 0):
            counter+=1
    if(counter==1):
        return True
    return False

# print(checkPrime(29))

# 6. Write a function that takes a list and returns a new list with unique elements only.

def uniqueListCoverter(mylist):
    return list(set(mylist))

# print(uniqueListCoverter([1,2,3,4,5,64,3,2,1]))

# 7. Write a function that returns the Fibonacci sequence up to `n` terms.

# def Fibonaccii(n):
#     a = 0
#     b = 1
#     c = 0 
#     counter = 0
#     while(1):
#         if(counter==n):
#             break
#         print(a)
#         c = a+b 
#         a = b
#         b = c 
#         counter+=1

# Fibonaccii(10)



# 8. Write a function that merges two dictionaries.
def mergeDict(d1,d2):
    for i in d2:
        d1.update({i : d2[i]})
    print(d1)
# mergeDict({"Nam" : "Raj"},{"Age": 12})


"""

## **Advanced (10 Questions)**

1. Write a recursive function to calculate the sum of digits of a number.
2. Write a function that implements a simple calculator using function dispatching.
3. Write a function that finds all permutations of a string.
4. Write a decorator function that prints "Function started" before executing and "Function ended" after executing a function.
5. Write a function that accepts a list of numbers and returns a dictionary with count of even and odd numbers.

"""
# 6. Write a function that finds all prime numbers in a given range.
# def checkPrime(n1,n2):
#     for k in range(n1,n2+1):
#         counter = 0
#         for i in range(1,k):
#             if(k % i == 0):
#                 counter+=1
#         if(counter==1):
#             print(k)

# checkPrime(20,100)
# 7. Write a function that takes another function as a parameter and applies it to a list of numbers.
# def outerfu(mylist):
#     for i in mylist:
#         print(i)

# def main(myfu):
#     myfu([11,12,13,14])

# main(outerfu)


# 8. Write a function that implements the Tower of Hanoi problem.
# 9. Write a function that calculates the GCD of two numbers using recursion.

# 24  : 2,2,2,3
# 20  : 2,2,5

# def findGCD(a,b):                     # a = 50 , b = 20
#     if(b == 0):            #20!=0                   # 4!=0
#         print(a)
#         return
#     remainder = a % b     # r = 50 % 20  = 10       # r = 20 % 10  b = 0 
#     a = b                 #  a=20                  # a = 4 
#     b = remainder         #  b = 10                 # b = 0
#     findGCD(a,b)
    

# findGCD(50,20) 


# 10. Write a function that returns all palindromic substrings in a given string.

# mystr = "nadamad"

# def myFu(mystr):
#     for i in range(0,len(mystr)):
#         for j in range(i,len(mystr)):
#             if(len(mystr[i:j+1])>1):
#                 if(mystr[i:j+1] == "".join(list(reversed(mystr[i:j+1])))):
#                     print(mystr[i:j+1])

# myFu(mystr)    











