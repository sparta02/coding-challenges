n=int(input())
parent=list(map(int, input().split()))
target=int(input())

edges=[ [] for _ in range(n)]

for i in range(n):
    a=i
    b=parent[i]
    if b!=-1:
        edges[b].append(a)

# print(edges)

edges[target]=[]
for edge in edges:
    if target in edge:
        edge.remove(target)
parent[target]=[]

# print(edges)


stack=[]
for i in range(n):
    if parent[i]==-1:
        stack.append(i)

result=0
while stack:
    curr=stack.pop()

    if len(edges[curr])==0:
        # print(f"ok{curr}")
        result+=1
    for next in edges[curr]:
        # print(next)
        stack.append(next)

print(result)