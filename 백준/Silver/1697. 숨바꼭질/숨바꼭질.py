from collections import deque

n, m = map(int, input().split())

visited=[0]*(100001)

queue=deque()

queue.append(n)
visited[n]=1

i=0
while(queue):
    curr=queue.popleft()
    for k in (curr-1, curr+1, curr*2):
        if 0<=k<=100000 and visited[k]==0:
            queue.append(k)
            visited[k]=visited[curr]+1

print(visited[m]-1)