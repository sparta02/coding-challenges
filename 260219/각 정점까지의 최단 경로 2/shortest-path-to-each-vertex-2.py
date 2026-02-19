n, m = map(int, input().split())

INF = 10**9
dist=[ [INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    dist[s][e]= min(dist[s][e], d)

for i in range(n+1):
    dist[i][i]=0

# Please write your code here.

def print_dist():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j]!=INF:
                print(dist[i][j], end=" ")
            else:
                print(-1, end=" ")
        print()
    print()


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])

print_dist()