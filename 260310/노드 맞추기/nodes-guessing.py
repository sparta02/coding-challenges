from collections import deque

n = int(input())
nodes = {}
temp_nodes=input().split()
temp_nodes.sort()

for i in range(n):
    nodes[i]=temp_nodes[i]
    nodes[temp_nodes[i]]=i

m = int(input())
edges=[ [] for _ in range(n)]
indegree=[0]*n

for _ in range(m):
    xi, yi = input().split()
    edges[nodes[yi]].append(nodes[xi])
    indegree[nodes[xi]]+=1

queue=deque()

for i in range(n):
    if indegree[i]==0:
        queue.append(i)
child= [[] for _ in range(n)]

print(len(queue))
for item in queue:
    print(nodes[item], end=" ")
print()

while queue:
    curr= queue.popleft()
    for next in edges[curr]:
        indegree[next]-=1
        if indegree[next]==0:
            child[curr].append(next)
            queue.append(next)
        
        

for i in range(n):
    print(nodes[i], end=" ")
    print(len(child[i]), end=" ")
    child[i].sort()
    for num in child[i]:
        print(nodes[num], end=" ")
    print()