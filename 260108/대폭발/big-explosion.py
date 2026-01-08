n, m, r, c = map(int, input().split())

# Please write your code here.
grid=[[0]*n for _ in range(n)]
grid[r-1][c-1]=1


def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()

for time in range(1, m+1):

    for x in range(n):
        for y in range(n):
            
            if grid[x][y] != 1:
                continue
            dx=[0,1,0,-1]
            dy=[1,0,-1,0]

            for i in range(4):
                if 0<=x+dx[i]*(2**(time-1))<n and 0<=y+dy[i]*(2**(time-1))<n and grid[x+dx[i]*(2**(time-1))][y+dy[i]*(2**(time-1))] !=1:
                    grid[x+dx[i]*(2**(time-1))][y+dy[i]*(2**(time-1))]=2
    # print_grid()
    for i in range(n):
        for j in range(n):
            if grid[i][j] ==2:
                grid[i][j]=1
    # print_grid()


result=0
for i in range(n):
        for j in range(n):
            result+=grid[i][j]
print(result)

