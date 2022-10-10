n=int(input())
ec=0
oc=0
while n:
    d=n%10
    n=n//10
    if d%2==0:
        ec=ec+1
    else:
        oc=oc+1
if ec>0 and oc>0:
     print("Mixed")
elif(ec>0):
     print("Even")
elif(oc>0):
    print("Odd")