n=5
# for j in range(n):
#     # print("*")
#     print("*",end=" ")

# 1st Pattern
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
print("Normal Pattern: ")
for i in range(n):   # row
    for j in range(n):   # column
        print("*",end=" ")
    print()

# 2nd Pattern (increasing order)

# *
# * *
# * * *
# * * * *
# * * * * *

print("Increasing Pattern:")
for i in range(n): # row
    for j in range(i+1): # stars
        print("*",end=" ")
    print()

# 3rd Pattern (decresing order)

# * * * * * 0 to 5
# * * * *   1 to 5
# * * *     2 to 5
# * *       3 to 5
# *         4 to 5
print("decreasing Pattern:")
for i in range(n): # row
    for j in range(i,n): # stars or range(n-i):
        print("*",end=" ")
    print()

# 4th Pattern (Right Angled Triangle pattern)
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

print("Right Angled Triangle pattern:")
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

# 5th pattern (inverted right angled )

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

print("inverted right angled pattern:")
for i in range(n): # row
    for j in range(i): # stars
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

# 6th pattern (pyramid)

#        *
#      * * *
#    * * * * * 
#  * * * * * * *
# * * * * * * * * *
print("Pyramid:")
for i in range(n):
    for j in range(i,n-1): #spaces
        print(" ", end=" ")
    for j in range(i): #stars
        print("*", end=" ")
    for j in range(i+1): #stars
        print("*", end=" ")
    print()

# 7th pattern (Inverted Pyramid)

# * * * * * * * * *
#  * * * * * * *
#    * * * * * 
#      * * *
#        *

print("Inverted Pyramid:")
for i in range(n): # row
    for j in range(i): # stars
        print(" ",end=" ")
    for j in range(n-i-1):  #or (i,n-1)
        print("*",end=" ")
    for j in range(i,n): 
        print("*",end=" ")
    print()


# 8th pattern (diamond)

#        *
#      * * *
#    * * * * * 
#  * * * * * * *
# * * * * * * * * *
#  * * * * * * *
#    * * * * * 
#      * * *
#        *
print("Diamond:")
for i in range(n-1):
    for j in range(i,n-1): #spaces
        print(" ", end=" ")
    for j in range(i): #stars
        print("*", end=" ")
    for j in range(i+1): #stars
        print("*", end=" ")
    print()
for i in range(n): # row
    for j in range(i): # stars
        print(" ",end=" ")
    for j in range(n-i-1):  #or (i,n-1)
        print("*",end=" ")
    for j in range(i,n): 
        print("*",end=" ")
    print()