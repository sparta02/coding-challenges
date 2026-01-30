import heapq

N = int(input())
commands = []

class priorityqueue:
    def __init__(self):
        self.pq=[]
    
    def empty(self):
        if self.pq:
            return 0
        return 1

    def size(self):
        return len(self.pq)

    def push(self, value):
        heapq.heappush(self.pq, -value)

    def pop(self):
        if self.empty==False:
            raise Exception("우선순위 큐에 아무 값도 없음.")
        return -heapq.heappop(self.pq)
    
    def top(self):
        if self.empty==False:
            raise Exception("우선순위 큐에 아무 값도 없음.")
        return -self.pq[0]


for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

pq=priorityqueue()
# print(commands)
# Please write your code here.
for i in range(N):
    if commands[i][0]=="push":
        pq.push(commands[i][1])
    elif commands[i][0]=="pop":
        print(pq.pop())
    elif commands[i][0]=="size":
        print(pq.size())
    elif commands[i][0]=="empty":
        print(pq.empty())
    elif commands[i][0]=="top":
        print(pq.top())

