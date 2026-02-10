t=int(input())

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()

def dfs(x, y, grid):
    #print(f"{x}, {y}")
    stack=[]
    stack.append((x,y))
    grid[x][y]=2

    while(stack):
        curr_x, curr_y=stack.pop()
        dx=[1, 0, -1, 0]
        dy=[0, 1, 0, -1]
        for i in range(4):
            temp_x=curr_x+dx[i]
            temp_y=curr_y+dy[i]
            if 0<=temp_x<len(grid) and 0<=temp_y<len(grid[0]):
                if grid[temp_x][temp_y]==1:
                    grid[temp_x][temp_y]=2
                    stack.append((temp_x, temp_y))

def count_bug(grid):
    cnt=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                dfs(i, j, grid)
                cnt+=1
                #print_grid(grid)
    print(cnt)

for _ in range(t):
    m, n, k = map(int, input().split())
    grid=[ [0]*m for _ in range(n)]
    for _ in range(k):
        b, a=map(int, input().split())
        grid[a][b]=1
    # print_grid(grid)
    count_bug(grid)
