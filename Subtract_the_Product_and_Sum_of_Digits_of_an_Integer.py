def sum(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s=s+d
    return s
def pro(n):
    p=1
    while n:
        d=n%10
        n=n//10
        p=p*d
    return p
n=int(input())
a=sum(n)
b=pro(n)
c=b-a
print(c)
    
    
    