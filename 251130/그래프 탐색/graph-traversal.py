n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]


class stack:
    def __init__(self):
        self.list=[]

    def push(self, value):
        self.list.append(value)
    
    def empty(self):
        if len(self.list)==0:
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            raise exception("스택이 비어있습니다.") 
        else:
            return self.list.pop()
    
    def print_list(self):
        print("스택 안 내용: ", end=" ")
        for i in range(len(self.list)):
            print(self.list[i], end=" ")
        print()

# Please write your code here.
def print_arr():
    for i in range(n+1):
        for j in range(n+1):
            print(arr[i][j], end=" ")
        print()

arr= [ [0]*(n+1) for _ in range(n+1)]

for edge in edges:
    arr[edge[0]][edge[1]]=1
    arr[edge[1]][edge[0]]=1

visited_arr=[0]*(n+1)
result_arr=[0]*(n+1)


# 시작
s =stack()
s.push(1)

while(s.empty() == False):
    #s.print_list()
    현재위치=s.pop()
    #print(f"현재위치:{현재위치}")

    if visited_arr[현재위치]:
        continue

    
    visited_arr[현재위치]=1
    
    #print(f"방문한 곳: {visited_arr}")

    for curr_v in range(1, n+1):
        if arr[현재위치][curr_v] and not visited_arr[curr_v]:
            s.push(curr_v)

    #print(f"방문한 곳: {visited_arr}")

# print(visited_arr)

print(sum(visited_arr)-1)