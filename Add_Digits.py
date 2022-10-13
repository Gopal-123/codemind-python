def sum(n):
    s=0
    while n:
       d=n%10
       n=n//10
       s=s+d
    return s
    
n=int(input())
while n:
    a=sum(n)
    if a<=9:
        print(a)
        break
    n=a

