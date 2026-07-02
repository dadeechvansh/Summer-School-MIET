# Functions: it is a subprogram i.e. part of the program that carries out some well defined tasks.

# functions are categorized into 2 main categories:
# 1. Built in functions - which are already defined
#  for eg.: print(), import random- [ random(), randint(a,b) ]
# import random
# print(random.random())
# print(random.randint(12,14))

# 2. User defined functions - a function by the user for a specific task is user defined function.

# 2.a Function definition
# 2.b Function call :


# Arguments:  it is the value which is supplied to the function.
# return: return a value of a function where it is called.

#           Parameter                             vs	                       Argument
# A variable defined in a function definition.	        The actual value passed to the function when it is called.
# Exists when creating the function.	                Exists when calling the function.
# Placeholder for data.	                                Real data given to the function.

# ways of writing a function:
# 1. no argument & no return
# 2. no argument & with return
# 3. with argument & with return
# 4. with argument & no return

# def function_name(a,b):
#     sum=a+b
#     return sum
# x=int(input("Enter Num 1: "))
# y=int(input("Enter Num 2: "))
# print(function_name(x,y))

# multi threaded vs single threaded

# import time

# print("Task 1")
# time.sleep(2)

# print("Task 2")
# time.sleep(2)

# print("Done")


# 1. no argument & no return

# def add():
#     a=int(input("Enter Num 1: "))
#     b=int(input("Enter Num 2: "))
#     print(f"Sum: {a+b}")
# add()

# 2. no argument & with return

# def add():
#     a=int(input("Enter Num 1: "))
#     b=int(input("Enter Num 2: "))
#     return a+b
# print(add())

# 3. with argument & with return

# def add(x,y):
#     return x+y
# a=int(input("Enter Num 1: "))
# b=int(input("Enter Num 2: "))
# print(add())


# 4. with argument & no return

# def add(x,y):
#     print(x+y)
# a=int(input("Enter Num 1: "))
# b=int(input("Enter Num 2: "))
# add(a,b)

# # bcdi------------------------------------------
# def vansh(x,y):
#     mul1=int(input("Enter Multiple 1: "))
#     mul2=int(input("Enter Multiple 2: "))

#     ans1=mul1*x
#     ans2=mul2*y
#     return (ans1,ans2)
# a=int(input("Enter Num 1: "))
# b=int(input("Enter Num 2: "))
# d,e=vansh(a,b)
# print(d)
# print(e)
# print(vansh(a,b))

# # bcdi max
# for i in vansh(a,b):
#     print(i)
# # ----------------------------------------------

#  find whether a numver is odd or even using function.

# def evodd(num):
#     if num%2==0:
#         # return True
#         # return "Even"
#         print("Even")
#     else:
#         # return False
#         # return "Odd"
#         print("Odd")
# x=int(input("Enter Number: "))
# # print(evodd(x))
# evodd(x)

# reverse of a number using string

# def rev(s):
#     return (s[::-1])
# s=input()
# print(rev(s))


# reverse of a number using num

# def revers(num):
#     rev=0
#     while num > 0:
#         digit = num % 10
#         rev = rev*10 + digit
#         num//= 10
#     return rev
# s=int(input("Enter Number: "))
# print(revers(s))
# # print(type(revers))

# # 1st iteration -1234
# digit=1234 % 10 =4
# rev = 0 * 10 + 4 = 4
# num//=10 =123

# # 2nd iteration
# digit=123 % 10 =3
# rev = 4 * 10 + 3 = 43
# num//=10 =12

# # 3rd iteration

# digit=12 % 10 =2
# rev = 43 * 10 + 2 = 432
# num//=10 =1


# # 4th iteration

# digit=1 % 10 =1
# rev = 432 * 10 + 1 = 4321
# num//=10 =0

# final ans= 4321

# Types of Argument: 

# 1. Positional Arguments
# Arguments/ values that are stored in the same order as the parameters

# def add(a, b):
#     print(a + b)
# add(10, 20)

# 2. Keyword Arguments
# Arguments are passed using parameter names.

# def student(name, age):
#     print(name, age)
# student(age=20, name="Ansh")

# 3. Default Arguments
# A parameter has a default value.

# def greet(name="Guest"):
#     print("Hello", name)

# greet()
# greet("Ansh")

# Output:
# Hello Guest
# Hello Ansh

# 4. Variable-Length Arguments
# (a) *args – Multiple Positional Arguments
# def total(*nums):
#     print(sum(nums))

# total(10, 20, 30, 40)

# Output:
# 100

# Homework - how to reverse negative number

# num = int(input("Enter a number: "))
# if num < 0:
#   sign = -1
# else :
#    sign=1
# num = abs(num)
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(sign * rev)



# Local Variable - A local variable is declared inside a function and can only be used within that function.

# def greet():
#     message = "Hello"   # Local variable
#     print(message)
# greet()
# print(message)  # ERROR


# Global Variable - A global variable is declared outside all functions and can be accessed from anywhere in the program.

