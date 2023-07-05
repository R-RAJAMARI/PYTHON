l=[]
n=int(input("enter the no of elements in list"))
for i in range(n):
    p=int(input("enter the num:"))
    l.append(p)
try:
    x=int(input("enter the index value:"))
    print(l[x])
except:
    print("index not present,the last index value is:",len(l)-1)
