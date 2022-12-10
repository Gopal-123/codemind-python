n=input()
u=[]
g=[]
c=0
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        if n.count(i)==1 and chr(ord(i)+32) not in n:
            u.append(i)
            c+=1
    elif ord(i)>=95 and ord(i)<=122:
        if n.count(i)==1 and chr(ord(i)-32) not in n:
            u.append(i)
            c+=1
    if c==1:
        print(i)
        break
if c==0:
    print("-1")
    

