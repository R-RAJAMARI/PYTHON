name=str(input("enter name"))
YoS=int(input("enter years of service"))
salary=int(input("enter your salary"))
if YoS>10:
    print("your bonus",salary*(10/100))
elif YoS>6 and YoS<10:
     print("your bonus",salary*(8/100))
else:
    print("your bonus",salary*(5/100))
    
