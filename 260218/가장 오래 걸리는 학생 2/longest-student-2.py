import heapq
n, m = map(int, input().split())
edges=[[] for _ in range(n+1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    edges[e].append((s,d))

# print(edges)

INF=10**6
dist=[INF]*(n+1)
dist[n]=0
pq=[]

heapq.heappush(pq, (0, n))

while pq:
    curr_dist, curr_node= heapq.heappop(pq)

    if dist[curr_node]<curr_dist:
        continue
    for next_node, next_weight in edges[curr_node]:
        weight=curr_dist+next_weight

        if dist[next_node]>weight:
            dist[next_node]=weight
            heapq.heappush(pq, (weight, next_node))
print(max(dist[1:]))
