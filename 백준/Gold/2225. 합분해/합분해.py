n, k = map(int, input().split())
result=0

#dp[i][j]
dp= [[0]*(n+1) for _ in range(k)]

for i in range(n+1):
    dp[0][i]=1

def print_dp():
    for i in range(k):
        print(*dp[i])

for i in range(1, k):
    for j in range(n+1):
        dp[i][j]=sum(dp[i-1][:j+1])%1000000000

# print_dp()

print(dp[-1][-1])