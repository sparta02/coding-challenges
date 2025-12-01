n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
# 2 5 7 9 10 15
result=9999999999999999999999
for i in range(n):
    result=min(result, arr[n+i]-arr[i])

print(result)