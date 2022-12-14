def re(n):
    r=0
    while n:
        d=n%10
        n=n//10
        r=r*10+d
    return r
n=int(input())
if n<0:
    m=-(n)
    print(-re((m)))
else:
    print(re((n)))