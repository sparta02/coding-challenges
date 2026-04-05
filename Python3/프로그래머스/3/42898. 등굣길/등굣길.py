def print_dp(dp):
    for i in range(len(dp)):
        print(*dp[i])

def solution(m, n, puddles):
    answer = 0
    grid=[ [0]*m for _ in range(n)]
    for x, y in puddles:
        grid[y-1][x-1]=1
    
    dp =[ [0]*m for _ in range(n)]
    dp[0][0]=1
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                # 아래로 이동 가능한 경우
                if i>0:
                    dp[i][j]=(dp[i][j]+dp[i-1][j])%1000000007
                # 오른쪽으로 이동 가능한 경우
                if j>0:
                    dp[i][j]=(dp[i][j]+dp[i][j-1])%1000000007
    return dp[-1][-1]%1000000007