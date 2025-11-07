arr=[0]*10
a,b=map(int, input().split())
arr[0]=a
arr[1]=b

for i in range(2,10):
    arr[i]=(arr[i-2]+arr[i-1])%10

for i in arr:
    print(i, end=" ")