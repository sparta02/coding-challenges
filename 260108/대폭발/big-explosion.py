n, m, r, c = map(int, input().split())

# Please write your code here.
grid=[[0]*n for _ in range(n)]
grid[r-1][c-1]=1

def make_new_grid():
    new_grid=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[i][j]=grid[i][j]
    return new_grid

def print_grid(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()

for time in range(1, m+1):
    new_grid=make_new_grid()
    # print_grid(new_grid)
    for x in range(n):
        for y in range(n):
            
            for i in range(n):
                for j in range(n):
                    if ((abs(x-i) ==time and y==j) or (abs(y-j) == time and x==i)) and grid[i][j]==1:
                        new_grid[x][y]=1

    for i in range(n):
        for j in range(n):
            grid[i][j]=new_grid[i][j]
    # print_grid(grid)

result=0
for i in range(n):
        for j in range(n):
            result+=grid[i][j]
print(result)

