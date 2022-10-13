import math
def prime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
    
def isprime(n):
    while n:
        d=n%10
        n=n//10
        if prime(d):
            continue
        return False
    return True    
n=int(input())
if prime(n) and isprime(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")