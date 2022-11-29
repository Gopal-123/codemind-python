n=input()
b=n.split()
s=[]
for i in b:
    k=i[::-1]
    g=k[::-1]
    s.append(g)
s.reverse()
print(*s)
    