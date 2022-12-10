n=input()
b=n.split()
g=[]
g.append(min(b[0]))
g.append(max(b[-1]))
print(*g)