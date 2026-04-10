n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]


INF=10**9
dist= [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i]=0

for s, e, d in roads:
    dist[s][e]=d

def print_dist():
    for i in range(1, n+1):
        print(*dist[i][1:])

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])

# print_dist()
result=INF
for i in range(1, n+1):
    for j in range(i+1, n+1):
        result=min(result, dist[i][j]+dist[j][i])

print(result)