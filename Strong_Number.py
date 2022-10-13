def strong(temp):
    n=temp
    s=0
    while n:
        d=n%10
        n=n//10
        a=fun(d)
        s=s+a
    if s==temp:
        return True
    return False    

def fun(n):
    if n==0:
        return 1
    return n*fun(n-1)    
n=int(input())
if strong(n):
    print("The number %(n)d is a strong number" %{"n":n})
else:
    print("The number %(n)d is not a strong number" %{"n":n})