Digit_word = { 1 : "One", 2 : "Two" , 3 : "Three", 4 : "Four" , 5 : "Five" , 6 :"Six" , 7 : "Seven" , 8 : "Eight" , 9 : "Nine"}
n=int(input("enter a number:"))
for i in str(n):
    print(Digit_word[int(i)],end=' ')
