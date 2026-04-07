n,m = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(n)]

def change(x,y, grid):
    dx=[0, 1, 0, -1, 0]
    dy=[0, 0, 1, 0, -1]
    for i in range(5):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0<=next_x<n and 0<=next_y<m:
            grid[next_x][next_y]=grid[next_x][next_y]^1

def print_grid(grid):
    for i in range(n):
        print(*grid[i])
    print()

result=10**9
for bit in range(1<<m):
    new_grid=[row[:] for row in grid]
    temp=0

    for j in range(m):
        if bit & (1<<j):
            change(0, j, new_grid)
            temp+=1
    for i in range(1, n):
        for j in range(m):
            if new_grid[i-1][j]==0:
                change(i, j, new_grid)
                temp+=1
    flag=1
    for i in range(n):
        for j in range(m):
            if new_grid[i][j]==0:
                flag=0
                break
    if flag:
        result=min(result, temp)

if result==10**9:
    print(-1)
else:
    print(result)


