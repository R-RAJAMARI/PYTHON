l=[]
n=int(input("enter no.of elements"))
for i in range(n):
    p=int(input("enter the value:"))
    l.append(p)
l1=sorted(l)
if(l==l1):
    print("list is in ascending order")
else:
    print("list is not in ascending order")
