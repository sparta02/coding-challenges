n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n)]

parent= [i for i in range(100001)]
size= [1]*(100001)

def find(x):
    if parent[x] !=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    A=find(a)
    B=find(b)
    # print(A, B)
    if A!=B:
        parent[B]=A
        size[A]+=size[B]
        
    

for a, b in edges:
    union(a, b)
    print(size[find(a)])