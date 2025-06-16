'''
#### 🔢 Number

6. Write a Python function to check whether a number is an Armstrong number.
7. Create a program that simulates a simple calculator using user input and functions.
8. Generate a list of prime numbers between 1 and 100 using a loop.
9. Convert temperature from Celsius to Fahrenheit using a function.
10. Write a program to calculate the compound interest for a given principal.

'''

# 6. Write a Python function to check whether a number is an Armstrong number.
'''
mynumber = 153
add = 0

def myfu(mynumber,add):
    if(len(str(mynumber))<3):
        print('Not Armstrong')
        return 
    for i in str(mynumber) :
        add+=pow(int(i),len(str(mynumber)))
    if(mynumber == add):
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
      
myfu(mynumber,add)
'''

# 8. Generate a list of prime numbers between 1 and 100 using a loop.
mylist = []
for i in range(1,101):
    count = 0
    if i<=2:
        continue
    for j in range(2,i+1):
        if(i%j==0):
            count+=1
    if(count==1):
        mylist.append(i)

    
print(mylist)
