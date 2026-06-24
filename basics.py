# hackerrank, leetcode, codechef
# print("Hello World")

# x=input("Enter String: ")
# print("Length of String: ",len(x))
# print(x)
# print(type(x))
# char="0"
# print(type(char))

# z = complex(input())
# print(z)
# print(type(z))


# a="10"
# print(int(a))

# b="raj"
# print(int(b)) # error.. as name cant converted into int


# c=20
# print(float(c))


# g="raj"
# h="u"
# print(g+h)

# # str[stidx:endix:step]

# a="programming"
# print(a[2:4])
# print(a[3:6:-2]) # empty....backward
# print(a[5:6:2])
# print(a[2::-1])
# print(a[3::])
# print(a[-1])
# ab="language basics"
# print(ab.split())
# print(ab.strip)

# # f string mormatting
# name="vansh dadeech"
# age=20
# print("his name is", name,"his age is",age)
# print(f"his name is {name}. his age is {age}")

# # wap for if age>18: eligible to vote,  if age>40: , if age<18: not eligible to vote
# ag=int(input("Emter Age: "))
# if ag<18:
#     print("Stay at home")
# elif (ag>40):
#     print("stay at home")
# # elif (ag>=18 and ag<=40):
# #     print("Eligible to vote")
# else:
#     print("Eligible to vote")

# floor division--- round down the ans


# a="10"
# b="20"

# print(a*8)
# print(9/3)
# print(9//3)
# print(10.6/2)
# print(-10.6//2)

# print(-2.5//-0.5)
# print(9.5%3)

# print(-104)



# # make a calc for +, -, *, %, /, //

# opr=input("Enter Operation: ")
# if opr=='+':
#     n1=int(input("Enter Number 1: "))
#     n2=int(input("Enter Number 2: "))
#     print(f"Sum: {n1+n2}")
# elif opr=='-':
#     n1=int(input("Enter Number 1: "))
#     n2=int(input("Enter Number 2: "))
#     print(f"Subtraction: {n1-n2}")
# elif opr=='*':
#     n1=int(input("Enter Number 1: "))
#     n2=int(input("Enter Number 2: "))
#     print(f"Multiplication: {n1*n2}")
# elif opr=='/':
#     n1=int(input("Enter Number 1: "))
#     n2=int(input("Enter Number 2: "))
#     print(f"Division: {n1/n2}")
# elif opr=="//":
#     n1=int(input("Enter Number 1: "))
#     n2=int(input("Enter Number 2: "))
#     print(f"Floor Division: {n1//n2}")
# elif opr=="%":
#     n1=int(input("Enter Number 1: "))
#     n2=int(input("Enter Number 2: "))
#     print(f"Remainder: {n1%n2}")
# else:
#     print("Invalid Operator !!!")




# #  loops

# for i in range(2,11,2):
#     print(i)

# # searching program
# z=[22,89,745,36,74,96,25,63,14,63,45,85,96,145,32,45]
# print(z)
# s=int(input("Enter Element to Search: "))
# idx=45
# for i in range(len(z)):
#     if s==z[i]:
#         idx=i
# if idx==45:
#     print("Element Not Found")
# else:
#     print(f"Element {s}, found at index {idx}")

# # from while loop
# i=1
# while (i<=10):
#     if(i%2)==0:
#         print(i)
#     i+=1

# #  print the sum of first N natural numbers
# sum=0
# n=int(input("Enter N: "))
# for i in range(n+1):
#     sum+=i
# print(sum)

# # pattern printing
# for i in range(3):
#     print("")
#     for j in range(3):
#         print("*",end=" ")



# #  22-06-26

# list=[-1,-2,-3,-4,-5,-7,-8,-9]
# for i in range(min(list),max(list)):
#     if i not in list:
#         print("Missing Number is: ",i)

        

# # i*2 in list
# x=int(input())
# arr=list(map(int,input().split()))
# list=[]
# for i in arr:
#     # print(i*2,end=" ")
#     list.append(i*2)
# for i in list:
#     print(i, end=" ")


# # armstrong number

