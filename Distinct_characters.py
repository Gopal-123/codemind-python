n=input()
u=[]
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        if n.count(i)==1 and chr(ord(i)+32) not in n:
            u.append(i)
    elif ord(i)>=95 and ord(i)<=122:
        if n.count(i)==1 and chr(ord(i)-32) not in n:
            u.append(i)
u.sort()
b="".join(u)
print(b)
        