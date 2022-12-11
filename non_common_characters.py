s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
c=[]
d=[]
f=[]
for i in a:
    if i not in b and i!=" ":
        c.append(i)
for i in b:
    if i not in a and i!=" ":
        d.append(i)
c.extend(d)
for i in c:
    if i not in f:
        f.append(i)
f.sort()
k="".join(f)
print(k)
        