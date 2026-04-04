import sys
input=sys.stdin.readline

n, m, start, end = map(int, input().split())
roads=[ list(map(int, input().split())) for _ in range(m)]

q=int(input())
new_plan=[ list(map(int, input().split())) for _ in range(q)]


INF=10**20
dist=[ [INF]*(n+1) for _ in range(n+1)]

for s,e,d in roads:
    dist[s][e]=min(dist[s][e], d)

for i in range(n+1):
    dist[i][i]=0

def print_dist(dist):
    for i in range(1, n+1):
        print(*dist[i][1:])

# print_dist(dist)
# print()

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

# print_dist(dist)
# print()
# 1~3 + 3~5 + 5~7

for i in range(q):
    s1,e1,d1,s2,e2,d2=new_plan[i]
    temp=INF
    temp=min(INF, dist[start][end], dist[start][s1]+d1+dist[e1][end], dist[start][s2]+d2+dist[e2][end], dist[start][s1]+d1+dist[e1][s2]+d2+dist[e2][end], dist[start][s2]+d2+dist[e2][s1]+d1+dist[e1][end])

    # print(dist[start][end])
    # print(f"{dist[start][s1]+d1+dist[e1][end]}, {dist[start][s1]}+{d1}+{dist[e1][end]}")
    # print(f"{dist[start][s2]+d2+dist[e2][end]},{dist[start][s2]}+{d2}+{dist[e2][end]}")
    # print(f"{dist[start][s1]+d1+dist[e1][s2]+d2+dist[e2][end]},{dist[start][s1]}+{d1}+{dist[e1][s2]}+{d2}+{dist[e2][end]}")
    if temp>=INF:
        print(-1)
    else:
        print(temp)
