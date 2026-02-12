n, k = map(int, input().split())
items=[]

for _ in range(n):
    a, b=map(int, input().split())
    items.append([a, b])

items.sort()

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(dp[i][j], end=" ")
        print()
    print()

# dp[n][k]
# n번째 아이템까지 고려하고
# 무게 k까지 고려했을 때
# 최대 가치

dp=[[0]*(k+1) for _ in range(n)]

for j in range(k+1):
    if items[0][0]<=j:
        dp[0][j]=items[0][1]

for i in range(1, n):
    for j in range(k+1):
        w=items[i][0]
        v=items[i][1]
        # 안 담는 경우
        dp[i][j]=max(dp[i][j], dp[i-1][j])
        if j>=w:
            # 이번 아이템을 담는 경우
            dp[i][j]=max(dp[i][j], dp[i-1][j-w]+v)
            
print(max(dp[-1]))




# print_grid(dp)