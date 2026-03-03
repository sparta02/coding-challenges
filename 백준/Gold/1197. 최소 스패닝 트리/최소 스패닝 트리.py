import sys
sys.setrecursionlimit(10000)

v, e = map(int, input().split())
edges=[list(map(int, input().split())) for _ in range(e)]

edges.sort(key=lambda x: x[2])

parent=[ i for i in range(v+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

result=0
for s, e, d in edges:
    if find(s) !=find(e):
        result+=d
        union(s, e)

print(result)