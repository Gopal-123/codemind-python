a,b=map(int,input().split())
l=list(map(int,input().split()))
s=[]
for i in l:
    k=abs(i)
    c=0
    if k==0:
        c=c+1
    while k:
        k=k//10
        c=c+1
    if c==b:
        s.append(c)
print(len(s))    
    
        
