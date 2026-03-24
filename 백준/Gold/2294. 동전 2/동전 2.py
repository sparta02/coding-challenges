n, k = map(int, input().split())
coins= [int(input()) for _ in range(n)]

coins=list(set(coins))
coins.sort()
n=len(coins)
# print(coins)

INF=9999999999
dp= [ [INF]*(k+1) for _ in range(n)]

def print_dp():
    for i in range(n):
        print(*dp[i])

for i in range(1, k+1):
    if i%coins[0]==0:
        dp[0][i]=i//coins[0]
for i in range(n):
    dp[i][0]=0

for i in range(1, n):
    for j in range(1, k+1):
        dp[i][j]=min(dp[i][j], dp[i-1][j])
        if j>=coins[i]:
            dp[i][j]=min(dp[i][j], dp[i][j-coins[i]]+1)
            # if dp[i-1][j-coins[i]]!=INF:
            #     dp[i][j]=min(dp[i][j], dp[i-1][j-coins[i]]+1)

# print_dp()
print(dp[-1][-1] if dp[-1][-1] !=INF else -1)