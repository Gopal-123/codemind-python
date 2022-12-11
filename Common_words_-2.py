s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
c=a.split()
d=b.split()
g=[]
f=[]
for i in c:
    if c.count(i)==1 and d.count(i)==1 and i in d and i!=" ":
        g.append(i)
for i in  d:
    if d.count(i)==1 and c.count(i)==1 and i in c and i!=" ":
        g.append(i)
for i in g:
    if i not in f:
        f.append(i)
print(len(f))
