def rev(n):
    re=0
    while n:
       d=n%10
       n=n//10
       re=re*10+d
    return re   
    
    

n=int(input())
c=n*n
a=rev(c)
d=rev(n)
e=d*d
f=rev(e)
if c==f and e==a:
    print("True")
else:
    print("False")