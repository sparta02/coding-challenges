from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
total_visited=[[0]*(n) for _ in range(n)]

def bfs(x, y):
    queue=deque()
    queue.append((x,y))
    visited=[[0]*(n) for _ in range(n)]
    visited[x][y]=1
    total_visited[x][y]=1

    while queue:
        curr_x, curr_y=queue.popleft()
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            next_x=curr_x+dx[i]
            next_y=curr_y+dy[i]
            if 0<=next_x<n and 0<=next_y<n and visited[next_x][next_y]==0 and grid[next_x][next_y]==0:
                visited[next_x][next_y]=1
                total_visited[next_x][next_y]=1
                queue.append((next_x, next_y))


for x, y in points:
    bfs(x-1, y-1)

result=0
for i in range(n):
    result+=sum(total_visited[i])

print(result)