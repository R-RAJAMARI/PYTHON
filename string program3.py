
str1=input("enter string")
l=str1.split()
maxi=""
for i in l:
    if len(i)>len(maxi):
        maxi=i
print(maxi,len(maxi))
