n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

# Please write your code here.
roots=set()
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
        if min_num not in roots:
            roots.add(min_num)
        if max_num in roots:
            roots.remove(max_num)

for a, b in edges:
    union(a, b)

# result=set()
# i=1
# while(len(result)<2):
#     result.add(find(1))
#     i+=1
# result=list(result).sort()
roots=list(roots)
roots.sort()
print(*roots)