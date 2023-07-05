def substring(s1,s2):
    if(s2 not in s1):
        print("NO",s2,"cannot be formed by deletion or addition charecters")
    else:
        print("YES",s2,"can  be formed by deletion or addition charecters")
s1=str(input("enter the larger string :"))
s2=str(input("enter the smaller string :"))
substring(s1,s2)
