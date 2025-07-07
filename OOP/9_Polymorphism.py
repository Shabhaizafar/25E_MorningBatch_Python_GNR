# 1 Dynamic Polymorphism :

# class Cat:
#     def speak(self):
#         print("Meow !!!")

# class Dog:
#     def speak(self):
#         print("Wolf !!!")


# cat1 = Cat()
# dog1 = Dog()


# def Animal(xyz):
#     xyz.speak()

# Animal(cat1)
# Animal(dog1)



# class Bird:
#     def fly(self):
#         print("Bird is Flying")


# class Aeroplane:
#     def fly(self):
#         print("Aeroplane is Flying")


# b1 = Bird()
# p1 = Aeroplane()

# def method_start(flyer):
#     flyer.fly()


# method_start(b1)
# method_start(p1)


# 2 Function Polymorphism :

# print(len([1,3,4,5,6,2,1,7]))

# print(len("Royal"))



# -------------------------------------------------------------------
# Polymorphism with inheritance :  

# class Animal :
#     def speak(self):
#         print("Something speak")

# class Cat(Animal):
#     def speak(self):
#         print("Meow !!!")

# class Dog(Animal):
#     def speak(self):
#         print("Wolf !!!")


# c1 = Cat()
# d1 = Dog()
# a1 = Animal()

# # c1.speak()
# # d1.speak()
# # a1.speak()

# animals = [Cat(),Dog(),Animal()]


# for a in animals:
#     a.speak()



'''

### 🔹 Question 1:

You are designing a drawing application. Create a polymorphic setup where different shapes (`Circle`, `Rectangle`, `Triangle`) all implement a method called `draw()`. How would you design this so that a function can call `draw()` on any shape without knowing its type?

---

### 🔹 Question 2:

You’re building a notification system that sends alerts through different channels like `Email`, `SMS`, and `PushNotification`. All notification classes have a method `send(message)`. How can you use polymorphism to write a function that sends the message regardless of the notification type?

'''

