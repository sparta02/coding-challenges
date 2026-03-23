n, m = map(int, input().split())
commmand=[ list(map(int, input().split())) for _ in range(m)]
parent=[i for i in range(n+1)]

def find(x):
    root=x
    while root!=parent[root]:
        root=parent[root]

    while x!=root:
        next=parent[x]
        parent[x]=root
        x=next
    return root

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

for c, a, b in commmand:
    if c==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')