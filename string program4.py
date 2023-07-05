def length(s):
    length=len(s)
    print("length of sring ",length)
    if length%5==0:
        s=s[::-1]
        s=s.upper()
        print(s)
str1=input("enter the string")
length(str1)
