import heapq
n, m = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]

edges=[ [] for _ in range(n+1)]

for s, e, d in temp:
    edges[s].append((e, d))
    edges[e].append((s, d))

pq=[(0, 1)]
visited=[0]*(n+1)
INF=10**9
dist=[INF]*(n+1)
dist[1]=0
result=0

while pq:
    curr_dist, curr_node=heapq.heappop(pq)

    if visited[curr_node]==1:
        continue
    # print(curr_node, curr_dist)
    visited[curr_node]=1
    result+=curr_dist

    for next_node, next_dist in edges[curr_node]:
        if visited[next_node]==0 and dist[next_node]>next_dist:
            dist[next_node]=next_dist
            heapq.heappush(pq, (next_dist, next_node))

print(result)
        