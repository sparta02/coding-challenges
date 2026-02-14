n= int(input())

grid= [ list(map(int, input().split())) for _ in range(n)]

# dp[i][j][k]
# i행, j열에서
# k: 가로, 세로, 대각선일 때
# 이동 가능한 방법 수

# k:0 (가로)
# k:1 (세로)
# k:2 (대각선)

dp=[[ [0]*3 for _ in range(n)] for _ in range(n)]

def print_dp():
    print("one")
    for i in range(n):
        for j in range(n):
            print(dp[i][j][0], end=" ")
        print()
    print()
    print("two")
    for i in range(n):
        for j in range(n):
            print(dp[i][j][1], end=" ")
        print()
    print()
    print("three")
    for i in range(n):
        for j in range(n):
            print(dp[i][j][2], end=" ")
        print()
    print()

# 처음 세팅
dp[0][1][0]=1

# # 맨 처음에 오른쪽 아래로 갈 수 있는지
# if grid[0][2]+grid[1][1]+grid[1][2]==0:
#     dp[1][2][2]=1

# 맨 처음에 오른쪽으로 쭉 갈 수 있는지
for i in range(2, n):
    if grid[0][i]==0:
        dp[0][i][0]=1
    else:
        break
# print_dp()

for i in range(1,n):
    for j in range(2, n):
        # print(i, j)
        if grid[i][j]==0:
            # 가로로 오는 경우
            dp[i][j][0]+=dp[i][j-1][0]+dp[i][j-1][2]
            # 세로로 오는 경우
            dp[i][j][1]+=dp[i-1][j][1]+dp[i-1][j][2]
            # 대각선으로 오는 경우
            if i>=1:
                if grid[i-1][j]+grid[i][j-1]==0:
                    dp[i][j][2]+=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

        # print_dp()

print(sum(dp[-1][-1]))