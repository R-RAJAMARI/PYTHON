def addquantity(g):
    p=input("enter the product to add quantitY")
    aq=int(input("enter the no of quantity to be added"))
    g[p]["quantity"]=g[p]["quantity"]+aq
    print(g)

def update(g):
    pro=input("enter the product to change price")
    new_p=int(input("enter the new price"))
    g[pro]["price"]=new_p
    print(g)
def addnew(g):
    item=input("enter the new item")
    q=int(input("enter quantity"))
    p=int(input("enter price"))
    g[item]={"quantity":q,"price":p}
    print(g)
    
Grocery = { "Cornflakes" : {"quantity" : 15 , "price" : 100} , "Muesli" : {"quantity" : 14 , "price" : 150}, "Oats" : {"quantity":10, "price" : 80},"Wheat Flakes" : {"quantity" : 5, "price" : 75},"Granola" : {"quantity" : 8, "price" : 125}}
print(Grocery)
print('''what you want to do?
1.Add the additional quantity of the cereals
2.Update the price of the grocery
3.Add new item''')
choice=int(input())
if choice==1:
    addquantity(Grocery)
elif choice==2:
    update(Grocery)
else:
    addnew(Grocery)
        
