import heapq
n, m = map(int, input().split())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, d= map(int, input().split())
    edges[s].append((e, d))
    edges[e].append((s, d))

start, end = map(int, input().split())

# 거리 저장하는 배열
INF=10**6
dist= [INF]*(n+1)
# 경로를 저장하는 배열
route= [-1]*(n+1)
# 우선순위큐
pq=[]

# 시작점 세팅
dist[start]=0
heapq.heappush(pq, (0, start))

while pq:
    curr_dist, curr_node = heapq.heappop(pq)

    if dist[curr_node]<curr_dist:
        continue

    for next_node, next_dist in edges[curr_node]:
        weight=next_dist+curr_dist
        if dist[next_node]>weight:
            route[next_node]=curr_node
            dist[next_node]=weight
            heapq.heappush(pq, (weight, next_node))

print(dist[end])
# print(route[1:])
result_route=[end]

curr=end
while curr!=start:
    result_route.append(route[curr])
    curr=route[curr]

for n in result_route[::-1]:
    print(n, end=" ")
