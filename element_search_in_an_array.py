n=int(input())
l=list(map(int,input().split()))
c=int(input())
for i in range(len(l)):
    if l[i]==c:
        print("True")
        break
else:
    print("False")

        
        
