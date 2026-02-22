import heapq
n, m, r=map(int, input().split())

items=[0]+list(map(int, input().split()))
edges=[ [] for _ in range(n+1)]
for _ in range(r):
    s, e, d = map(int, input().split())
    edges[s].append((e,d))
    edges[e].append((s,d))

# 각 지점별 아이템 개수를 저장하는 리스트
result_list=[-1]*(n+1)


def dy(start):
    # 시작점에서 획득 가능한 item 값
    item_value=0

    INF = 10**6
    # 각 지점별 최단거리를 저장하는 배열
    dist= [INF]*(n+1)

    # 우선순위 큐
    pq=[]

    # 시작점 세팅
    dist[start]=0
    heapq.heappush(pq, (0, start))

    while pq:
        curr_dist, curr_node=heapq.heappop(pq)

        if dist[curr_node]<curr_dist:
            continue
        # 수색 범위 이내라면 추가
        if curr_dist<=m:
            # print(f"add {curr_node}")
            item_value+=items[curr_node]

        

        for next_node, next_dist in edges[curr_node]:
            w=curr_dist+next_dist
            if dist[next_node]>w:
                dist[next_node]=w
                heapq.heappush(pq, (w, next_node))
    return item_value
    


for i in range(1,n+1):
    # 다익스트라를 통해 지점 방문
    #print(f"node {i}")
    result_list[i]=dy(i)
    #print(result_list[i])

print(max(result_list))

