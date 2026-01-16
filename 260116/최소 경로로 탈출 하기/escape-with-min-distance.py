from collections import deque
n, m = map(int, input().split())
snake = [list(map(int, input().split())) for _ in range(n)]

visited = [ [0]*m for _ in range(n)]

count_list=[ [-1]*m for _ in range(n)]
count_list[0][0]=0
# Please write your code here.
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def BFS(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y]=True

    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            temp_x=curr_x+dx[i]
            temp_y=curr_y+dy[i]

            if not (0<=temp_x<n and 0<=temp_y<n):
                continue
            
            if snake[temp_x][temp_y]==0:
                continue

            if visited[temp_x][temp_y]==True:
                continue
            
            visited[temp_x][temp_y]= True
            queue.append((temp_x, temp_y))
            count_list[temp_x][temp_y]= count_list[curr_x][curr_y]+1

BFS(0,0)

# for i in range(n):
#     for j in range(n):
#         print(count_list[i][j], end=" ")
#     print()
# print()

print(count_list[-1][-1])
