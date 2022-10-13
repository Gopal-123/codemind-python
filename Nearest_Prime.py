import math
def prime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

n=int(input())
for i in range(1,n+1):
    
    m=int(input())
    for i in range(m,0,-1):
        if prime(i):
           break
    for j in range(m+1,m*m,+1):
        if prime(j):
           break
    c=m-i
    d=j-m
    if(c==d):
        if i<m:
           print(i)
        else:
           print(j)
            
    if c<d:
        print(i)
    elif c>d:
        print(j)
