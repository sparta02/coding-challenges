from collections import deque
import sys

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1,c1,r2,c2=r1-1,c1-1,r2-1,c2-1

queue=deque()
visited=[[0]*n for _ in range(n)]

queue.append((r1, c1, 0))
visited[r1][c1]=1

while queue:
    curr_x, curr_y, dist=queue.popleft()
    if (curr_x, curr_y)==(r2, c2):
        print(dist)
        sys.exit()
    
    dx=[-1, -2, -2, -1, 1, 2, 2, 1]
    dy=[-2, -1, 1, 2, 2, 1, -1, -2]
    for i in range(8):
        next_x, next_y = curr_x+dx[i], curr_y+dy[i]
        if 0<=next_x<n and 0<=next_y<n and visited[next_x][next_y]==0:
            visited[next_x][next_y]=1
            queue.append((next_x, next_y, dist+1))

print(-1)