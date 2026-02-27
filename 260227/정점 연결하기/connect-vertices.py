n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

# Please write your code here.
parent= [ i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    if A!=B:
        min_num, max_num=min(A,B), max(A,B)
        parent[max_num]=min_num

for a, b in edges:
    union(a, b)


# 각 정점의 루트 수집
roots = set()
for i in range(1, n + 1):
    roots.add(find(i))

# 연결 요소는 정확히 2개
r1, r2 = min(roots), max(roots)
print(r1, r2)