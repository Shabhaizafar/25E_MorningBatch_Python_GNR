# class User:
#     # constructor
#     def __init__(self,fname,lname):
#         self.firstname = fname      # Property / Attributes
#         self.lastname = lname       # Property / Attributes

#     def bioData(self):
#         print(f"My name is {self.firstname} {self.lastname}.")


# u1 = User("Raj","Shah")

# print(u1.firstname)
# print(u1.lastname)
# u1.bioData()


# u2 = User("Rajesh","Sharma")
# print(u2.firstname)
# print(u2.lastname)
# u2.bioData()


'''

### 🧑‍🎓 **Q1. Student Portal System**

**Scenario**: You’re building a student management system.
Create a class `Student` with:

* Attributes: `name`, `roll_no`
* Method: `display_profile()` → shows the student's name and roll number
  🟢 *Use Case*: School wants to print ID cards using this info.

'''

# class Student : 
#     def __init__(self,name,roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     def display_profile(self):
#         print("Your Info:-")
#         print(f"Name : {self.name}")
#         print(f"Roll No. : {self.roll_no}")


# s1 = Student("Ajay",101)
# s1.display_profile()

# s2 = Student("Ramesh",102)
# s2.display_profile()


'''

### 🚗 **Q3. Car Dealer Inventory System**

**Scenario**: A car dealer wants to manage its car inventory.
Create a class `Car` with:

* Attributes: `brand`, `model`, `year`
* Method: `car_info()` → shows car details
  🟢 *Use Case*: Display available cars to customers on a website.

'''

'''

### 🏦 **Q4. Bank Account System**

**Scenario**: A bank app tracks user deposits.
Create a class `BankAccount` with:

* Attributes: `account_holder`, `balance`
* Methods:

  * `deposit(amount)` → increases balance
  * `show_balance()` → displays balance
    🟢 *Use Case*: User adds ₹1000 to their account and checks balance.

'''

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Your Amount Added SuccessFully")

    def show_balance(self):
        print(f"Your Balance : {self.balance}")



b1 = BankAccount("Hard",1000000)

print(b1.account_holder)
print(b1.balance)
b1.deposit(1000)

b1.show_balance()
'''

### 🛒 **Q5. Shopping Cart System**

**Scenario**: An online store needs to calculate order totals.
Create a class `Product` with:

* Attributes: `name`, `price`, `quantity`
* Method: `total_cost()` → returns full cost (price × quantity)
  🟢 *Use Case*: Display total cost in the shopping cart.


'''


'''

🔧 Q6. Mobile Recharge System
Scenario: A mobile recharge app tracks user balance and allows top-up.

Create a class MobileUser with:

Attributes: name, balance

Methods:

recharge(amount) → add amount to balance

use_data(amount) → deduct amount from balance

show_balance() → display remaining balance

🟢 Use Case: User recharges ₹200, uses ₹50 for data, and checks balance.

📚 Q7. Library Book Management
Scenario: A library tracks book availability.

Create a class LibraryBook with:

Attributes: title, total_copies, issued_copies

Methods:

issue_book() → increase issued_copies by 1

return_book() → decrease issued_copies by 1

available_copies() → returns total - issued

🟢 Use Case: Librarian issues a book, then returns it, and checks available copies.


'''