n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp=[ [0]*n for _ in range(n)]

# 각 칸은 (최솟값, 최댓값)

dp[0][0] = (grid[0][0], grid[0][0])

for i in range(1, n):
    min_num=min(dp[0][i-1][0], grid[0][i])
    max_num=max(dp[0][i-1][1], grid[0][i])
    dp[0][i]=(min_num,max_num)

for i in range(1, n):
    min_num=min(dp[i-1][0][0], grid[i][0])
    max_num=max(dp[i-1][0][1], grid[i][0])
    dp[i][0]=(min_num,max_num)

#print(dp)

for i in range(1,n):
    for j in range(1,n):
        min_num_1=min(dp[i-1][j][0],grid[i][j])
        max_num_1=max(dp[i-1][j][1],grid[i][j])
        min_num_2=min(dp[i][j-1][0],grid[i][j])
        max_num_2=max(dp[i][j-1][1],grid[i][j])
        if (max_num_1-min_num_1>max_num_2-min_num_1):
            dp[i][j]=(min_num_2, max_num_2)
        else:
            dp[i][j]=(min_num_1, max_num_1)

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end=" ")
#     print()
# print()

print(dp[n-1][n-1][1]-dp[n-1][n-1][0])