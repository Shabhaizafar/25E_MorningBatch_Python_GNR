"""
1.Class & Object Basics

1. Create a class `Car` with attributes `brand`, `model`, and `year`. Create two objects and print their details.

"""
# 2. Create a class `Book` with attributes `title`, `author`, and `price`. Write a method to display book details.

#empty Class 
# class Book:
#     pass

# class Book:
#     # Constructor
#     def __init__(self,title,author,price):
#         self.bookname = title
#         self.authorname = author
#         self.bookprice = price

#     # Method 
#     def displayData(self):
#         print(f"Book Name : {self.bookname}\nAuthorname : {self.authorname}\nPrice : {self.bookprice}")

    
# book1 = Book("Herry Potter","Hendri ",2000)
# book2 = Book("Tom and Jerry","San ",199)

# book1.displayData()
# book2.displayData()


"""

2.Constructor & Methods

4. Create a class `Rectangle` with `length` and `width`. Add methods to calculate `area` and `perimeter`.

"""
# 3. Create a class `Student` with attributes `name`, `roll_no`, and `marks`. Use a constructor to initialize values. Add a method to calculate grade.

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
    
#     def givesGrade(self):
#         if self.marks>=90 and self.marks<=100:
#             print("Grade A")
#         elif self.marks>=80 and self.marks<90:
#             print("Grade B")
#         elif self.marks>=70 and self.marks<80:
#             print("Grade C")
#         elif self.marks>=50 and self.marks<70:
#             print("Grade D")
#         elif self.marks>=35 and self.marks<50:
#             print("Grade E")
#         elif self.marks<35:
#             print("Grade F")
#         else:
#             print('Enter Valid Marks !!!')


# s1 = Student("Raj",101,87)
# s1.givesGrade()

# s2 = Student("Ajay",111,56)
# s2.givesGrade()


# s3 = Student("Sahil",112,20)
# s3.givesGrade()

# s4 = Student("Rajesh",105,200)
# s4.givesGrade()


"""

3.Encapsulation

6. Create a class `Person` with private attributes `__name` and `__age`. Provide getter and setter methods.

"""
# 5. Create a class `BankAccount` with a private attribute `__balance`. Add methods `deposit()`, `withdraw()`, and `get_balance()`. Ensure balance cannot be negative.

# class BankAccount: 
#     def __init__(self):
#         self.__balance = 10000

#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Deposit Successfully !!")

#     def withdraw(self,amount):
#         if(self.__balance>0 and self.__balance>=amount):
#             self.__balance-=amount
#             print(f"{amount} withdrawal Successfully !!")
#         else:
#             print("Withdrawal Failed !!")

#     def get_balance(self):
#         print(f"Your Balance : {self.__balance}")


# p1 = BankAccount()
# p1.get_balance()
# p1.deposit(3000)
# p1.get_balance()
# p1.withdraw(9000)
# p1.get_balance()
# p1.withdraw(3999)
# p1.get_balance()



"""

4.Inheritance

7. Create a base class `Employee` with attributes `name` and `salary`. Create a derived class `Manager` that adds `department`. Print details of both.
8. Create a class `Animal` with a method `sound()`. Derive `Dog` and `Cat` classes that override the sound method.

"""

"""

5.Polymorphism

9. Create two classes `Circle` and `Square` each having a method `area()`. Demonstrate polymorphism by calling `area()` on different objects.
10. Create classes `CreditCardPayment` and `UPIPayment` with a method `pay(amount)`. Show polymorphism by using the same method for different payment types.

"""

"""

6.Abstraction

11. Create an abstract class `Shape` with abstract methods `area()` and `perimeter()`. Implement `Rectangle` and `Circle` subclasses.
12. Create an abstract class `Vehicle` with an abstract method `start_engine()`. Implement `Car` and `Bike`.

"""

"""

7.Class & Static Methods

13. Create a class `Employee` with a class variable `company_name`. Use a class method to change the company name for all employees.
14. Create a class `MathUtils` with a static method `is_prime(n)` that checks if a number is prime.

"""

"""

8.Operator Overloading

15. Create a class `ComplexNumber` and overload the `+` operator to add two complex numbers.
16. Create a class `Vector` and overload the `*` operator for dot product.

"""

"""

9.Real-Life Case Studies

17. Create a class `ShoppingCart` where you can add items (name, price, qty) and calculate total bill.
18. Create a class `Library` with methods to `add_book`, `remove_book`, and `display_books`.
19. Create a class `ATM` that simulates ATM transactions like deposit, withdraw, and balance check.
20. Create a class `OnlineCourse` with attributes `title`, `instructor`, and `price`. Add a method to apply a discount.

"""