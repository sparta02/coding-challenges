n, m = map(int, input().split())

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()

grid=[]

for _ in range(n):
    temp=list(map(int, input().split()))
    grid.append(temp)

commands=[]
for _ in range(m):
    temp=list(map(int, input().split()))
    commands.append(temp)

sum_grid=[[0]*n for _ in range(n)]
sum_grid[0][0]=grid[0][0]

for j in range(1, n):
    sum_grid[0][j]=sum_grid[0][j-1]+grid[0][j]
for i in range(1, n):
    sum_grid[i][0]=sum_grid[i-1][0]+grid[i][0]

for i in range(1, n):
    for j in range(1, n):
        sum_grid[i][j]=sum_grid[i-1][j]+sum_grid[i][j-1]-sum_grid[i-1][j-1]+grid[i][j]


for x1,y1,x2,y2 in commands:
    x1,y1,x2,y2=x1-1,y1-1,x2-1,y2-1
    temp=sum_grid[x2][y2]
    if x1>0:
        temp-=sum_grid[x1-1][y2]
    if y1>0:
        temp-=sum_grid[x2][y1-1]
    if x1>0 and y1>0:
        temp+=sum_grid[x1-1][y1-1]
    print(temp)
