l=[]
n=int(input("enter the no of elements in list"))
for i in range(n):
    p=int(input("enter the num:"))
    l.append(p)
x=int(input("enter the index value:"))
if x>=len(l):
    raise IndexError("enter the correct index value")
else:
    print(l[x])
