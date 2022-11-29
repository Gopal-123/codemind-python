n=input()
k=input()
s=[97,101,105,111,117,65,69,73,79,85]
f=[]
for i in range(0,len(n)):
    if k==n[i]:
        f.append(i)
        break
if len(f)>0:
    print("True")
    print(*f)
elif len(f)==0:
    print("False")
        