def pret(i):
    c=0
    while i:
        d=i%10
        i=i//10
        if d==2 or d==3 or d==5:
            c=c+1
        return c    


n=int(input())
for i in range(1,n+1):
    c=0
    m,g=map(int,input().split())
    for i in range(m,g+1):
        a=pret(i)
        c=c+a
    print(c)    
    