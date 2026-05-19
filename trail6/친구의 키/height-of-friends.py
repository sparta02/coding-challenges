from collections import deque
n, m = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]

indegree=[0]*(n+1)

edges=[[] for _ in range(n+1)]

for s, e in temp:
    edges[s].append(e)
    indegree[e]+=1

queue=deque()

for i in range(1, n+1):
    if indegree[i]==0:
        queue.append(i)
answer=[]
while queue:
    curr=queue.popleft()
    answer.append(curr)

    for next in edges[curr]:
        indegree[next]-=1

        if indegree[next]==0:
            queue.append(next)

print(*answer)