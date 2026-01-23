n = int(input())
l, m, r = [], [], []
cost=[]
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)
    cost.append((left,mid,right))

# Please write your code here.

# dp[i][j]
# i층까지 가고
# 현재 j층이라면
# 얻을 수 있는 최대 개수

dp= [[-9999]*3 for _ in range(n)]

dp[0][0]=l[0]
dp[0][1]=m[0]
dp[0][2]=r[0]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j==k:
                continue
            dp[i][j]=max(dp[i][j], dp[i-1][k]+cost[i-1][j])

print(max(dp[-1]))