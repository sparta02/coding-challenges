import heapq

# 노드 개수 n, 간선 개수 m 입력
n, m = map(int, input().split())

# 인접 리스트
# edges[x] = (x와 연결된 노드, 간선 가중치)
edges = [[] for _ in range(n + 1)]

# 간선 정보 입력 (무방향 그래프)
for _ in range(m):
    s, e, d = map(int, input().split())
    edges[s].append((e, d))
    edges[e].append((s, d))

# 시작점 A, 도착점 B
A, B = map(int, input().split())

# 우선순위 큐 (다익스트라용)
pq = []

# 충분히 큰 값 (최단거리 초기화용)
INF = 10**15

# dist[x] : x번 노드에서 도착점 B까지의 최단거리
dist = [INF] * (n + 1)

# 도착점 B의 최단거리는 0
dist[B] = 0

# (현재까지 거리, 노드 번호) 형태로 PQ에 삽입
heapq.heappush(pq, (0, B))

# -------------------------------
# 다익스트라 알고리즘 시작
# (도착점 B를 시작점으로)
# -------------------------------
while pq:
    curr_dist, curr_node = heapq.heappop(pq)

    # 이미 더 짧은 거리로 방문한 적이 있다면 무시
    if dist[curr_node] < curr_dist:
        continue

    # 현재 노드와 연결된 모든 간선 확인
    for next_node, next_dist in edges[curr_node]:
        # curr_node → next_node로 이동했을 때의 거리
        weight = curr_dist + next_dist

        # 더 짧은 거리라면 갱신
        if dist[next_node] > weight:
            dist[next_node] = weight
            heapq.heappush(pq, (weight, next_node))

# ---------------------------------
# 사전순으로 가장 앞선 최단경로 출력
# ---------------------------------

# 현재 위치를 시작점 A로 설정
curr = A

# 시작점 출력
print(curr, end=" ")

# 도착점 B에 도달할 때까지 반복
while curr != B:
    # 현재 위치에서 최단경로로 갈 수 있는 후보 노드들
    candidates = []

    # curr와 연결된 모든 간선 확인
    for next_node, next_dist in edges[curr]:
        # dist 조건을 만족하면
        # 실제로 최단거리 경로 위에 있는 간선
        if dist[next_node] + next_dist == dist[curr]:
            candidates.append(next_node)

    # 후보 중 정점 번호가 가장 작은 노드 선택
    # → 사전순으로 가장 앞선 경로 보장
    curr = min(candidates)

    # 선택된 노드 출력
    print(curr, end=" ")