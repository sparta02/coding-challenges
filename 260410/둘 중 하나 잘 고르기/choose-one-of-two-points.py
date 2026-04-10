n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# dp[2n][n]
# 총 i개만큼 고르고
# 빨간색을 j개 골랐을 때 최대값
INF=-9999
dp= [[INF]*(n+1) for _ in range(2*n)]

def print_dp():
    for i in range(2*n):
        print(*dp[i])

dp[0][0]=blue[0]
dp[0][1]=red[0]

for i in range(2*n-1):
    for j in range(n+1):
        if dp[i][j]!=INF:
        # 파란색 하나만 걍 뽑았을 때 유지
            dp[i+1][j]=max(dp[i+1][j], dp[i][j]+blue[i+1])
            # 빨간색을 하나 더 뽑을 수 있다면
            if j<n:
                dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j]+red[i+1])

# print_dp()
print(dp[-1][-1])