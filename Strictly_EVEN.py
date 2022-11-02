n=int(input())
l=list(map(int,input().split()))
k=[]
g=[]
for i in range(len(l)):
    if i%2==0 and l[i]%2==0:
        k.append(i)
    elif i%2 and l[i]%2==0:
        g.append(i)
if len(k)>0 and len(g)==0:
    print("True")
else:
    print("False")