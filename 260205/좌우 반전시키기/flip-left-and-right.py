n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def change(num):
    for i in range(num-1, num+2):
        if 0<=i<n:
            if arr[i]==0:
                arr[i]=1
            else:
                arr[i]=0

result=0
for i in range(n-1):
    if arr[i]==0:
        change(i+1)
        result+=1
    #print(arr)
if 0 in arr:
    print(-1)
else:
    print(result)