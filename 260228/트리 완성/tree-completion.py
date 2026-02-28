n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

parent=[i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    parent[A]=B

for a, b in edges:
    union(a, b)

count_set=set()
# print(parent)
for i in range(1, n+1):
    count_set.add(find(i))
print(len(count_set)-1)