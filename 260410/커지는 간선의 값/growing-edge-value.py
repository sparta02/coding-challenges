import heapq
n, m, k = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

edges=[[] for _ in range(n+1)]
for s, e , d in temp:
    edges[s].append((e, d))
    edges[e].append((s, d))

pq=[(0, 1)]
visited=[0]*(n+1)

dist=[10**9]*(n+1)
result=0

while pq:
    curr_dist, curr_node=heapq.heappop(pq)

    if visited[curr_node]:
        continue
    
    visited[curr_node]=1
    result+=curr_dist

    for next_node, next_dist in edges[curr_node]:
        if visited[next_node]==0 and dist[next_node]>next_dist:
            dist[next_node]=next_dist
            heapq.heappush(pq, (next_dist, next_node))

# 노드가 총 n개면
# 추가하는 간선은 n-1개
# k * (1+2+3+...n-2)를 더해야 함
result+=k*int((1+n-2)/2*(n-2))
print(result)