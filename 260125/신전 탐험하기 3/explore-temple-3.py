n, m = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp= [ [0]*m for _ in range(n) ]

for i in range(m):
    dp[0][i]=cost[0][i]

def print_grid():
    for i in range(n):
        for j in range(m):
            print(dp[i][j], end=" ")
        print()
    print()

for i in range(1, n):
    for j in range(m):
        # 이전 칸과 다른 것만 고려
        for k in range(m):
            if j == k:
                continue
            dp[i][j]=max(dp[i][j], dp[i-1][k]+cost[i][j])

# print_grid()
print(max(dp[-1]))