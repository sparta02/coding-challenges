import heapq
n, m = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]
edges=[ [] for _ in range(n+1)]
indegree=[0]*(n+1)

for start, end in temp:
    edges[start].append(end)
    indegree[end]+=1

pq=[]
for i in range(1, n+1):
    if indegree[i]==0:
        heapq.heappush(pq, i)

result=[]
while pq:
    curr=heapq.heappop(pq)

    result.append(curr)
    for next in edges[curr]:
        indegree[next]-=1
        if indegree[next]==0:
            heapq.heappush(pq, next)

if len(result)==n:
    print(*result)
else:
    print(-1)