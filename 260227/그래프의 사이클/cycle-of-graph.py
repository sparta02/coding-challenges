n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
parent= [i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

for i in range(m):
    a, b = edges[i][0], edges[i][1]
    if find(a)==find(b):
        print(i+1)
        break
    union(a, b)
else:
    print('happy')