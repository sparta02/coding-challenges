n=int(input())
m=int(input())
INF=10**9
grid= [ [INF]*(n+1) for _ in range(n+1)]
dist= [ [INF]*(n+1) for _ in range(n+1)]

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()

for _ in range(m):
    start, end, d= map(int, input().split())
    grid[start][end]=min(grid[start][end], d)
    

# print_grid(grid)

for i in range(n+1):
    grid[i][i]=0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            grid[i][j]=min(grid[i][j], grid[i][k]+grid[k][j])

# print_grid(grid)

for i in range(1, n+1):
    for j in range(1, n+1):
        print(grid[i][j] if grid[i][j]!=INF else 0, end=" ")
    print()
print()