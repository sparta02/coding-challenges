n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def modify(arr):
    for i in range(len(arr)):
        arr[i]= abs(arr[i])

modify(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")