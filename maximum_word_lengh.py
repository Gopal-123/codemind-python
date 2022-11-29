def c(i):
    for j in i:
        return (len(i))

n=input()
b=n.split()
s=[]
for i in b:
    s.append(c(i))
print(max(s))
    