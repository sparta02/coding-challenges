import heapq
from collections import deque

n, m, a, b=map(int, input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
edges=[ [] for _ in range(n+1)]

for s, e, d in arr:
    edges[s].append((e,d))
    edges[e].append((s,d))

INF=10**20
dist=[INF]*(n+1)
dist[a]=0

pq=[]
heapq.heappush(pq, (0, a))

while pq:
    curr_dist, curr_node=heapq.heappop(pq)

    if dist[curr_node]<curr_dist:
        continue
    
    for next_node, d in edges[curr_node]:
        w=d+curr_dist
        if dist[next_node]>w:
            dist[next_node]=w
            heapq.heappush(pq, (w, next_node))

# print(dist[1:])

queue=deque()
queue.append(b)
visited=[0]*(n+1)
visited[b]=1

while queue:
    curr=queue.popleft()
    
    for next, d in edges[curr]:
        if dist[curr]==dist[next]+d and visited[next]==0:
            visited[next]=1
            queue.append(next)

print(sum(visited))
for i in range(1, n+1):
    if visited[i]:
        print(i, end=" ")

