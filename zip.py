# students = ["Raj","Rajesh","Rajendra"]
# marks = [67,78,90,89]

# myzip = zip(students,marks) 
# print(list(myzip))
# print(tuple(myzip))



# myzip = [('Raj', 67), ('Rajesh', 78), ('Rajendra', 90)]

# students,marks = zip(*myzip)
# print(students)
# print(marks)



students = ["Raj","Rajesh","Rajendra"]
subject = ["Guj","Sci","Math"]
marks = [67,78,90,89]

myzip = zip(students,subject,marks)

print(list(myzip))