from collections import deque
N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

s=deque()

for i in range(N):
    if command[i]=="push":
        s.append(A[i])
    elif command[i]=="pop":
        print(s.popleft())
    elif command[i]=="size":
        print(len(s))
    elif command[i]=="empty":
        print(0 if s else 1)
    elif command[i]=="front":
        print(s[0])
    