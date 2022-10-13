def power(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s=s+d
    return s    
        
    
    

n=int(input())
c=pow(n,2)
d=power(c)
if d==n:
    print("Neon Number")
else:
    print("Not Neon Number")