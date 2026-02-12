from collections import deque

n, k = map(int, input().split())

road=[-1]*(200000)

queue=deque()
queue.append(n)
road[n]=0

while(queue):
    num=queue.popleft()
    if 0<=(2*num)<len(road) and road[2*num]==-1:
        road[2*num]=road[num]
        queue.append(2*num)
        
    for i in (num-1, num+1):
        if 0<=i<len(road) and road[i]==-1:
            road[i]=road[num]+1
            queue.append(i)

    

print(road[k])