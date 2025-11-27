n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n-1):
    min=i
    for j in range(i, n):
        if arr[min]>arr[j]:
            min=j
    arr[i], arr[min]=arr[min], arr[i]


for i in arr:
    print(i, end=" ")