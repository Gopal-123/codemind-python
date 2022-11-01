n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i==0 or i==1:
        a.append(i)
    else:
        b.append(i)
if len(b)==0:
    print('True')
else:
    print('False')
    