# Iterators & Generators


# Iterators : its like a pointer jo pehle elemrnt ko point krta h fir next elemrnt ko point krta h

# Iterators are objects that can be iterated upon, meaning that you can traverse through all the values. 
# Technically, an iterator is any object which implements the `__iter__()` and `__next__()` methods.

# list=[10,20,30,40,50]
# it=iter(list) # this builds an iterator object
# x=next(it) # this returns the next value in the iterator
# print(x) # Output: 10
# x=next(it) # this returns the next value in the iterator
# print(x) # Output: 20
# x=next(it) # this returns the next value in the iterator
# print(x) # Output: 30

# lit=[10,20,30,40,50]
# it=iter(lit) # this builds an iterator object
# while True:
#     try:
#         x=next(it) # this returns the next value in the iterator
#         print(x) # Output: 10, 20, 30, 40, 50
#     except StopIteration:
#         break

# print("ye print hoga")


# Generators : ye ek function h jo ki ek value ko return krta h aur fir next value ko return krta h

# These are type of functions that uses yield as return.
# Note:
#   ---> yield does not end function like return, 
# it pauses the function saving all its states and later continues from there on successive calls.

# it saves memory and boosts performance.

def fun():
    return 10
    return 20
    return 30

x=fun()
print(x) # Output: 10

def fun1():
    yield 10
    yield 20
    yield 30
x=fun1()
print(x) # Output: <generator object fun1 at 0x000001F2D8C3A5E0>
print(next(x)) # Output: 10
print(next(x)) # Output: 20
print(next(x)) # Output: 30



# Question: write a generator method to produce n prime numbers.. may be in assesment test