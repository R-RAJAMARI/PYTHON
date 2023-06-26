a=int(input("enter starting range:"))
b=int(input("enter ending range:"))
for i in range(a,b+1):
    f_c = 0
    if i!=1:
        for j in range(2,i):
            if(i%j == 0):
                f_c += 1
        if (f_c==0):
            print(i,end=' ')
