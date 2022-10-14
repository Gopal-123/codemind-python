n=(input())
d=str(n)
g=d[::-1]
h=int(g)
if h%10==0 or len(d)>10 or len(d)<10:
    print("Invalid")
elif len(d)==10:
    print("Valid")
    
        

