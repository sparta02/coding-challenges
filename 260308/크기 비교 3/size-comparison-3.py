import heapq
n, m = map(int, input().split())
edges = [ [] for _ in range(n+1)]
indegree=[0]*(n+1)
pq=[]

for _ in range(m):
    s, e= map(int, input().split())
    edges[s].append(e)
    edges[s].sort()

    indegree[e]+=1

for i in range(1, n+1):
    if indegree[i]==0:
        heapq.heappush(pq, i)

while pq:
    curr=heapq.heappop(pq)
    print(curr, end=" ")

    for next in edges[curr]:
        indegree[next]-=1

        if indegree[next]==0:
            heapq.heappush(pq, next)