n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

# Please write your code here.

uf = [ i for i in range(n+1)]


def find(x):
    if uf[x]==x:
        return x
    root=find(uf[x])
    uf[x]=root
    return root

def union(a, b):
    A=find(a)
    B=find(b)
    uf[A]=B

for a, b in edges:
    union(a, b)

flag=1
for i in range(len(path)-1):

    if find(uf[path[i]])!=find(uf[path[i+1]]):
        flag=0

print(flag)