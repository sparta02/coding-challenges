from collections import deque
import sys
input=sys.stdin.readline

n=int(input())

visited=[0]*(n+10)

queue = deque()

queue.append(1)
visited[1]=1

while queue:
    # print(queue)
    curr=queue.popleft()
    if curr==n:
        break
    if curr*3<=n+1 and visited[curr*3]==0:
        visited[curr*3]=1
        queue.append(curr*3)
    if curr*2<=n+1 and visited[curr*2]==0:
        visited[curr*2]=2
        queue.append(curr*2)
    if curr<=n and visited[curr+1]==0:
        visited[curr+1]=3
        queue.append(curr+1)

result_list=[n]
num=n
while num!=1:
    curr=visited[num]
    if curr==1:
        num//=3
    elif curr==2:
        num//=2
    else:
        num-=1
    result_list.append(num)
print(len(result_list)-1)
print(*result_list)