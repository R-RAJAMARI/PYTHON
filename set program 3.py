s=input("enter string:")
v=set(['a','o','i','e','u'])
c=0
for i in s:
    if i in v:
        c=c+1
print(c)
