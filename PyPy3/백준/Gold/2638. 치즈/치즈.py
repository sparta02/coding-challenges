n, m = map(int, input().split())

grid = [ list(map(int, input().split())) for _ in range(n)]

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()

def dfs():
    colored_grid=[ row[:] for row in grid]
    
    stack=[(0,0)]
    visited= [ [0]*m for _ in range(n)]

    colored_grid[0][0]=2
    visited[0][0]=1

    while stack:
        curr_x, curr_y=stack.pop()
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            next_x=curr_x+dx[i]
            next_y=curr_y+dy[i]
            if 0<=next_x<n and 0<=next_y<m and visited[next_x][next_y]==0 and grid[next_x][next_y]==0:
                colored_grid[next_x][next_y]=2
                visited[next_x][next_y]=1
                stack.append((next_x, next_y))
    return colored_grid

def melt_cheese(colored_grid):
    global grid
    # colored_grid의 모든 칸을 순회하며
    # 인접한 2가 2개 이상인 경우
    # 해당 칸을 녹인다
    new_grid=[ row[:] for row in grid]

    for x in range(n):
        for y in range(m):
            temp_count=0
            dx=[1,0,-1,0]
            dy=[0,1,0,-1]
            for i in range(4):
                next_x=x+dx[i]
                next_y=y+dy[i]
                if 0<=next_x<n and 0<=next_y<m:
                    if colored_grid[next_x][next_y]==2:
                        temp_count+=1
            # 인전한 2가 2개 이상인지 확인
            if temp_count>=2:
                new_grid[x][y]=0
    grid=[row[:] for row in new_grid]

def check_finished():
    result=0
    for i in range(n):
        result+=sum(grid[i])
    return result


time=0
while(1):
    time+=1
    colored_grid=dfs()
    # print_grid(colored_grid)
    melt_cheese(colored_grid)
    # print_grid(grid)
    if check_finished()==0:
        break

print(time)