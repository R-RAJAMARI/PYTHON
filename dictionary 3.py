d={}
for i in range(1,10):
    s=set()
    for j in range(1,i+1):
        if i%j==0:
            s.add(j)
    d[i]=s
print(d)
