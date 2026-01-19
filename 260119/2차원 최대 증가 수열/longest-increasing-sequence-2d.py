n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp=[ [1]*m for _ in range(n)]
for i in range(1, n):
    grid[i][0]=99999
    grid[0][i]=99999

for x in range(1, n):
    for y in range (1, m):

        for i in range(x):
            for j in range(y):
                if grid[i][j]<grid[x][y] and dp[i][j]+1>dp[x][y]:
                    dp[x][y]=dp[i][j]+1

# for i in range(n):
#     for j in range(m):
#         print(dp[i][j], end=" ")
#     print()
# print()

result=0
for i in range(n):
    for j in range(m):
        result=max(result, dp[i][j])