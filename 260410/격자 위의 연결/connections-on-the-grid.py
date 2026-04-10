import heapq
n, m = map(int, input().split())

horizontal = [list(map(int, input().split())) for _ in range(n)]
vertical = [list(map(int, input().split())) for _ in range(n - 1)]

# 1. (가중치, 노드1, 노드2) 순으로 만들어 최소 heap에 추가
# 2. 가중치가 작은 간선부터 확인하며 cycle이 생기는지 체크
#   2-1) n*m-1개의 간선이 추가되었다면 종료

pq=[]
for i in range(n):
    for j in range(m-1):
        heapq.heappush(pq, (horizontal[i][j], i*m+j, i*m+j+1))

for i in range(n-1):
    for j in range(m):
        heapq.heappush(pq, (vertical[i][j], i*n+j, (i+1)*n+j))

parent=[ i for i in range(n*m+1)]
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

result=0
while pq:
    dist, s, e = heapq.heappop(pq)
    if find(s)!=find(e):
        union(s, e)
        result+=dist

print(result)