def palindrome(i):
    re=0
    while i:
        d=i%10
        i=i//10
        re=re*10+d
    return re
n=int(input())
m=int(input())

for i in range(n,m+1):
    a=palindrome(i)
    if a==i:
        print(i,end=" ")
        
