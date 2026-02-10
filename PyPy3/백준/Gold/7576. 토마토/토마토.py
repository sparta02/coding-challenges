from collections import deque
m,n=map(int, input().split())

grid= [ list(map(int, input().split())) for _ in range(n)]

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()


# 처음부터 모든 토마토가 익어 있다면 0 출력

def all_tomato_done(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                return False
    return True

is_all_tomato_done=all_tomato_done(grid)

queue=deque()

visited= [ [-1]*m for _ in range(n)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            visited[i][j]=0
            queue.append((i,j))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

while(queue):
    x, y=queue.popleft()
    for i in range(4):
        temp_x=x+dx[i]
        temp_y=y+dy[i]
        if 0<=temp_x<n and 0<=temp_y<m:
            if visited[temp_x][temp_y]==-1 and grid[temp_x][temp_y]==0:
                visited[temp_x][temp_y]=visited[x][y]+1
                queue.append((temp_x,temp_y))


# print_grid(visited)

result=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        result=max(result, visited[i][j])

def last_check():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0 and visited[i][j]==-1:
                return True
    return False

if is_all_tomato_done==True:
    print(0)
else:
    if last_check():
        print(-1)
    else:
        print(result)

        