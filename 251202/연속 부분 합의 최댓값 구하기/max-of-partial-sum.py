n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
DP=[0]*n
DP[0]=arr[0]

for i in range(1, n):
    DP[i] = max(DP[i-1]+arr[i], arr[i])

print(max(DP))