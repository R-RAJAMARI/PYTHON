dicfare=1020*(20/100)
fare=1020
age=int(input("Enter age"))
if(age>60):
    date1=(int(input("enter day of date (in num) ")))
    month1=(int(input("enter month of date(in num) ")))
    year1=(int(input("enter year of date ")))   
    d2=11
    m2=5
    y2=2023
    if(year1>y2):
        print("your fare is ",dicfare)
    else:
        print("your fare is ",fare)
else:
    print("your fare is ",fare)
