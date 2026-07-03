
words=["apple","banana","cat"]
d={}
for x in words:
    d[x]=len(x)
print(d)

d={x:len(x) for x in words}
print(d)
