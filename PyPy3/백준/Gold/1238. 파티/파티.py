import heapq
n, m, x = map(int, input().split())
road= [ [] for _ in range(n+1)]
INF=10**9

for _ in range(m):
    start, end, distance= map(int, input().split())
    road[start].append((end, distance))

# 가고 오는데 걸리는 총 시간
time= [0]*(n+1)

def search(start):
    global time
    # 거리 저장을 위한 임시 배열
    dist=[INF]*(n+1)
    dist[start]=0
    heap=[]
    heapq.heappush(heap, (0, start))

    while(heap):
        d,curr=heapq.heappop(heap)
        for next_node, next_dist in road[curr]:
            if d+next_dist<dist[next_node]:
                dist[next_node]=d+next_dist
                heapq.heappush(heap, (dist[next_node], next_node))
    # x점일 경우
    if start==x:
        for i in range(1, n+1):
            if i==x:
                continue
            else:
                time[i]+=dist[i]
    # 아닌 경우
    else:
        time[start]+=dist[x]




# 가는데 걸리는 시간 계산
for start in range(1, n+1):
    search(start)

print(max(time))
