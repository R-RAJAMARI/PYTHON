s=set()
for i in range(1,30):
    s.add(i**2)
l=[]
for j in range(1,30):
    if(j%3)==0:
        l.append(j)
r=s.difference(set(l))
print(r)
