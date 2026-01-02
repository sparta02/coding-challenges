from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def size(self):
        return len(self.dq)
    
    def empty(self):
        if self.dq:
            return 0
        return 1

    def push(self, item):
        self.dq.append(item)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.dq[0]


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

new_queue = Queue()
for com, num in zip(command, A):
    if com == "push":
        new_queue.push(num)
    elif com == "pop":
        print(new_queue.pop())
    elif com =="size":
        print(new_queue.size())
    elif com =="empty":
        print(new_queue.empty())
    elif com == "front":
        print(new_queue.front())
