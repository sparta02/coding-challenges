from collections import deque

class Deque:
    def __init__(self):
        self.dq = deque()

    def size(self):
        return len(self.dq)
    
    def empty(self):
        if len(self.dq):
            return 0
        return 1
    
    def front(self):
        return self.dq[0]
    
    def back(self):
        return self.dq[-1]

    def push_front(self, item):
        self.dq.appendleft(item)
    
    def push_back(self, item):
        self.dq.append(item)
    
    def pop_front(self):
        return self.dq.popleft()
    
    def pop_back(self):
        return self.dq.pop()
    

n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
dq=Deque()

for c, n in zip(cmd, num):
    if c=="push_front":
        dq.push_front(n)
    elif c=="push_back":
        dq.push_back(n)
    elif c=="pop_front":
        print(dq.pop_front())
    elif c=="pop_back":
        print(dq.pop_back())
    elif c=="size":
        print(dq.size())
    elif c=="empty":
        print(dq.empty())
    elif c=="front":
        print(dq.front())
    elif c=="back":
        print(dq.back())
    
