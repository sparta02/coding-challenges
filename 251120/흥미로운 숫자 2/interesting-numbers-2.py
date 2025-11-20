X, Y = map(int, input().split())

# Please write your code here.

def check(x):
    arr=[0]*10
    s=str(x)
    for i in s:
        i=int(i)
        arr[i]+=1
    a=0
    b=0
    for i in arr:
        if i>=2:
            a+=1
        if i==1:
            b+=1
    
    if a==1 and b==1:
        return True
    return False


cnt=0
for i in range(X, Y+1):
    if check(i)==True:
        cnt+=1

print(cnt)