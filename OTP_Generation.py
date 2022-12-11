
        

n=input()
d=0
for i in n:
    if int(i)%2:
        d=d*10+int(i)
f=str(d)
g=[]
for i in f:
    g.append(str((pow(int(i),2))))
m="".join(g)
print(m)