# Function : It's Block of Code which is Perform spesific Task.

# Lambda Function : Anonymous Function  : single line Function

# Declaration :
# newVariable = lambda variablesname : single Line code  

# Use : 
# newVariable()





# a = 12 
# output = lambda a : print(a)
# output(a)


# List with Lambda : 
# mysList = [2,3,6,11,45,8,23,112,45,1,25]
# print(mysList)
# find min value
'''without Lambda : '''
# minvalue = mysList[0]
# for  i in mysList:
#     if(minvalue>i):
#         minvalue = i 
# print(minvalue)
# print(min(mysList))


# find max value 
'''without Lambda : '''
# maxvalue = mysList[0]
# for  i in mysList:
#     if(maxvalue<i):
#         maxvalue = i 
# print(maxvalue)
# print(max(mysList))


# find sum of all value 
# print(sum(mysList))

# sorting asc and desc 
# print(sorted(mysList))


# mylist = ["zas","Zafar","ra","Rajesh","Hard"]

# print(mylist)
# print(sorted(mylist))


# print(sorted(mylist,key= lambda x : len(x)))



# square of all value


# mylist = [1,2,3,4,5,6]

# print(list(map(lambda x : x,mylist)))
# print(list(map(lambda x : x*x,mylist)))



# mysList = [2,3,6,11,45,8,23,112,45,1,25]

# print(list(filter(lambda x : x>40,mysList)))

# print(list(map(lambda x : x>40,mysList)))

'''

1. **Use `filter()` and `lambda` to extract all even numbers from a list.**
   `nums = [10, 15, 21, 30, 42, 55]`

2. **Use `map()` and `lambda` to square each number in a list.**
   `nums = [1, 2, 3, 4, 5]`

3. **Use `len()` to find the total number of words in a list of strings.**
   `words = ["apple", "banana", "grape", "kiwi", "orange"]`

4. **Use `sorted()` to sort a list of tuples based on the second value.**
   `pairs = [(1, 3), (4, 1), (2, 2), (5, 0)]`

5. **Use `min()` to find the smallest element in a list of integers.**
   `numbers = [45, 22, 89, 17, 30]`

6. **Use `max()` to find the longest string in a list of strings.**
   `names = ["Alice", "Jonathan", "Bob", "Christine"]`

7. **Use `map()` and `lambda` to convert a list of strings to uppercase.**
   `colors = ["red", "green", "blue", "yellow"]`

8. **Use `filter()` and `lambda` to get all strings from a list with length > 5.**
   `cities = ["Delhi", "London", "Sydney", "NYC", "Tokyo", "Amsterdam"]`

9. **Use `sorted()` and `lambda` to sort a list of dictionaries by a specific key.**
   `students = [{"name": "Zara", "score": 85}, {"name": "Liam", "score": 92}, {"name": "Mia", "score": 78}]`

10. **Use `map()` and `lambda` to extract the first character of each word in a list.**
    `words = ["apple", "banana", "cherry", "date"]`

11. **Use `filter()` and `lambda` to get all numbers greater than the average of the list.**
    `marks = [60, 75, 80, 55, 90, 70]`

12. **Use `sorted()` with `reverse=True` to sort a list of numbers in descending order.**
    `scores = [35, 80, 45, 99, 70]`

13. **Use `min()` with `key=lambda` to find the dictionary with the smallest "age" value.**
    `people = [{"name": "A", "age": 30}, {"name": "B", "age": 25}, {"name": "C", "age": 35}]`

14. **Use `max()` with `key=lambda` to find the word with the most vowels in a list.**
    `words = ["apple", "education", "sky", "umbrella", "dog"]`

15. **Use `map()` and `lambda` to add 10 to each element in a list of integers.**
    `numbers = [5, 10, 15, 20, 25]`


'''