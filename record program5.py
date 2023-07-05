a={1,2,3,4}
b={1,2,3}
k=0
for i in b:
    if i in a:
        k=k+1
if k==len(b):
    print("b is a subset of a")
