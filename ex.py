# # v1=12,v2=13,v3=14      3invalid
# v1,v2,v3 = 12,"Zafar",14 #valid
# print(v1)
# print(v2)
# print(v3)


# v1,v2,*v3 = 12,"Zafar",14,15
# print(v1)
# print(v2)
# print(v3)


# *v1,v2,v3 = 12,"Zafar",14,15
# print(v1)
# print(v2)
# print(v3)

# v1,*v2,v3 = 12,"Zafar",14,15
# print(v1)
# print(v2)
# print(v3)



# def myfu(**mydict):
#     print(mydict)

# # myfu(name='Alice', age=25, city='Delhi')
# myfu(v=12,v2=13)