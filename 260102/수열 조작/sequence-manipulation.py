from collections import deque

n = int(input())

# Please write your code here.
dq=deque()

for i in range(1, n+1):
    dq.append(i)

while(len(dq)>1):
    dq.popleft()
    temp=dq.popleft()
    dq.append(temp)

print(dq.popleft())