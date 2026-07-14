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

# class Student:
#     @staticmethod  #--- decorator
#     def college():
#         print("MIET")

# Decorator: decorators allow us to wrap  another function in 
#            order to extend the behavious of the wrppped function without permanently modifying it.



# Abstraction: Hiding the implementation details of a class & only showing the essential features to the users is abstraction.

# class Car:
#     def __init__(self):
#         self.breaking=False
#         self.clutch=False
#         self.accelerating=False
#     def start(self):
#         self.clutch=True
#         self.accelerating=True
#         print("Car chalegayi")

# car1=Car()
# car1.start()


# Encapsulation: Wrapping data & features into a single unit(object)

#que: create account class with 2 attributes, balance and account number.. now create methods for debit, credit and printing the balance.

# class Account:
#     def __init__(self, balance):
#         self.balance = balance

#     def credit(self, amt):
#         self.balance += amt

#     def debit(self, amt):
#         self.balance -= amt

#     def show(self):
#         print("Balance:", self.balance)


# a = Account(5000)
# a.credit(1000)
# a.debit(500)
# a.show()

# 13-07-26

# del Keyword: used to delete object property or object itself.

# del s1.name
# del s1

# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("ram")
# print(s1)
# del s1
# print(s1)

# private(like) attributes & methods:

# private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass #---- here (__)--- (double underscore) makes private

#     def reset(self):
#         print(self.__acc_pass)
# acc1=Account("123456","abcde")
# print(acc1.acc_no)
# print(acc1.reset())
# print(acc1.__acc_pass) # ---gives error as its an private attribute



# Inheritance: When one class (child/derived) derives the properties & methods of another class (parent/base)

# class Car:
#     @staticmethod
#     def start():
#         print("Shuru Hoja")
    
#     @staticmethod
#     def stop():
#         print("rukja")

# class Tata(Car):
#     def __init__(self,name):
#         self.name=name

# car1=Tata("Nano")
# print(car1.name)
# print(car1.start())


# Types of Inheritance:

# 1. Single Inheritance
# 2. Multilevel Inheritance : Multi level of parents and child
# 3. Multiple Inheritance


# 2. Multilevel Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("shuru hoja")
#     @staticmethod
#     def stop():
#         print("rukja")

# class Tata(Car):
#     def __init__(self,name):
#         self.name=name
# class Mahindra(Car):
#     def __init__(self,type):
#         self.type=type

# car1=Mahindra("Diesel")
# Mahindra.start()



#3. Multiple Inheritance
# one derived class can inherit properties of multiple classes.

# class A:
#     varA="Hello java (sidhvi)"

# class B:
#     varB="hello Macbook(shivangi)"
# class C(A,B):
#     varC="Welcome Back"

# c1=C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)


# Super Method :

# Super() method is access methods of parent class.

# class Car:
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car shuru")
#     @staticmethod
#     def stop():
#         print("rukja")

# class Tata(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name

# car1=Tata("Nano","electric")


# Class Method:

# A class method is bound to the class & recieves the class as an implicit 


# class Person:
#     name="anonymous"

#     def collegename(self, name):
#         self.name=name
#         Person.name=name
#         self.__class__.name=name
# p1=Person()
# p1.collegename("MIET")
# print(p1.name)
# print(Person.name)

# but i want ki function ke andr hi class method ko direct access kr pau


# class Person:
#     name="anonymous"
#     animal="cat"

#     @classmethod
#     def collegename(cls, name, animal):
#         cls.name=name
#         cls.animal=animal
        
# p1=Person()
# p1.collegename("MIET","LION")
# print(p1.name)
# print(p1.animal)
# print(Person.name)
# print(Person.animal)


# Property:
# we use @property on any method in class to use the method as a property.

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage
#     def calculatePercentage(self):
#         self.percentage
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3) + " %"

# student1=Student(89,55,66)
# print(student1.percentage)
# print(student1.calculatePercentage())


# student1.phy=70
# print(student1.phy)
# # print(student1.percentage)
# # print(student1.calculatePercentage)
# print(student1.percentage)


# Polymorphism:

# in oops polymorphism allows the same method function to behave differently depending on the object

# example: len() [built - in ploymorphism]
# print(1+2)
# print("jatin"+"anirudh") # concatination
# print([1,2,3]+[4,2,3]) #merge


# Key Points to remember:
# Meaning : One Interface, many implementations.
# Built in functions like len() and operations like (+) are examples of polymorphism in python

# for eg:
# object

# Here we are using '+' for 3 different operations. So we can see 1 operator used in many forms.
# So this is called operator overloading & it's an example of polymorphism.


# Dunder Functions: __<FUNCTION_NAME>__ for eg- (__add__)

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def showNumber(self):
#         print(self.real,"i + ",self.img,"j")
#     def __add__(self,num2):
#         newreal=self.real;+num2.real
#         newImg=self.img+num2.img
#         return Complex(newreal,newImg)
#     def add(self,num2):
#         newreal=self.real;+num2.real
#         newImg=self.img+num2.img
#         return Complex(newreal,newImg)
# num1=Complex(1,3)
# num1.showNumber()

# num2=Complex(4,5)
# num2.showNumber()

# num3=num1+num2
# num3.showNumber()

# num4=num1.add(num2)
# num4.showNumber()


# Question: Define a circle class to create a circle with radius r using the constructor.
# define area() method of the class with calculates the area of the circle.
# define a perimeter method of the class which allows you to calculate the perimeter of the circle.

# class circle:
#     pi=22/7
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         print("Area:", self.pi*self.r**2)
#     def perimeter(self):
#         print("Perimeter:",self.pi*2*self.r)
    

# obj1=circle(4)
# obj1.area()
# obj1.perimeter()

# define a employee class with attributes role, department & salary. this class also has a showdetails() method.
# create an engineer class that inherits properties from Employee.
# class Employee:
#     def __init__(self,role,dept,sal):
#         self.role=role
#         self.dept=dept
#         self.sal=sal
#     def showdetails(self):
#         print(f"Role : {self.role}\nDepartment : {self.dept}\nSalary: {self.sal}")
# # create an engineer class that inherits properties from Employee.
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","IT",150)
#     def showdetails(self):
#         super().showdetails()
#         print(f"Name : {self.name}\nAge : {self.age}")
    

# obj1=Employee("Peon","CSE - AIML", 90000)
# obj1.showdetails()

# obj2=Engineer("Software Engineer","nandu")
# obj2.showdetails()

# Create a class called order which stores item & its price

# use dunder function __gt__() to convey that:
#       order1>order2 if price of order1>price of order 2

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, other):
#         if self.price > other.price:
#             print(f"{self.item} is costlier than {other.item}")
#         else:
#             print(f"{other.item} is costlier than or equal to {self.item}")


# order1 = Order("Laptop", 60000)
# order2 = Order("Mobile", 30000)

# order1 > order2



