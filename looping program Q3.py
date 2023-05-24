a=int(input())
b=int(input())
for i in range(a+1,b):
    for j in range(2,i):
        if i%j==0:
            break
        print(i,end=",")

