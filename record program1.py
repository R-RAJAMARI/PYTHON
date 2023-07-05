
def factnum(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factnum(n-1)
def no_of_digits(n):
    i=0
    while(n!=0):
        n=n//10
        i=i+1
    return i

n=int(input("enter a positive number :"))
fact_num=factnum(n)
if (n%2!=0):
    print("factorial of number is ",fact_num)
    print("no of digits of factorial :",no_of_digits(fact_num))
else:
    num=str(n)
    if (num==num[::-1]):
        print("given number is palindrome")
    else:
        print("given number is not palindrome")
    
    
