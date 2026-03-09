from collections import deque
import heapq
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


for item in temp_nodes:
    if indegree[nodes[item]]==0:
        queue.append(item)
        
print(len(queue))
for item in queue:
    print(item, end=" ")
print()

for alpha in temp_nodes:
    i=nodes[alpha]
    son_son_list={}
    visited=[0]*n
    queue=deque()
    pq=[]
    for item in edges[i]:
        queue.append(item)
        heapq.heappush(pq, item)
    
    
    while queue:
        curr=queue.popleft()

        for next in edges[curr]:
            visited[next]=1
            son_son_list[next]=1
            queue.append(next)

    print(nodes[i], end=" ")
    print(len(pq)-len(son_son_list), end=" ")
    while pq:
        item = heapq.heappop(pq)
        if item not in son_son_list:
            print(nodes[item], end=" ")

    print()
    