# name = "Ansh"   # Global variable

# def display():
#     print(name) 

# display()
# print(name)

# eg.-
# a=3
# def demo():
#     a=5
#     print(a)
# demo()
# print(a)

# *args (Non-keyword / Positional Arguments)
# *args collects multiple positional arguments into a tuple.

# def add(*args):
#     print(args)
#     print(sum(args))

# add(10, 20, 30, 40)
 # eg.-
# student=["ram","Raju","arjun","giya"]
# def name(*student):
#     print(student)
# name(*student)
# print(type(student))
# **kwargs (Keyword Arguments)
# **kwargs collects keyword arguments into a dictionary.

# def student(**kwargs):
#     print(kwargs)

# student(name="Ansh", age=21, city="Jammu")

# student={"name":"Ansh", "age":"21", "class":"first"}
# def student_info(student):
#     print(student["name"])
#     print(student["age"])
#     print(student["class"])

# student_info(student)

# def create_user(user):
#     print(user)
# create_user({"name":"Rahul","age":20})

# def create_students(students):
#     for student in students:
#         print(student)

# create_students(["Rahul","Ankit","Aman"])

# def get_numbers():
#     return [10,20,30,40]
# print(get_numbers())

# def get_student():
#     return {"id":1,"name":"Rahul"}s
# print(get_student())

# 01-07-26

# Nested Function:
# def outer():
#     print("it is outer")
#     def inner():
#         print("it is inner")
#     return inner()
# x=outer()
# print(x)

# closure: is useful when you want a function to remember some configuration or statement without using global variables 
#          repeatedly passing the same argument...

# oneline - function + remembered variable

# closure function is a function that remembers variable of its outer function even after the outer function has finished
#         executing...


# def new(num):
#     def actual(x):
#         return x**num
#     return actual
# f=new(2)
# g=new(3)

# # print(f)
# # print(g)

# print(f(3))
# print(g(3))

#OWN PRAC.

# def mine(st):
#     def st_mul(x):
#         return st*x
#     return st_mul
# fstore=mine("Vansh ")
# fstore2=mine("Dadeech ")
# xc=fstore(2)
# xd=fstore2(3)
# print(f"{xc} {xd}")

#BCDI ----------------------------
# p=int(input("How Much Time: ")) 
# for i in range(p):
#     xc=fstore(1)
#     xd=fstore2(1)
#     print(f"{xc} {xd}")
#----------------------------------


# Recursion: when a function calls itself repeatedly

# 2 main things :
    # 1. Base Case
    # 2. Work

# print n to 1 backwards:

# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
#     print("end")

# x=int(input())
# show(x)

# factorial using recursion

# def fact(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         return x*fact(x-1)
# x=int(input())
# z=fact(x)
# print(z)
    

# def sum(x):
#     if x==0:
#         return 0
#     else:
#         return x+sum(x-1)
# x=int(input())
# z=sum(x)
# print(z)
    

# def plist(list,index):
#     if index==len(list):
#         return
#     print(list[index])
#     plist(list,index+1)
# plist([1,2,3,4,5,6],0)


# 02-07-26
# Lambda Function /anonymous Function:

# A lambda function is a small anonymous (nameless) function that is written in a single line.
# It is used for simple operations where defining a full function with def is unnecessary.

# Syntax : Lambda Argument, expression.

# def square(x):
#     print(x**2)

# square(5)

# print((lambda x :x**2)(5))

# x=((lambda a,b,c :a+b+c))
# print(x(3,4,5))


# sum of first n natural number: 

# def sum(n):
#     return n*(n+1)//2
# print(sum(5))

# # using lambda 
# x=((lambda n:n*(n+1)//2))
# print(x(5))

# filter():
# returns an iterator where the items are filtered through a function to test if the item is accepted or not.

# ages=[5,12,17,18,24,80,8]
# def myfun(x):
#     if x<18:
#         return False
#     else:
#         return True
    
# adults=list(filter(myfun,ages))
# for x in adults:
#     print(x)

# # Lambda

# adults = list(filter(lambda x: x >= 18, ages))
# for x in adults:
#     print(x)


# find even values of a list using filter

# nums=[1,3,4,5,2,7,8,98,8]
# def even(x):
#     if x%2==0:
#         return True
# numbers=list(filter(even,nums))
# for i in numbers:
#     print(i)

# numbers1=list(filter(lambda x:x%2==0,nums))
# for i in numbers:
#     print(i)

# MAP : it executes a specified function for each item in a iterable . The item is sent to function as parameter.
# -----> data nikalna and us par kuch operation krna

# example: 

ages=[5,12,13,14,18,90,67,56]

def myfun(x):
    if x<18:
        return False
    else:
        return True

def myfun1(x):
    return x*x

adult=list(filter(myfun,ages))

# for x in adult:
#     print(x)

square=map(myfun1,adult)
for x in square:
    print(x)


adult=filter(lambda a: a>=18,ages)
square=list(map(lambda a: a*a, adult))

for i in square:
    print(i)
