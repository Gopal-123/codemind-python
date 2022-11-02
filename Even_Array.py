n=int(input())
l=list(map(int,input().split()))
k=[]
g=[]
for i in l:
    if i%2==0:
        k.append(i)
    else:
        g.append(i)
if len(k)>0  and len(g)==0:
    print("True")
else:
    print("False")
        