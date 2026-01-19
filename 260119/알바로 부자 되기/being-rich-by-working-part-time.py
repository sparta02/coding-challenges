n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
#dp[i]: i번째 알바를 선택했을 때 벌 수 있는 가장 많은 돈

dp=[0]*n
dp[0]=jobs[0][2]

for i in range(1, n):
    dp[i]=jobs[i][2]
    for j in range(i):
        if dp[j]+jobs[i][2]>dp[i] and jobs[j][1]<jobs[i][0]:
            dp[i]=dp[j]+jobs[i][2]

    #print(dp)
print(max(dp))