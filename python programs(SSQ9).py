food_rating=int(input("enter food rating(1 to 5)"))
service_rating=int(input("enter service rating(1 to 5)"))
ambience_rating=int(input("enter ambience rating(1 to 5)"))
billamount=int(input("enter billamount"))
if(food_rating>3):
    if(service_rating>3 and ambience_rating>3):
        billamount+=billamount*(10/100)
        print(billamount)
    else:
         billamount+=billamount*(5/100)
         print(billamount)
else:
     if(service_rating>3 and ambience_rating>3):
        billamount+=billamount*(5/100)
        print(billamount)
     else:
        billamount+=billamount*(1/100)
        print(billamount)
