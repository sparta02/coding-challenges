n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

INF=10**9
dp= [ [INF]*n for _ in range(1<<n)]
dp[1][0]=0

for i in range(1<<n):
    for curr in range(n):
        # i: 비트
        # j: 마지막 위치

        # Case 1. 마지막 위치가 비트에 포함되지 않는 경우 Pass
        if (i & 1<<curr ==0):
            continue
        # print(bin(i), curr)
        # Case 2. 현재까지 오는 방법이 없었으면 Skip
        if dp[i][curr]==INF:
            continue
        
        for next in range(n):
            # Case 3. curr -> next 이동이 불가능하면 skip
            if dist[curr][next]==0:
                continue
            # Case 4. 이마 next 지점을 방문했다면 skip
            if (i) & (1<<next) !=0:
                continue
            dp[i | (1<<next)][next] = min(dp[i | (1<<next)][next], dp[i][curr]+dist[curr][next])
for i in range(n):
    if dist[i][0]==0:
        dp[-1][i]=INF
    else:
        dp[-1][i]+=dist[i][0]
print(min(dp[-1]))