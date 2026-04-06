n = int(input())
dist=[0]
for _ in range(n):
    dist.append([0]+list(map(int, input().split())))

# dp=[1<<n][n]
# 비트가 1인 곳들을 모두 방문하고
# 현재 위치가 n일 때 최소거리

INF=99999999
dp = [[INF]*(n+1) for _ in range(1<<n)]

def print_dp():
    print(' '*n, end="")
    print(*range(1,n+1))
    for i in range(1<<n):
        print(bin(i), end=" ")
        print(*dp[i][1:])

dp[1][1]=0

for i in range(1<<n):
    for j in range(1, n+1):
        
        # 현재 위치 방문 불가하면 skip
        if dp[i][j]==INF:
            continue
        # # 비트 오류면 skip
        # if not(i&(1<<(j-1))):
        #     continue
        for k in range(1, n+1):
            # 이미 방문했으면 skip
            if i&(1<<(k-1)):
                # print('이미 방문함')
                continue
            # 현재 위치에서 다음 위치로 이동 못하면 skip
            if dist[j][k]==0:
                # print('이동 못함')
                continue
            # print(bin(i), j, k)
            next=i|(1<<(k-1))
            dp[next][k]=min(dp[next][k], dp[i][j]+dist[j][k])
            
for i in range(1, n+1):
    if dist[i][1]==0:
        dp[-1][i]=INF
    dp[-1][i]+=dist[i][1]

# print_dp()
print(min(dp[-1]))
