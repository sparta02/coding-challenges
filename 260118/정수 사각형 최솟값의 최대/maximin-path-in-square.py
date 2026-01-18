n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# dp: 각 칸에서 자신을 포함해 밟을 수 있는 가장 최솟값

dp=[[0]*n for _ in range(n)]

dp[0][0]=9
dp[0][1] = grid[0][1]
dp[1][0] = grid[1][0]

for i in range(1, n):
    dp[0][i]=min(dp[0][i-1], grid[0][i])

for i in range(1, n):
    dp[i][0]=min(dp[i-1][0], grid[i][0])
print(dp)

for x in range(1, n):
    for y in range(1, n):
        dp[x][y]=min(max(dp[x-1][y], dp[x][y-1]),grid[x][y])


# for x in range(n):
#     for y in range(n):
#         print(dp[x][y], end=" ")
#     print()
# print()

print(dp[n-1][n-1])