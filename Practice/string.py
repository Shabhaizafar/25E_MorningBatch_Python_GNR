'''
### ✅ **Level 1: Easy**

> Focus: Basic operations, indexing, slicing, and built-in functions

4. **Extract first and last characters of a string**
   Input: `"Programming"` → Output: `"Pg"`

5. **Check whether a substring is present**
   Input: `"Python is fun"`, Substring: `"fun"` → Output: `True`

6. **Convert string to uppercase and lowercase**
   Input: `"Python"` → Output: `"PYTHON"`, `"python"`

7. **Find length without using `len()` function**
   Input: `"Python"` → Output: `6`

10. **Print every 2nd character of the string**
    Input: `"education"` → Output: `"euao"`

'''
# 1. **Reverse a string**
#    Input: `"hello"` → Output: `"olleh"`
"""
# M : 1
mystr1 = "Hello Everyone !!!"
for i in range(len(mystr1)-1,-1,-1):
    print(mystr1[i],end="")
"""
# M : 2
"""
mystr1 = "Hello Everyone !!!"
myl = list(reversed(mystr1))
print("".join(myl))
"""
# 2. **Check if a string is a palindrome**
#    Input: `"madam"` → Output: `True`
"""
mystr2 = "Royal"
myl = list(reversed(mystr2))
if (mystr2 == "".join(myl)):
    print(True)
else :
    print(False)
"""
# 3. **Count vowels and consonants in a string**
#    Input: `"Python"` → Output: `Vowels: 1, Consonants: 5`
"""
mystr3 = "Royal T"
countvowels = 0
countconsonants = 0
vowels = ["A",'a',"E","e","I","i","O","o","U","u"]

for i in mystr3:
    if((i>='A' and i<="Z") or (i>='a' and i<="z")):
        if(i in vowels):
            countvowels+=1
        else:
            countconsonants+=1

print(f"Vowels: {countvowels}, Consonants: {countconsonants}")
"""


# 8. **Replace all spaces with hyphens**
#    Input: `"Learn Python Well"` → Output: `"Learn-Python-Well"`
"""
mystr8= "Learn Python Well"
print(mystr8.replace(" ","-"))
"""
# 9. **Concatenate two strings manually (without `+`)**
#    Input: `"Py"`, `"thon"` → Output: `"Python"`
"""
mystr91= "Py"
mystr92= "thon"

print(mystr91+mystr92)
print("{0}{1}".format(mystr91,mystr92))

mylist = list(mystr91)
mylist.append(mystr92)
print("".join(mylist))
"""
'''

### 🔁 **Level 2: Intermediate**

> Focus: String methods, formatting, looping, and advanced indexing

11. **Remove all punctuations from a string**
    Input: `"Hello!!! Python, is amazing..."` → Output: `"Hello Python is amazing"`


13. **Count number of words in a string**
    Input: `"Python is awesome"` → Output: `3`


17. **Swap cases of all characters**
    Input: `"PyTHon"` → Output: `"pYthON"`

19. Print characters and their ASCII values
    Input: "AB" → Output: A:65, B:66


20. **Sort the characters in a string alphabetically**
    Input: `"banana"` → Output: `"aaabnn"`

'''

# 12. **Check if two strings are anagrams**
#     Input: `"listen"` and `"silent"` → Output: `True`
"""
mystr121 = "listen"
mystr122 = "silent"

if(len(mystr121)==len(mystr122)):
    l1 = list(mystr121)
    l1.sort()
    l2 = list(mystr122)
    l2.sort()
    temp = True
    for i in range (0,len(l2)):
        if(l1[i]!=l2[i]):
            print(False , "Inner")        
            temp =False
            break
    if temp:
        print(True)
else :
    print(False , "Outer")
"""

# 18. **Find the longest word in a sentence**
#     Input: `"Python is powerful and simple"` → Output: `"powerful"`
"""
mystr18 = "Python is powerful and simple"
mylist = mystr18.split(' ')
print(max(mylist,key= lambda x : len(x)))
"""

# 14. **Capitalize the first letter of each word**
#     Input: `"hello world"` → Output: `"Hello World"`
"""
mystr14 = "hello world"
print(mystr14.title())
"""
# 15. **Find the frequency of each character in a string**
#     Input: `"banana"` → Output: `{ 'b': 1, 'a': 3, 'n': 2 }`
"""
mystr15 = "banana"
mydict = {}
for i in mystr15:
    mydict.setdefault(i,mystr15.count(i))

print(mydict)
"""

# 16. **Remove duplicate characters**
#     Input: `"programming"` → Output: `"progamin"`
"""
# M : 1
mystr16 = "programming"
myset = set(mystr16)
mystr16 = "".join(myset)
print(mystr16)

# M : 2
for i in range(0,len(mystr16)):
    temp = True
    for j in range(0,i):
        if(mystr16[j] == mystr16[i]):
            temp =False
    if(temp):
        print(mystr16[i],end="")
"""

'''

### 🧠 **Level 3: Advanced**

> Focus: Custom functions, edge cases, and mini-project style logic

22. **Compress string (count repeating chars)**
    Input: `"aaabbc"` → Output: `"a3b2c1"`

23. **Check if string is valid identifier (variable name)**
    Input: `"my_var"` → Output: `True`



26. **Group all uppercase characters together**
    Input: `"HeLLoWorld"` → Output: `"HLLW"`

27. **Check if string contains only digits (without `.isdigit()`)**


30. **Implement a custom `strip()` (remove leading/trailing spaces)**

'''

# 21. **Find the first non-repeating character**
#     Input: `"aabbcdde"` → Output: `"c"`
"""
mystr="aariyanr"
for i in mystr:
    count = 0
    for j in mystr:
        if i == j :
            count+=1
    if(count==1):
        print(i)
        break
"""

# 24. **Count total digits, letters, and special characters**
#     Input: `"Python123!@"` → Output: `Letters: 6, Digits: 3, Specials: 2`
"""
mystr = "Python123!@"
Letters = 0
Digits = 0
Specials = 0

for i in mystr:
    if((i>='A' and i<="Z") or (i>='a' and i<="z")):
        Letters+=1
    elif(i>="0" and i<="9"):
        Digits+=1
    else:
        Specials+=1

print(f"Number: {Digits}, Letters: {Letters} , Specials : {Specials}")
"""
# 29. **Find all substrings of a string**
#     Input: `"abc"` → Output: `["a", "ab", "abc", "b", "bc", "c"]`
"""
mystr = "abc"

for i in range(0,len(mystr)):
    for j in range(0,len(mystr)+1):
        if(mystr[i:j]):
            print(mystr[i:j])
"""
# 25. **Custom implementation of `startswith()` and `endswith()`**

"""
mystr = input("Enter String : ")

print(f"String Start with 'Z' : {mystr.startswith("Z")}")
print(f"String End with 'r' : {mystr.endswith("r")}")
"""


# 28. **Remove all characters except alphabets and numbers**
"""
mystr = "zxcvbh@#$%^234ASD"
for i in mystr:
    if((i>='A' and i<="Z") or (i>='a' and i<="z") or (i>="0" and i<="9")):
        print(i,end="")
    
"""