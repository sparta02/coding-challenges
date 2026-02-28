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

# n=4
# m=3
# len(set)=1

# n=4
# m=2
# len(set)=2

# n=4
# m=3
# len(set)=2

필요없는_간선_수=m+len(count_set)-n
print(필요없는_간선_수+len(count_set)-1)