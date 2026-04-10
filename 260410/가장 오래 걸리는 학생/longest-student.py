import heapq

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

edges=[ [] for _ in range(n+1)]

for s, e, d in roads:
    edges[s].append((e, d))
    edges[e].append((s, d))

# 학교 n에서 시작해서 각 지점에 도착하는 데 걸리는 최단거리
INF = 10**9
dist=[INF]*(n+1)
dist[n]=0
pq=[]
heapq.heappush(pq, ((0, n)))

while pq:
    curr_dist, curr_node = heapq.heappop(pq)

    if dist[curr_node]< curr_dist:
        continue

    for next_node, weight in edges[curr_node]:
        total_weight=curr_dist+weight
        if dist[next_node]>total_weight:
            dist[next_node]=total_weight
            heapq.heappush(pq, (total_weight, next_node))

print(max(dist[1:]))