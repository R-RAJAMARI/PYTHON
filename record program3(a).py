l=[]
n=int(input("enter the no of elements in list"))
for i in range(n):
    p=int(input("enter the num:"))
    l.append(p)
print(l)
r=int(input("enter the element to search:"))
print("positive index:")
for j in range(len(l)):
    if(l[j]==r):
        print(j,end=' ')
print()
print("negative index:")
for k in range(-len(l),0):
    if(l[k]==r):
        print(k,end=' ')
