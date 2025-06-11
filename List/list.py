# String :   '_', "_",'''_''',"""_"""
# Tuple :    ()
# Set :  {_,_} can't empty  /  if you want empty set  : set()


# List : Collection of Multiple Data
# Syntax : []
# ordered 
# index

# mylist = []
# print(mylist)
# print(type(mylist))


# mylist = [11,12,14,67,3,2,1]
# print(mylist)
# print(mylist[0])

# mylist = [11,12,14,67,3,2,1]
# index :   0  1  2  3  4 5 6
#          -7  -6 -5 -4-3-2-1

# print(mylist)
# print(mylist[-1])


# print(mylist)
# print(mylist[0:3])
# print(mylist[0:5:2])

# print(len(mylist))
# print(mylist[len(mylist)-1])


# for i in mylist:
#     print(i)


# for i in range(0,len(mylist)):
#     print(i,mylist[i])



# mylist = [11,12,1,14,1,67,3,2,1]
# print(mylist)
# mylist.append
# mylist.append(100)
# mylist.append(100,200)
# print(mylist)

# mylist.extend
# mylist.extend({100})
# print(mylist)

# mylist.clear
# mylist.clear()
# print(mylist)


# mylist.pop
# mylist.pop(10)
# print(mylist)

# mylist.copy
# newlist = mylist.copy()
# print(newlist)

# mylist.count
# print(mylist.count(300))


# mylist.index
# print(mylist.index(14))
# print(mylist.index(1))
# print(mylist.index(1,3))
# print(mylist.index(1,3,4))



# mylist.insert : 
# mylist.insert(3,300)
# print(mylist)

# mylist.insert(-3,300)
# print(mylist)

# mylist.remove
# mylist.remove(13)
# print(mylist)

# mylist.reverse
# mylist.reverse()
# print(mylist)

# mylist.sort
# mylist.sort()
# print(mylist)   # asc 

# mylist.sort(reverse=True)
# print(mylist)   #desc



# print(sorted(mylist))


"""
6.
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

7.
Write a Python program to remove duplicates from a list.
"""
# mylist =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(mylist)

# for i in range(0,len(mylist)):
#     for j in range(0,len(mylist)):
#         if(mylist[i][1]<mylist[j][1]):
#             temp = mylist[i]
#             mylist[i]=mylist[j]
#             mylist[j] = temp
        
# print(mylist)

# mylist =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# print(sorted(mylist,key=lambda x : x[1]))


# mylist = [11,12,1,14,1,67,3,2,1]
# print(mylist)

# mylist = list(set(mylist))
# print(mylist)