n=int(input())

grid=[ list(input()) for _ in range(n)]

visited=[ [0]*n for _ in range(n)]

def dfs(i,j,target):
    stack=[]
    stack.append((i,j))

    while stack:
        x, y = stack.pop()
        visited[x][y]=1
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if 0<=next_x<n and 0<=next_y<n:
                if grid[next_x][next_y]==target and visited[next_x][next_y]==0:
                    stack.append((next_x, next_y))


cnt1=0

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt1+=1
            dfs(i,j,grid[i][j])

for i in range(n):
    for j in range(n):
        if grid[i][j]=='R':
            grid[i][j]='G'

visited=[ [0]*n for _ in range(n)]

cnt2=0

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt2+=1
            dfs(i,j,grid[i][j])
print(cnt1, cnt2)
