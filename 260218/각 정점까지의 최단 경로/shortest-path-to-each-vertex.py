import heapq
n, m = map(int, input().split())
start_node = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    edges[s].append((e, d))
    edges[e].append((s, d))
    
# print(edges)    

# 거리를 저장할 배열
INF = 10**6
dist= [INF]*(n+1)

# 우선순위 큐
pq=[]

# 시작점 세팅
dist[start_node]=0
heapq.heappush(pq, (0, start_node))

while pq:
    curr_dist, curr_node=heapq.heappop(pq)

    if dist[curr_node]>curr_dist:
        continue

    # 현재 노드와 연결된 모든 노드에 대해
    for next_node, w in edges[curr_node]:
        next_w=curr_dist+w

        # 현재 노드를 경유해서 가는 게 더 짧다면
        if dist[next_node]>next_w:
            dist[next_node]=next_w
            heapq.heappush(pq, (next_w, next_node))

# print(dist)

for num in dist[1:]:
    if num==INF:
        print(-1)
    else:
        print(num)