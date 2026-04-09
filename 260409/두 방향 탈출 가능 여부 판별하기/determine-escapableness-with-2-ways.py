import sys
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
stack=[]
stack.append((0,0))
visited=[ [0]*(m) for _ in range(n)]
visited[0][0]=1
while stack:
    curr_x, curr_y=stack.pop()
    if (curr_x, curr_y) == (n-1, m-1):
        print(1)
        sys.exit()
    dx=[1,0]
    dy=[0,1]
    for i in range(2):
        next_x=curr_x+dx[i]
        next_y=curr_y+dy[i]
        if 0<=next_x<n and 0<=next_y<m:
            if grid[next_x][next_y]==1 and visited[next_x][next_y]==0:
                visited[next_x][next_y]=1
                stack.append((next_x, next_y))


print(0)