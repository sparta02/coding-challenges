import sys
import heapq
input = sys.stdin.readline

V = int(input())
edges = [[] for _ in range(V + 1)]

# 입력 처리
for _ in range(V):
    data = list(map(int, input().split()))
    u = data[0]
    i = 1
    while data[i] != -1:
        v = data[i]
        w = data[i + 1]
        edges[u].append((v, w))
        i += 2


def dijkstra(start):
    INF = 10**15
    dist = [INF] * (V + 1)
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        cur_dist, cur = heapq.heappop(pq)

        if dist[cur] < cur_dist:
            continue

        for nxt, w in edges[cur]:
            nd = cur_dist + w
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return dist


# 1번에서 가장 먼 정점 찾기
dist1 = dijkstra(1)
start = max(range(1, V + 1), key=lambda x: dist1[x])

# 해당 정점에서 다시 다익스트라
dist2 = dijkstra(start)

# 지름 출력
print(max(dist2[1:]))