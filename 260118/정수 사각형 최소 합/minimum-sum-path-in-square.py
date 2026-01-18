n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp=[[0]*n for _ in range(n)]

dp[0][n-1] = grid[0][n-1]
for i in range(n-2, -1, -1):
    dp[0][i]=dp[0][i+1]+grid[0][i]

for i in range(1, n):
    dp[i][n-1]=dp[i-1][n-1]+grid[i][n-1]

for x in range(1, n):
    for y in range(n-2, -1, -1):
        print(x, y)
        dp[x][y]=min(grid[x][y]+dp[x-1][y], grid[x][y]+dp[x][y+1])

print(dp[n-1][0])