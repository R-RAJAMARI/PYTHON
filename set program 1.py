def isprime(n):
    if(n!=1):
        f=0
        for i in range(2,n):
            if (n%i)==0:
                f=f+1
        if f==0:
            return True
        else:
            return False
    else:
        print(n,"is neither prime nor composite")
s=set()
sd5=set()
for i in range(1,50):
    if isprime(i):
        s.add(i)
    if i%5==0:
        sd5.add(i)
r1=s.union(sd5)
r2=s.intersection(sd5)
r3=s.difference(sd5)
r4=s.symmetric_difference(sd5)
print("union",r1)
print("intersection",r2)
print("difference",r3)
print("symmetric_difference",r4)
