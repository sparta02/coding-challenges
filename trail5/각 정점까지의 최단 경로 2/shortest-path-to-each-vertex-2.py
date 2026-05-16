n, m = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]

INF=10**9
edges=[[INF]*n for _ in range(n)]

for s, e, d in temp:
    s,e=s-1,e-1
    edges[s][e]=min(edges[s][e], d)
for i in range(n):
    edges[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if edges[i][k]!=INF and edges[k][j]!=INF:
                edges[i][j]=min(edges[i][j], edges[i][k]+edges[k][j])

for i in range(n):
    for j in range(n):
        print(edges[i][j] if edges[i][j]!=INF else -1, end=" ")
    print()
print()