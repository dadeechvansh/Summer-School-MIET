# oop: object oriented programming
#  to map real world scenarios, we started using objects in code, this is called oops.

# classes & objects in Python 
# class is a blueprint of an object



# # creating class
# class Student:
#     name = "Jatin"

# # creating objetcs
# s1=Student()
# print(s1.name)

# s2=Student()
# print(s2.name)


# __init__ function: 

# constructor: (at the object creation)
# all classes have a function called __init__() which is always executed when the object is being initiated.


# class Student:
#     def __init__(self,name):
#         self.name=name
#         print("adding student data")
#         print(self)
# s1=Student("Kashuu")


# *** Basically self parameter is a reference to the current instance of the vlass and is used to access variables that belobgs 
#   to the class.

# Attribute : Variables or data that are we are storing inside the class or inside the object is attribute
# # 1. Default constructor
# def __init__(self):
#     pass
# # 2. Parameterized constructor
# def __init__(self,name,birthdays):
#     self.name=name
#     self.birthdays=birthdays

# Class Attribute: jho chiz common hai that is this

# Instance Attribute: which is not common

# Methods:
# Methods are functions that belongs to objects.

# class Student:
#     def __init__(self,name):
#         self.name=name
#     def hy(self):
#         print("hello",self.name)

# s1=Student("Kashu")
# s1.hy()

# Q: Create student class that names & marks of 3 subjects as arguments in constructor then create a method to print max of the marks

# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def max_marks(self):
#         print("Max Marks =", max(self.m1, self.m2, self.m3))

# n=input("Enter Name: ")
# mar1=int(input("Enter Marks 1:"))
# mar2=int(input("Enter Marks 2:"))
# mar3=int(input("Enter Marks 3:"))
# s1 = Student(n,mar1,mar2,mar3)
# s1.max_marks()


# Static Method:
# Methods that don't use self parameter (works at class level)

class Student:
    @staticmethod  #--- decorator
    def college():
        print("MIET")

# Decorator: decorators allow us to wrap  another function in 
#            order to extend the behavious of the wrppped function without permanently modifying it.



# Abstraction: Hiding the implementation details of a class & only showing the essential features to the users is abstraction.

class Car:
    def __init__(self):
        self.breaking=False
        self.clutch=False
        self.accelerating=False
    def start(self):
        self.clutch=True
        self.accelerating=True
        print("Car chalegayi")

car1=Car()
car1.start()


# Encapsulation: Wrapping data & features into a single unit(object)

#que: create account class with 2 attributes, balance and account number.. now create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, balance):
        self.balance = balance

    def credit(self, amt):
        self.balance += amt

    def debit(self, amt):
        self.balance -= amt

    def show(self):
        print("Balance:", self.balance)


a = Account(5000)
a.credit(1000)
a.debit(500)
a.show()