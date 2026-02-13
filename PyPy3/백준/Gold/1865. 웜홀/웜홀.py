import sys

# 빠른 입력을 위해 사용
input = sys.stdin.readline

def bf(n, edges):
    # 모든 노드에서 동시에 시작하는 효과를 주기 위해 0으로 초기화
    # (음수 사이클 존재 여부만 궁금한 것이므로)
    dist = [0] * (n + 1)
    
    for i in range(n):
        for cur, nxt, cost in edges:
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 사이클 존재
                if i == n - 1:
                    return True
    return False

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    
    # 도로 (양방향, 가중치 양수)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    # 웜홀 (단방향, 가중치 음수)
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    if bf(n, edges):
        print("YES")
    else:
        print("NO")