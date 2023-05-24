name=str(input("enter name "))
age=int(input("enter age "))
gender=str(input("enter gender M or F"))
no_days=int(input("enter no.of days of work"))
if(age>=18 and age<30 and gender=='M'):
    print("your salary",no_days*700)
elif(age>=18 and age<30 and gender=='F'):
     print("your salary",no_days*750)
elif(age>=30 and age<40 and gender=='M'):
     print("your salary",no_days*800)
elif(age>=30 and age<40 and gender=='F'):
     print("your salary",no_days*800)
else:
    print("error")
