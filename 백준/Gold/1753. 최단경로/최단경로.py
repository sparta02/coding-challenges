import heapq
import sys
INF=999999999

v, e = map(int, input().split())
start_v=int(input())
heap=[]
nodes= [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int, input().split())
    nodes[a].append((b,c))

# for i in range(v+1):
#     print(nodes[i])

dist=[INF]*(v+1)


heapq.heappush(heap,(0, start_v))
dist[start_v]=0

while(heap):
    d, curr=heapq.heappop(heap)

    if dist[curr] <d:
        continue
    # print(f"curr: {curr}, dist: {d}")
    for next_node, w in nodes[curr]:
        # print(f"next node={next_node}")
        next_wei=w+d
        if next_wei<dist[next_node]:
            dist[next_node]=next_wei
            # print(dist)
            heapq.heappush(heap, (next_wei, next_node))


for i in range(1, v+1):
    print('INF' if dist[i]==INF else dist[i])