import heapq
n, m = map(int, input().split())
temp= [tuple(map(int, input().split())) for _ in range(m)]

edges=[[] for _ in range(n+1)]

for s, e, d in temp:
    edges[s].append((e, d))

# Please write your code here.
INF=10**6
dist=[INF]*(n+1)
dist[1]=0

pq=[]
heapq.heappush(pq, (1,0))

while pq:
    curr, curr_dist=heapq.heappop(pq)

    if dist[curr]<curr_dist:
        continue
    
    for next, next_dist in edges[curr]:
        w=curr_dist+next_dist
        if dist[next]>w:
            dist[next]=w
            heapq.heappush(pq, (next,w))

for num in dist[2:]:
    print(num if num!=INF else -1)
