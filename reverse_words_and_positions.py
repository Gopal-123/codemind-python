n=input()
b=n.split()
s=[]
for i in b:
    k=i[::-1]
    s.append(k)
s.reverse()
print(*s)