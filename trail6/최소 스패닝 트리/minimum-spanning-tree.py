n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]



edges.sort(key=lambda x:(x[2]))
parent=[ i for i in range(n+1)]

def find(x):
    if parent[x] !=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

result=0

for s, e, d in edges:
    if find(s)!=find(e):
        result+=d
        union(s, e)

print(result)