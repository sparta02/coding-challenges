from collections import deque

a, b = map(int, input().split())


queue=deque()

queue.append((a, 1))

result=-1
while(queue):
    num, cnt=queue.popleft()
    if num==b:
        result=cnt
        break

    if num*2<=b:
        queue.append((num*2, cnt+1))
    
    if num*10+1<=b:
        queue.append((num*10+1, cnt+1))

if result!=-1:
    print(cnt)
else:
    print(-1)