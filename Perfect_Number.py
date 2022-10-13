def perfect(k):
    s=0
    for i in range(1,k):
        if i==k:
            return False
        if k%i==0:
            s=s+i
    if s==k:
        return True
    return False    
            
    

n=int(input())
if perfect(n):
        print("True")
else:
    print("False")
        