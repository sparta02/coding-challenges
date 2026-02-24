import heapq
n=int(input())
m=int(input())
edges= [ [] for _ in range(n+1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    edges[s].append((e,d))

start, end= map(int, input().split())

# 특정 노드를 방문하기 직전 노드 저장하는 배열
route=[0]*(n+1)

# 시작점에서 각 노드까지 최단거리 저장하는 배열
INF=10**9
dist= [INF]*(n+1)

pq=[]

# 시작점 세팅
heapq.heappush(pq, (0, start))
dist[start]=0

while pq:
    curr_dist, curr_node=heapq.heappop(pq)

    if dist[curr_node]<curr_dist:
        continue
    
    for next_node, next_dist in edges[curr_node]:
        w= curr_dist+next_dist
        if dist[next_node]>w:
            dist[next_node]=w
            route[next_node]=curr_node
            heapq.heappush(pq, (w, next_node))

# print(dist)
# print(route)
result_route=[end]
curr=end
while(start!=curr):
    curr=route[curr]
    result_route.append(curr)
print(dist[end])
print(len(result_route))
print(*result_route[::-1])
