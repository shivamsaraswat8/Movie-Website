l=[[4,20],[5,10],[20,20]]
w=2
a=[]
v=0
for i in range(len(l)):
    if w==0:
       print(a)
       print(v)
       break
    
    if l[i][0]>0:
        k=min(l[i][0],w)
        v=v+k*(l[i][1]/l[i][0])
        a.append(k)
        w=w-k

print(a)
print(v)
        
    

