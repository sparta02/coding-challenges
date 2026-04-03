import heapq
import sys
n, p, k = map(int, input().split())
lines=[ list(map(int, input().split())) for _ in range(p)]
edges=[ [] for _ in range(n+1)]
for s, e, d in lines:
    edges[s].append((e, d))
    edges[e].append((s, d))

def di(limit):
    INF=10**5
    dist=[INF]*(n+1)
    dist[1]=0

    pq=[]
    heapq.heappush(pq, (0, 1))


    while pq:
        d, curr = heapq.heappop(pq)

        for next_node, w in edges[curr]:
            next_w=d + (1 if w>limit else 0)
            
            if dist[next_node]>next_w:
                dist[next_node]=next_w
                heapq.heappush(pq, (next_w, next_node))
    if dist[n]==INF:
        print(-1)
        sys.exit()
    return dist[n]

left=0
right=1000000
min_idx=1000001

while left<=right:
    mid=(left+right)//2
    # print(mid)
    if di(mid)<=k:
        min_idx=mid
        right=mid-1
    else:
        left=mid+1

print(min_idx)


