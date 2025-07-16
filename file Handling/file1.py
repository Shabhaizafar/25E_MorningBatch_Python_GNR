# File handling in Python allows you to create, read, write, and delete files. It’s a fundamental concept when working with data storage, logs, or user-generated content.


# Read File : 

# file1 = open("C://Users/shabh/Documents/ROYAL/25E_MorningBatch_Python_GNR/file Handling/intro1.txt",'r')
# print("Opened !!!")
# file1.close()


# file1 = open("C://Users/shabh/Documents/ROYAL/25E_MorningBatch_Python_GNR/file Handling/intro.txt",'r')

# print(file1.read())

# for i in file1.read():
#     print(i)


# print(file1.readline())
# print(file1.readline())
# print(file1.readline(1))


# print(file1.readlines(1))

# file1.close()



# file1 = open("C://Users/shabh/Documents/ROYAL/25E_MorningBatch_Python_GNR/file Handling/intro1.txt",'w')
# # file1.write("Hello Everyone !!")
# file1.write("Welcome !!")

# print("Data Added  Created !!!")

# file1.close()



# file1 = open("C://Users/shabh/Documents/ROYAL/25E_MorningBatch_Python_GNR/file Handling/intro.txt",'a')
# file1.write("\nRoyal !!")
# file1.close()



# with open("C://Users/shabh/Documents/ROYAL/25E_MorningBatch_Python_GNR/file Handling/intro.txt",'r') as file2:
#     data = file2.read()
#     print(data)


import os

# Check if file exists
if os.path.exists("C://Users/shabh/Documents/ROYAL/25E_MorningBatch_Python_GNR/file Handling/intro1.txt"):
    os.remove("C://Users/shabh/Documents/ROYAL/25E_MorningBatch_Python_GNR/file Handling/intro1.txt")  # Delete file
else:
    print("File does not exist")



# https://www.w3resource.com/python-exercises/file/index.php  
