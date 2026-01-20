n, m = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
dp=[999999]*(m+1)
dp[0]=0

for i in range(1, m+1):
    for cost in coin:
        # i원을 만들고 싶을 때
        # cost 동전을 사용
        if dp[i-cost]==999999:
            continue
        dp[i]=min(dp[i-cost]+1, dp[i])

if dp[-1]==999999:
    print(-1)
else:
    print(dp[-1])
        