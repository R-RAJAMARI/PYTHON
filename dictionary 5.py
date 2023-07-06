Cricketer = {"VinayKumar":{102,5},"Yuzvendra Chahal" : {89,10}, "Sandeep Sharma" : {95,8}, "Umesh Yadav" : {85,6}, "BhuvaneswarKumar":{106,10}, "Basil Thampi ": {70,5}}
l=[]
r=0
for k,v in Cricketer.items():
    l=list(v)
    if(l[0]>l[1]):
        v=l[0]/l[1]
    else:
        v=l[1]/l[0]
    Cricketer[k]=v
sorted_dict = sorted(Cricketer.items(), key=lambda x: x[1])
sorted_dict=sorted_dict[::-1]
sorted_dict=dict(sorted_dict)
    
print(sorted_dict)
print(Cricketer)
        
