# ____________________________________________________________________________________________________________________________________________________
# Python Modules:

# What is a library?
# A library is a collection of modules that is used for a specific type of application or need.

# 1. Python Standard Library:
#       -> this comes in-built with python

#  commonly used modules:
#  a. math module   : provides mathematical functions to support different type of calculations.
#  b. cmath module  : provides mathematical functions related to complex numbers.
#  c. random module : provides functions for generating random numbers.
#  d. urlib module  : provides url handling


# 2. NumPy Library          : Provides Some Advance Math Functionality along with tools to create and manipulate arrays.

# 3. Scipy Library          : For Scientific calculation

# 4. Pandas Library         : For Data Manipulation

# 5. Matplotlib Library     : Data Visualization (graphs & Charts)

# 6. Tkinter Library        : For GUI interface and different types of calculation

# 7. Beautiful Soup Library : For Web Scrapping

# 8. Scikit Learn Library   : For ML

# 9. OpenCV Library         : For Image & Video Processing

# _______________________________________________________________________________________________________________________________________________________

# What is Module ? :

# A python module is containing variables, class definitions, statements & functions related to a particular task.

# The Major feature of a module is that the content of it can be used in other programs without having rewrite or recreate them.

# Structure of a Python Module :
#   -> docstring : triple quoted string for document purpose (''' ''')
#   -> variables & constants
#   -> classes : Templates or blueprints
#   -> Objects : Instances of class
#   -> Statements : Instructions
#   -> Functions : for performing a task.


# Creating a Module:

#   -> To get help from a module you need to import that & then use help command to get help for that module.


#  Docstring Conversion:

#   -> First Letter of first line should be capital
#   -> Second line should be blank
#   -> Rest of the details begain from the third line

#  Importing a module : 2 Forms
#  1. To import entire module
#       --> import <module_name>
#  2. To import selected object from a module
#       --> from <module_name> import <function_name>

# After Importing a Module you can use any function/definition inside it as per the following Syntax:

# <module_name>.<function_name>()

# ---> the name of module is stored inside which constant :
#   ans : __name__
# s="hello"
# s[0]="H"
# l=[1,2,4,5,3]
# l[1:4]=[10]
# y=l.sort()
# print(y)
# a,*b,c=1,2,3,4,5
# print(b)


# ---> Package: it is a way to organize related modules into a directory hierarchy.

# Whats inside?? 

# ---> (__init__.py)  subpackages   Home.py   subpackage
#                     __init__.py               __init__.py
#                      Play.py                  New.py
#                       Cal.py                  Hello.py



# __init__.py -- it is a python file which distinguishes a package from a regular directory.
#               --> this can be empty pr can contain initialization code for package.

# jabh bhi aap kisi package ko import kroge toh usme sabse pahle (__init__.py) ka code run hoga

# creating a python package :
# Step 1) Create a Directory Structure
# Step 2) Define Modules
# Step 3) Import Module in the code

#  note - learn sep="-"
# sep stands for seperator
# difference b/w parent & root directory






# PIP- Python install package

# --- its like playstote of python

# eg- pip install numpy

# comman commands in pip


# Exception Handling :

# compiler: poore code ko compile krne wala ek sath
# interpreter: line by line code chalaata hai

# mostly there are 2 errors:

# 1. Compilation Errors --> Compile Ke Time
# 2. Runtime Errors--> when program runs

# --> compilation errors mostly code when you write a wrong syntax
# --> exception is a kind of runtime error.

# Types of Errors:
# 1. Syntax Error: errors that arises due to wrong syntax
# 2. logical error / sementic error:  that arises due to wrong logic
# 3. runtime errors : errors that are arise during execution


# Types of Exception:

# 1. Built-in Exception
# 2. User Defined Exception


# 1. Built-in Exception
#   a. syntax error
#   b. valueError : arises due to wrong type of value
#   c. IOError: arises while input/output operation.
#   d. keyboard interrupt error: arises dur ot keyboard. then its a type of a keyboard error..
#   e. import error : arises due to wrong import of a file or module
#   f. EOFError : arises due to reaching end of a file without executing inner things.
#   g. zero division error: this arises due to dividing by zero to a number.
#   h. indexError : arises dur to index
#   i. nameError: when using an idenrifier with no existence.
#   j. typeError: basically it arises when u expect a different type in any 

#   Exception Handling in Python:
#   1.try
#   2.except
#   3.else
#   4.finally

#   1. try: this is block in which those lines of code are placed which might contain error.
# 
#   2. except: this is the block in which statements related to handle are written.
# 
# note: 1. One try block can have multiple except blocks to handle multiple exceptions.
#       2. except block must be placed immediately after the try block.
#            
#   3. else: the statement indside else block are executed when there is no exception found in try block.
# 
#   4. finally: the statement inside this are executed irrespective of whether any exception is found in try block or not.


# try:
#     a=int(input("Enter Num: "))
#     b=int(input("Enter Num: "))
#     c=a/b
#     print("divide = ",c)
# except:
#     print("Divide by Zero is not defined ")

# else:
#     print("Program is Successfull")
# finally:
#     print("Hahah MIET Summer Bootcamp is nice")


# user defined exceptions:
# key word used is raise exception

# program:

age=int(input())
if age<0:
    raise Exception("age can't be negative")
elif age>=18:
    print("vote")
else:
    print("No vote")


