n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(len(arr)):
    print(f"i는 {i}, arr[i]는 {arr[i]}")
    if arr[i]%2==0:
        print(arr[int(i/2)], end=" ")