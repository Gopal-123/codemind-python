def palindrome(temp):
    n=temp
    re=0
    while n:
        d=n%10
        n=n//10
        re=re*10+d
    if re==temp:
        return True
    return False    

n=int(input())
for i in range(1,n+1):
    m=int(input())
    if palindrome(m):
        print("True")
    else:
        print("False")
        