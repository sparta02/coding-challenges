n=int(input())
cost= [ list(map(int, input().split())) for _ in range(n)]


# dp[i][j][k]
# i번째 라인에서
# j번째 색을 선택하고
# 맨 처음 k번째 색을 선택했을 때
# 비용의 최솟값
INF=10**9
dp= [[[INF]*3 for _ in range(3)] for _ in range(n)]

def print_dp():
    for i in range(n):
        for j in range(3):
            print(dp[i][j], end=" ")
        print()
    print()

dp[0][0][0]=cost[0][0]
dp[0][1][1]=cost[0][1]
dp[0][2][2]=cost[0][2]

for i in range(1, n-1):
    for j in range(3):
        for k in range(3):
            # j가 다르고 k는 같아야함
            dp[i][j][k]=min(INF if dp[i-1][(j+1)%3][k]==INF else dp[i-1][(j+1)%3][k]+cost[i][j], INF if dp[i-1][(j+2)%3][k]==INF else dp[i-1][(j+2)%3][k]+cost[i][j])

for j in range(3):
    for j_2 in range(3):
        for k_2 in range(3):
        # j와 j_2, j와 k_2도 달라야 함
            if j==j_2 or j==k_2:
                continue
            dp[-1][j][0]=min(dp[-1][j][0], dp[-2][j_2][k_2]+cost[-1][j])


# print_dp()
print(min([ x[0] for x in dp[-1]]))