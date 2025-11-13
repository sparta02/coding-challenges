n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def modify(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]=int(arr[i]/2)

modify(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")