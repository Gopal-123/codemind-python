n=input()
s=[]
g=[]
for i in n:
    if i.isdigit():
        s.append(i)
for i in s:
    g.append(int(i))
print(sum(g))
