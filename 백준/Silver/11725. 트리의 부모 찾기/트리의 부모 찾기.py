from collections import deque
import sys
input=sys.stdin.readline

n= int(input().strip())


nodes=[ [] for _ in range(n+1)]

for _ in range(n-1):
    a, b= map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited=[0]*(n+1)


queue=deque()
queue.append(1)
visited[1]=1

while (queue):
    curr=queue.pop()
    
    for i in nodes[curr]:
        if visited[i]==0:
            visited[i]=curr
            queue.append(i)

for i in range(2, n+1):
    print(visited[i])