N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
dp=[-1]*(M+1)
dp[0]=0

for cost in coin:
    for i in range(1, M+1):
        if cost>i:
            continue
        if dp[i-cost]==-1:
            continue
        dp[i]=max(dp[i],dp[i-cost]+1)
    #print(dp)

print(dp[-1])