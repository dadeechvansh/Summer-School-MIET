# mat=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]


#snake traversal
# row=len(mat)
# col=len(mat[0])

# final=[]

# for i in range(row):

#     if i%2==0:
#         for j in range(col):
#             final.append(mat[i][j])
#     else:
#         for j in range(col-1,-1,-1):
#             final.append(mat[i][j])


# print(final)



# s="pythonrocks"
# print(s[-6:-1])

# print("Data Science".replace("a","@",1)) # 1 here refers that only till once referrance

# name="Alice"
# age=30
# print(f"{name},{age}")

# print(f"{3.14159:>10.2f}|")

# print(None==False)

# x=[]
# print("empty" if not x else "not empty")

# x=5
# print(1<x<10<x)


# total=0
# for i in range(1,5):
#     if i==3:
#         continue
#     total+=i
# print(total)

# i=0
# while i<3:
#     print(i,end=" ")
#     i+=1
# else:
#     print("done")

# fun=[lambda:i for i in range(3)]
# print([f() for f in fun])


# print([x for x in range(10) if x%3==0])

# lst=[1,2,3]
# lst.insert(1,99)
# print(lst)


# matrix=[[0]*3]*3
# matrix[0][0]=1
# print(matrix)

# print({1,2,3} | {3,4,5})

# print({True,1,1.0,"1"}).

# c=100
# def show():
#     print(c)
# show()


# def f(n):
#     return 1 if n==0 else n*f(n-1)
# print(f(4))


def f():
    try:
        return 1
    finally:
        return 2
print(f())