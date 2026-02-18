import heapq
INF=10**6
n, m = map(int, input().split())
edges = [[] for _ in range(n+1)] 
for _ in range(m):
    s, e, d=map(int, input().split())
    edges[s].append((e, d))

pq=[]
dist=[INF]*(n+1)

heapq.heappush(pq, (0, 1))
dist[1]=0

while(pq):
    curr_dist, curr_node = heapq.heappop(pq)

    if dist[curr_node]<curr_dist:
        continue

    for next_node, next_dist in edges[curr_node]:
        if dist[next_node]>curr_dist+next_dist:
            dist[next_node]=curr_dist+next_dist
            heapq.heappush(pq, (curr_dist+next_dist, next_node))

# print(edges)
# print(dist)

for i in dist[2:]:
    if i==INF:
        print(-1)
    else:
        print(i)
