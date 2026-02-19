n=int(input())
grid= [ [' ']* (2*n) for _ in range(n )]


def start(i, j, size):
    if size==3:
        grid[i][j]="*"
        grid[i+1][j-1]="*"
        grid[i+1][j+1]="*"
        for k in range(-2, 3):
            grid[i+2][j+k]="*"

    else:
        newsize=size//2
        start(i,j,newsize)
        start(i+newsize,j-newsize,newsize)
        start(i+newsize,j+newsize,newsize)


start(0, n-1,n)


def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end="")
        print()
    print()

print_grid()