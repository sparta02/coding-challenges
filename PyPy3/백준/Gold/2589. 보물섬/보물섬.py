from collections import deque
import sys
input=sys.stdin.readline
n, m = map(int, input().split())

grid= []

while input:
    line = list(input().strip())
    if not line:
        break
    grid.append(line)
# print(grid)
    
ground=[]

for i in range(n):
    for j in range(m):
        if grid[i][j]=='L':
            ground.append((i,j))


def bfs(x, y):
    visited=[[0]*m for _ in range(n)]
    queue=deque()
    queue.append((x,y, 0))
    max_num=0
    visited[x][y]=1
    while queue:
        curr_x, curr_y, cnt=queue.popleft()
        max_num=max(max_num, cnt)

        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            next_x=curr_x+dx[i]
            next_y=curr_y+dy[i]
            if 0<=next_x<n and 0<=next_y<m and visited[next_x][next_y]==0 and grid[next_x][next_y]=='L':
                queue.append((next_x, next_y, cnt+1))
                visited[next_x][next_y]=1
    # print(x, y)
    # print(max_num)
    return max_num

result=0

for x,y in ground:
    result=max(result, bfs(x,y))

print(result)