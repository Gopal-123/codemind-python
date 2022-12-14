
n=int(input())
s=str(n)
l=[]
for i in s:
    if i not in l:
        l.append(i)
if len(l)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")
