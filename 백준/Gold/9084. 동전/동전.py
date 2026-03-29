import sys
input = sys.stdin.readline

t=int(input())

for _ in range(t):
    n =int(input())
    coins=list(map(int, input().split()))
    target=int(input())
    
    # dp[i][j]
    # i번째 동전까지 고려했을 때
    # j원을 만드는데 가능한 경우의 수
    dp= [[0]*(target+1) for _ in range(n)]
    for i in range(n):
        dp[i][0]=1
    for i in range(coins[0], target+1, coins[0]):
        dp[0][i]=1
    for i in range(1, n):
        for j in range(target+1):
            dp[i][j]=dp[i-1][j]
            if j>=coins[i]:
                dp[i][j]+=(dp[i][j-coins[i]])
    print(dp[-1][-1])