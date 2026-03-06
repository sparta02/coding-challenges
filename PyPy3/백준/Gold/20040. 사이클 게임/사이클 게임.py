n,m=map(int, input().split())
command= [ list(map(int, input().split())) for _ in range(m)]

parent=[i for i in range(n)]
def find(x):
    # 최종 조상의 값을 저장할 root
    root=x
    while parent[root]!=root:
        root=parent[root]
    
    # 경로 압축
    while x != root:
        x, parent[x] = parent[x], root
    return parent[x]
    
def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B


for i in range(m):
    s, e = command[i]
    if find(s)==find(e):
        print(i+1)
        break
    union(s, e)
else:
    print(0)