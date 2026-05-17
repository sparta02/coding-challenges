n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

parent= [ i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

for q, a, b in query:
    if q==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print(1)
        else:
            print(0)