from collections import deque
n, m=map(int, input().split())
edges=[ [] for _ in range(n+1)]
indegree=[0]*(n+1)

for _ in range(m):
    s, e = map(int, input().split())
    edges[s].append(e)
    indegree[e]+=1

# print(edges[1:])
# print(indegree[1:])

queue=deque()
for i in range(1, n+1):
    if indegree[i]==0:
        queue.append(i)

while queue:
    curr=queue.popleft()
    print(curr, end=" ")

    for next in edges[curr]:
        indegree[next]-=1
        if indegree[next]==0:
            queue.append(next)