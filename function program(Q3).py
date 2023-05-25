import math 
def sphere():
    r=int(input("Enter the radius "))
    SA=4*math.pi*(r**2)
    V=(4/3)*math.pi*(r**3)
    print("surface area of sphere is ",SA)
    print("volume of sphere is ",V)
def cylinder():
    r=int(input("Enter the radius of cylinder "))
    h=int(input("Enter the height of cylinder "))
    SA=2*math.pi*r*(h+r)
    V=math.pi*(r**2)*h
    print("surface area of cylinder is ",round(SA,2))
    print("volume of cylinder is ",V)
def cone():
    r=int(input("enter the radius of cone "))
    h=int(input("Enter the height of cone "))
    s=int(input("Enter the slant height of cone "))
    SA=(math.pi*r*s)+(math.pi*(r**2))
    V=(1/3)*math.pi*(r**2)*h
    print("surface area of cone is ",SA)
    print("volume of cone is ",V)
def rectangular_prism():
    l=int(input("enter the length "))
    w=int(input("enter the width "))
    h=int(input("enter the height "))
    SA=2*((l*w)+(l*h)+(w*h))
    V=l*w*h
    print("surface area of rectangular prism is ",SA)
    print("volume of rectangular prism is ",V)

def triangular_prism():
    l=int(input("enter the length "))
    b=int(input("enter the breath "))
    s=int(input("Enter the slant height "))
    SA=(b*h)+(2*l*s)+(l*b)
    V=(1/2)*(b*l*h)
    print("surface area of triangular prism is ",SA)
    print("volume of triangular prism is ",V)

choice=int(input('''enter the choice\n
1.sphere
2.cylinder
3.cone
4.rectangular prism
5. triangular prism\n '''))
if(choice==1):
    sphere()
elif(choice==2):
    cylinder()
elif(choice==3):
    cone()
elif(choice==4):
    rectangular_prism()
else:
    triangular_prism()
