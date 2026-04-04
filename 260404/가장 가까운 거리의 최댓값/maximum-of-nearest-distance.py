import heapq

n, m = map(int, input().split())
a, b, c = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]
edges=[[] for _ in range(n+1)]

for s, e, d in temp:
    edges[s].append((e, d))
    edges[e].append((s, d))
    
# print(edges)

min_dist=[10**6]*(n+1)


def di(start):
    INF=10**6
    dist=[INF]*(n+1)
    dist[start]=0
    pq=[]
    heapq.heappush(pq, (0, start))

    while pq:
        curr_dist, curr_node=heapq.heappop(pq)

        for next_node, d in edges[curr_node]:
            w=d+curr_dist
            if dist[next_node]>w:
                dist[next_node]=w
                heapq.heappush(pq, (w, next_node))
    # print(dist)
    for i in range(1, n+1):
        min_dist[i]=min(min_dist[i], dist[i])
di(a)
di(b)
di(c)
print(max(min_dist[1:]))