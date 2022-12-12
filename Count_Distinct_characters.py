n=input()
n=n.lower()
u=[]
for i in n:
    if ord(i)>=97 and ord(i)<=122 and i not in u:
        u.append(i)
print(len(u))        