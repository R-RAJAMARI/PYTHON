v=float(input("enter wind speed"))
t=float(input("enter temperature"))
wc=13.12 + 0.6215*t - 11.37*v*0.16 + 0.3965*t*v*0.16
print("wind chill index is ",round(wc))
