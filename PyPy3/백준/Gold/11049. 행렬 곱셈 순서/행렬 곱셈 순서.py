import sys

n= int(input())

matrix= [list(map(int, input().split())) for _ in range(n)]


if n==1:
    print(0)
    sys.exit()

# dp[i][j]
# i번째 행렬~j번째 행렬까지 고려했을 때
INF=10**15
dp = [[INF]*(n) for _ in range(n)]

for i in range(n-1):
    temp=matrix[i][0]*matrix[i][1]*matrix[i+1][1]
    dp[i][i+1]=temp

for i in range(n):
    dp[i][i]=0

def print_dp():
    for i in range(n):
        print(*dp[i])

for i in range(2, n):
    for j in range(n-i):
        x=j
        y=j+i
        # print(x,y)
        for k in range(x, y):
            # print(x, k, k+1, y)
            temp=dp[x][k]+dp[k+1][y]+matrix[x][0]*matrix[k][1]*matrix[y][1]
            dp[x][y]=min(dp[x][y],temp)

# 0~2
# 0~0 1~2
# 0~1 2~2

# 1~3
# 1~1 2~3
# 1~2 3~3

# 2~4
# 2~2 3~4
# 2~3 4~4
#================
# 0~3
# 0~0 1~3
# 0~1 2~3
# 0~2 3~3

# 1~4
# 1~1 2~4
# 1~2 3~4
# 1~3 4~4
#================
# 0~4
# 0~0 1~4
# 0~1 2~4
# 0~2 3~4
# 0~3 4~4
print(dp[0][-1])
# print_dp()

