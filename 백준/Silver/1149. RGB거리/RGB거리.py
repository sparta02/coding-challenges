n=int(input())

arr=[]

for _ in range(n):
    a,b,c=list(map(int, input().split()))
    arr.append([a,b,c])

# i번째 집에서
# j번째 색을 골랐을 때
# 최소 비용
dp=[ [99999999999]*3 for _ in range(n)]

dp[0][0]=arr[0][0]
dp[0][1]=arr[0][1]
dp[0][2]=arr[0][2]

# i번째 집에서
for i in range(1, n):
    # j번째 색을 골랐을 때
    for j in range(3):
        # 이전 k번째 색과 달라야 함
        for k in range(3):

            if j==k:
                continue
            dp[i][j]=min(dp[i][j], dp[i-1][k]+arr[i][j])

print(min(dp[-1]))