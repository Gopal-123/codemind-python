n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2:
        o.append(i)
    else:
        e.append(i)
e.extend(o)
for i in e:
    print(i,end=' ')