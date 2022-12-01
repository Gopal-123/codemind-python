n=input()
b=n.split()
g=[]
for i in b:
    c=0
    for j in i:
        c=c+1
    g.append(c)
print(sum(g))