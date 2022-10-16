n=int(input())
s=0
while n:
    d=n%10
    n=n//10
    if s<=d:
        s=d
print(s)        
