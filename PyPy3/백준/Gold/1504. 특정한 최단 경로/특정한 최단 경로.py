import heapq

n, e = map(int, input().split())

edges= [[] for _ in range(n+1)]

for _ in range(e):
    start, end, dist= map(int, input().split())
    edges[start].append((end, dist))
    edges[end].append((start, dist))

A, B = map(int, input().split())

# 1 -> A -> B -> N
# 1 -> B -> A -> N

# 최종 결과를 저장할 변수
result1=0
result2=0

INF = 10**10

# start -> end까지 최소거리를 반환하는 함수
def calc_min_dist(start, end):
    # dist를 저장할 배열

    dist=[INF]*(n+1)

    # 우선순위 큐
    pq=[]

    # 시작점 세팅
    dist[start]=0
    heapq.heappush(pq, (0, start))

    while pq:
        curr_dist, curr_node=heapq.heappop(pq)

        if dist[curr_node]<curr_dist:
            continue

        for next_node, next_dist in edges[curr_node]:
            #현재까지 거리 + 다음 노드까지 거리
            weight=curr_dist+next_dist

            # 현재 노드를 경유해서 가는게 빠르다면
            # 갱신 후 우선순위 큐에 넣기
            if dist[next_node]>weight:
                dist[next_node]=weight
                heapq.heappush(pq, (weight, next_node))

    #print(dist)
    return dist[end]


result1+=calc_min_dist(1, A)
result1+=calc_min_dist(A, B)
result1+=calc_min_dist(B, n)

result2+=calc_min_dist(1, B)
result2+=calc_min_dist(B, A)
result2+=calc_min_dist(A, n)

result= min(result1, result2)
print(result if result<INF else -1)