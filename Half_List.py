
def f(a,b):
    j=1
    g=[]
    for i in range(a):
        g.append(b[-j])
        j+=1
    c=(b[:a])
    g.extend(c)
    print(*g)


n=int(input())
l=list(map(int,input().split()))
c=len(l)//2
d=f(c,l)
