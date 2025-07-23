
# Create decorator
# def myDecorator(func):
#     def connector(*args,**kwargs):
#         print("Before Function Execution :")
#         output = func(*args,**kwargs)
#         print("After Function Execution :")
#         return output
#     return connector


# # use Decorator
# @myDecorator
# def greet(name):
#     print(f"Hello,{name} !!")

# greet("Raj")



# def myd(fun):
#     def wrapper(*arg,**kwargs):
#         print(f"Arguments : {arg} , {kwargs}")
#         return fun(*arg,**kwargs)
#     return wrapper

# @myd
# def add(a,b):
#     print(a+b)

# add(12,13)