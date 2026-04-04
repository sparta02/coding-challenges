n, m = map(int, input().split())
category=[0]+list(input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]

new_edges=[]
edges=[[] for _ in range(n+1)]

for s,e,d in temp:
    if category[s]!=category[e]:
        new_edges.append((d,s,e))
        edges[s].append((e, d))
        edges[e].append((s, d))

new_edges.sort()

cnt=0
result=0

parent=[i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

for dist, a, b in new_edges:
    if find(a)==find(b):
        continue
    union(a, b)
    cnt+=1
    result+=dist

if cnt==n-1:
    print(result)
else:
    print(-1)