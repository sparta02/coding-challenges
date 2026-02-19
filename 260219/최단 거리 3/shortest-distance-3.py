import heapq

n, m = map(int, input().split())
edges = [ [] for _ in range(n+1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    edges[s].append((e, d))
    edges[e].append((s, d))
# print(edges)

A, B = map(int, input().split())

# 최종 거리 저장할 배열
INF=10**6
dist=[INF]*(n+1)

# 우선순위 큐
pq=[]

#시작점 세팅
dist[A]=0
heapq.heappush(pq, (0, A))

while pq:
    curr_dist, curr_node=heapq.heappop(pq)

    if dist[curr_node]<curr_dist:
        continue

    for next_node, next_dist in edges[curr_node]:
        w=curr_dist+next_dist

        if dist[next_node]>w:
            dist[next_node]=w
            heapq.heappush(pq, (w, next_node))

print(dist[B])