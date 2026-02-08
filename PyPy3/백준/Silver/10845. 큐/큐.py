from collections import deque

n= int(input())

commands=[]

for _ in range(n):
    temp= list(input().split())
    if temp[0]=='push':
        temp[1]=int(temp[1])
    commands.append(temp)

# print(commands)


queue=deque()
for i in range(n):
    if commands[i][0]=='push':
        queue.append(commands[i][1])
    elif commands[i][0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif commands[i][0]=='size':
        print(len(queue))
    elif commands[i][0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif commands[i][0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif commands[i][0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
   # print(stack)
