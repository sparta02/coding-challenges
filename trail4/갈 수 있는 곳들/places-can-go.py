from collections import deque
cnt=0

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.


visited=[ [0]*n for _ in range(n)]

def bfs(x, y):
    global cnt
    # print(f"start: {x}, {y}")
    visited[x][y]=1
    queue=deque()
    queue.append((x, y))

    while queue:
        curr_x, curr_y = queue.popleft()
        cnt+=1
        # print(curr_x, curr_y)
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            next_x=curr_x+dx[i]
            next_y=curr_y+dy[i]
            if 0<=next_x<n and 0<=next_y<n and visited[next_x][next_y]==0 and grid[next_x][next_y]==0:
                visited[next_x][next_y]=1
                queue.append((next_x, next_y))



for x, y in points:
    if visited[x-1][y-1]==0:
        bfs(x-1, y-1)
print(cnt)