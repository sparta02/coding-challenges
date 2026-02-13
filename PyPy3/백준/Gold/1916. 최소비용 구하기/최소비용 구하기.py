import heapq
INF=10**9

n=int(input())
m=int(input())

roads=[ [] for _ in range(n+1)]

for _ in range(m):
    s, e, d= map(int, input().split())
    roads[s].append((e, d))

start, end = map(int, input().split())

dist=[INF]*(n+1)
dist[start]=0
heap=[]
heapq.heappush(heap, (0, start))


while(heap):
    d, curr=heapq.heappop(heap)
    if d>dist[curr]:
        continue
    for next_node, next_dist in roads[curr]:
        if dist[next_node]>dist[curr]+next_dist:
            dist[next_node]=dist[curr]+next_dist
            heapq.heappush(heap, (dist[next_node], next_node))
# print(dist)
print(dist[end])