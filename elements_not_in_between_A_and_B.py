def arr(n,m,s):
    if s<n or s>b:
        return True
    return False  
n=int(input())
g=[]
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in l:
    if arr(a,b,i):
        g.append(i)
        
if len(g)>0:
    for i in g:
        print(i,end=" ")
else:
    print("-1")
        
    