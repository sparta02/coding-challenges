from collections import deque
n= int(input())
queue= deque()

for i in range(1, n+1):
    queue.append(i)


while(len(queue)!=1):
    queue.popleft()
    if len(queue)==1:
        break
    temp=queue.popleft()
    queue.append(temp)

print(queue[0])