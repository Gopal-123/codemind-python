n=input()
b=n.split()
s=[]
for i in range(0,len(b)):
    if i%2==0:
        k=b[i][::-1]
        s.append(k)
    else:
        s.append(b[i])
print(*s)