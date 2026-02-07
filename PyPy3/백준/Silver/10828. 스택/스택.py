n= int(input())

commands=[]

for _ in range(n):
    temp= list(input().split())
    if temp[0]=='push':
        temp[1]=int(temp[1])
    commands.append(temp)

# print(commands)


stack=[]
for i in range(n):
    if commands[i][0]=='push':
        stack.append(commands[i][1])
    elif commands[i][0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif commands[i][0]=='size':
        print(len(stack))
    elif commands[i][0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif commands[i][0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
   # print(stack)
