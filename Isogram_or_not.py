n=input()
l=""
for i in n:
    if i not in l:
        l+=i
    else:
        print("False")
        break
if l==n:
    print("True")