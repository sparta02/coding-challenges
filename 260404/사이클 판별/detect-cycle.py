from collections import deque
import sys

n, m = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
edges=[[] for _ in range(n+1)]

indegree=[0]*(n+1)
cnt=0
for s, e in temp:
    edges[s].append(e)
    indegree[e]+=1

# print(edges)
# print(indegree)

queue=deque()
for i in range(1, n+1):
    if indegree[i]==0:
        queue.append(i)
# print(queue)

while queue:
    curr=queue.popleft()
    # print(curr)
    cnt+=1

    for next in edges[curr]:
        indegree[next]-=1
        # print(next, indegree)

        if indegree[next]<0:
            print('Exists')
            sys.exit
        elif indegree[next]==0:
            queue.append(next)
if cnt==n:
    print('Not Exists')
else:
    print('Exists')