N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.

class stack:
    def __init__(self):
        self.item =[]

    def push(self, item):
        self.item.append(item)

    def empty(self):
        return 0 if self.item else 1

    def pop(self):
        if self.empty():
            raise Exception("스택이 비어있습니다")
        else:
            return self.item.pop()
    
    def size(self):
        return len(self.item)
    
    def top(self):
        return self.item[len(self.item)-1]

s= stack()
# s.push(3)
# print(s.size())
# print(s.empty())
# print(s.pop())
# # push 3
# size

for i in range(N):
    if command[i] == "push":
        s.push(value[i])
    elif command[i] == "pop":
        print(s.pop())
    elif command[i] == "size":
        print(s.size())
    elif command[i] == "empty":
        print(s.empty())
    elif command[i] == "top":
        print(s.top())