# x=(input().strip())
# count=len(x)
# sum=0
# for i in x:
#     sum+=(int(i))**count
# if int(x)==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# LIST COMPREHENSION: a shorthand way to write a list is called list comprehension
#1.
# list=[]
# 2.
# a=[]
# size=int(input())
# for i in range(size):
#     val=int(input("Value: "))
#     a.append(val)
# 3.
# a=[]
# for i in range(1,5):
#     a[i]=i*i
# # == 3. in one line
# a=[i*i for i in range(1,5)]
# a= list name
# i*i - elements u wanna enter
# for loop

# # /conversions
# a=[]
# for i in range(1,6):
#     a.append(i*2)
# print(a)
# # converting into LC
# a=[i*2 for  i in range(1,6)]
# print(a)

# a=[]
# for i in range(1,50):
#     if i%7==0:
#         a.append(i)
# print(a)
# # after LC
# a=[i for i in range(1,50) if i%7==0]
# print(a)

# a=[num if num<5 else num*2 for num in range(2,9)]
# print(a)
# a=[]
# for i in range(2,9):
#     if i<5:
#         a.append(i)
#     else:
#         a.append(i*2)
# print(a)

# values=[35,63,22,15,9,88,77]
# a=[i for i in values if i%3==0]
# print(a)

# a=[('a',11),('b',12),('c',13)]
# nl=[(x,n*3) for (x,n) in a if x=='b' or x=='c']
# # nl1=[(x,y) for (x,y*3) in a if x=='b' or x=='c']
# print(nl)
# # print(nl1)


# result=[]
# for x in [10,5,2]:
#     for y in [2,3,4]:
#         result.append(x**y)
# print(result)

# result=[x**y for x in [10,5,2] for y in [2,3,4]]
# print(result)


# Dictionary --  these are used to store data values in key: value pairs...
# --> unordered
# --> mutable
# --> they dont allow duplicate keys.

# dict={
#     "name":"Ravi",
#     "cgpa":"8.2",
#     "marks":88,
#     1:"2024a6r030"
# }
# print(dict)
# dict["name"]="raj"
# print(dict["name"])
# print(type(dict))
# # print(dict[0]) -- wrong
# null_dict={}
# print(null_dict)

# student={"name":"vansh",
#          "class":"a1",
#          "marks":{26,68,98,54,34}
#          }
# print(student["marks"])

# dictionary methods:

#### dict sushant:

# dict["name"] = "raj"
# print(dict["name"])
# # print(dict[0])
# d={}
# print(d)

# d["name"] = "yasin"
# print(d)

# print(d["Name"])

# student = {
#     "name" : "Avleen",
#     "age": 20,
#     "score":{
#         "c":98,
#         "cyber":56
#     }
# }
# # print(student)
# # print(student["score"])
# # print(student["score"]["c"])

# dict = {
#     "name": "ravi",
#     "cgpa" : "8.2",
#     88 : 88
# }

# for i in dict:
#     print(i)
# print(dict.keys())
# print((list(dict.keys())))

# for i in dict.keys():
#     print(i)

# print(dict.values())
# print(list(dict.values()))
# for i in dict:
#     print(dict[i])
# for i in dict.values():
#     print(i)

# for i,j in dict.items():
#     print(i,"->",j)

# for i,j in dict.items():
#     print(i,j)
# print(list(dict.items()))


# print()
# pair = list(student.items())
# n = list(pair[2][1].items())

# print(n[0])

### Sets: is a collection of data in unordered method.
# --> each element in a set must be unique.
# --> mutable
# --> each element in a set must be immutable.

# nums={1,2,3}
# ## marks={[1,2,3],2,3}  ---not a set because list in it is immutable
# marks={"raj","ravi", "rahul"}
# ram={"raj",55,"True",0,"True"}
# ram={(1,2,3),"r",1,2,3}
# print(marks)

collection={1,2,3,4}
print(collection)
print(type(collection))


# set
collection.add(5)
print(collection)

collection.remove(2)
print(collection)

collection.pop()
print(collection)

collection.clear()
print(collection)

#union
set1={1,2,3,4}
set2={5,6,7,8}

set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)