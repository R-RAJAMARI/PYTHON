t=[]
n=int(input("enter the no. of elements in tuple :"))
for i in range(n):
    p=input("enter the element of tuple:")
    t.append(p)
t=tuple(t)
print(t)
s=""
for i in t:
    s=s+i
print(s)
t1=[]
n=int(input("enter the no. of elements in tuple :"))
for i in range(n):
    p=input("enter the element of tuple:")
    t1.append(p)
t1=tuple(t1)
print(t1)
print(t1[::-1])
