'''
#### 🔤 String

1. Write a Python program to find the most frequent word in a paragraph.
2. Replace all digits in a string with `*` without using regex.
3. Count the number of capital letters in a string using `isupper()`.
4. Extract only the domain name from an email address string.

'''

# mystr = "listen silent enlist inlets stone tones notes stone"


# mylist = mystr.replace('.','').replace(',','').split(' ')
# mostfreqWord = mystr[0]
# mostfreqtime = 1

# for i in mylist:
#     count = 0
#     for j in mylist:
#         if i==j:
#             count+=1
#     if(count>=mostfreqtime):
#         mostfreqtime = count
#         mostfreqWord = i 

# print(mostfreqWord,mostfreqtime)


mystr = 'roy234al129'
newstr = ""
for i in mystr:
    if(ord(i)>=48 and ord(i)<=57):
        newstr+="*"
    else:
        newstr+=i 

print(newstr)