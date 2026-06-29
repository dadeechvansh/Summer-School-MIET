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

def add(x,y):
    print(x+y)
a=int(input("Enter Num 1: "))
b=int(input("Enter Num 2: "))
add(a,b)

