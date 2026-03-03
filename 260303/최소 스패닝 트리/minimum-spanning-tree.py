import heapq
n, m = map(int, input().split())
edges = []

for _ in range(m):
    s, e, d = map(int, input().split())
    heapq.heappush(edges, (d,s,e))

parent=[ i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    A=find(a)
    B=find(b)
    parent[A]=B


result=0
temp=n-1
while temp:
    dist, start, end = heapq.heappop(edges)
    if find(start)==find(end):
        continue
    
    union(start, end)
    result+=dist
    temp-=1

print(result)