from collections import deque
import sys
n, m = map(int, input().split())
edges=[[] for _ in range(n+1)]
indegree= [0] * (n+1)

for _ in range(m):
    s, e= map(int, input().split())
    edges[s].append(e)

    indegree[e]+=1


queue=deque()
for i in range(1, n+1):
    if indegree[i]==0:
        queue.append(i)
cnt=0
while queue:
    curr=queue.popleft()
    cnt+=1
    for next in edges[curr]:
        indegree[next]-=1
        
        
        if indegree[next]==0:
            queue.append(next)
if cnt==n:
    print('Consistent')
else:
    print('Inconsistent')

