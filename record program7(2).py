d={}
name=input("enter your name :")
try:
    age=int(input("enter your age:"))
    if age<0:
        raise ValueError
    print("enter 6 subjects mark")
    l=[]
    total=0
    for i in range(6):
        x=int(input())
        l.append(x)
        total+=x
    d['name']=name
    d['age']=age
    d['marks']=l
    d['total']=total
    d['average']=total/6
    print(d)
    
except ValueError:
    print(d)
