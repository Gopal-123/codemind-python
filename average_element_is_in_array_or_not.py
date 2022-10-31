n=int(input())
l=list(map(int,input().split()))
d=sum(l)//n
for i in range(len(l)):
    if l[i]==d:
        print("True")
        break
else:
    print("False")