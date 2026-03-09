from collections import deque
n = int(input())
nodes = {}
temp_nodes=input().split()
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
        
print(len(queue))
for num in queue:
    print(nodes[num], end=" ")
print()

for i in range(n):
    son_son_list={}
    visited=[0]*n
    queue=deque()
    queue2=deque()
    for item in edges[i]:
        queue.append(item)
        queue2.append(item)
    
    
    while queue:
        curr=queue.popleft()

        for next in edges[curr]:
            visited[next]=1
            son_son_list[next]=1
            queue.append(next)

    print(nodes[i], end=" ")
    print(len(queue2)-len(son_son_list), end=" ")
    for item in queue2:
        if item not in son_son_list:
            print(nodes[item], end=" ")

    print()
    