n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
g=[]
for i in l:
    if i<a or i>b:
        g.append(i)
if len(g)>0:
    print(max(g))
else:
    print("-1")