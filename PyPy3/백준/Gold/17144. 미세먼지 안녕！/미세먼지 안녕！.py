r, c, t= map(int,input().split())

grid= [ list(map(int, input().split())) for _ in range(r)]
machine=[]

for x in range(r):
    for y in range(c):
        if grid[x][y]==-1:
            machine.append((x,y))



def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()


def split_dust():
    global grid
    new_grid= [ [0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            # 해당 칸에 먼지가 있으면
            if grid[x][y] not in (-1, 0):
                mini_dust=grid[x][y]//5

                dx=[1,0,-1,0]
                dy=[0,1,0,-1]
                for i in range(4):
                    next_x=x+dx[i]
                    next_y=y+dy[i]
                    if 0<=next_x<r and 0<=next_y<c and grid[next_x][next_y]!=-1:
                        new_grid[next_x][next_y]+=mini_dust
                        grid[x][y]-=mini_dust
                new_grid[x][y]+=grid[x][y]
    new_grid[machine[0][0]][machine[0][1]]=-1
    new_grid[machine[1][0]][machine[1][1]]=-1
    grid=new_grid

def cycle():
    # 공기청정기 윗 부분 좌표
    start_x, start_y=machine[0]


    for x in range(start_x-2, -1, -1):

        grid[x+1][0]=grid[x][0]

    for y in range(1, c):

        grid[0][y-1]=grid[0][y]

    for x in range(1, start_x+1):

        grid[x-1][c-1]=grid[x][c-1]

    for y in range(c-2, 0, -1):
        grid[start_x][y+1]=grid[start_x][y]
    
    grid[start_x][1]=0

    # 공기청정기 아랫 부분 좌표
    start_x, start_y=machine[1]


    for x in range(start_x+2, r):
        grid[x-1][0]=grid[x][0]

    for y in range(1, c):
        grid[r-1][y-1]=grid[r-1][y]

    for x in range(r-2, start_x-1, -1):
        grid[x+1][c-1]=grid[x][c-1]

    for y in range(c-2, 0, -1):
        grid[start_x][y+1]=grid[start_x][y]
    
    grid[start_x][1]=0

for _ in range(t):
    split_dust()
    # print_grid(grid)
    cycle()
    # print_grid(grid)

result=2

for x in range(r):
    for y in range(c):
        result+=grid[x][y]
print(result)

