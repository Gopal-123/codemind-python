n=int(input())
s=0
c=0
while n:
    if n==1:
        print("Ugly Number")
        break
    if n%2==0:
        n=n//2
        c+=1
    elif n%3==0:
        n=n//3
        c+=1
    elif n%5==0:
        n=n//5
        c+=1
    else: 
        print("Not Ugly Number")
        break
        


        