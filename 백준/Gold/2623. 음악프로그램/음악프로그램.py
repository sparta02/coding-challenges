from collections import deque
n, m = map(int, input().split())
edges=[ [] for _ in range(n+1)]
indegree=[0]*(n+1)
for _ in range(m):
    arr=list(map(int, input().split()))
    arr=arr[1:]
    for i in range(len(arr)-1):
        edges[arr[i]].append(arr[i+1])
        indegree[arr[i+1]]+=1

queue=deque()

for i in range(1, n+1):
    if indegree[i]==0:
        queue.append(i)

result=[]

while queue:
    curr=queue.popleft()
    result.append(curr)
    for next in edges[curr]:
        indegree[next]-=1
        if indegree[next]==0:
            queue.append(next)

if len(result)==n:
    for item in result:
        print(item)
else:
    print(0)