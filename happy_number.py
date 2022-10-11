def ha(n):    
    sum=0
    while(n):
        d=n%10
        n=n//10
        f=pow(d,2)
        sum=sum+f
    return sum

def happy(n):
    while(n):
        a=ha(n)
        if a==1 or a==7:
            return True
        elif a!=1 or a!=7:
            n=a
        if a<10:
            return False
n=int(input())
if happy(n):
    print("True")
else:
     print("False")
