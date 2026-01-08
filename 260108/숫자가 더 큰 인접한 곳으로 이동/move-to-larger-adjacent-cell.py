n, r, c = map(int, input().split())
a=[[0] * (n + 1) for _ in range(n + 1)]
b= [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
def print_grid(grid):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(grid[i][j], end=" ")
        print()
    print()

def move(x, y):
    # 우, 좌, 하, 상 순서로
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0, 0]

    result_x=-1
    result_y=-1
    for i in range(4):
        temp_x=x+dx[i]
        temp_y=y+dy[i]
        if b[temp_x][temp_y]==0 and a[temp_x][temp_y] > a[x][y]:
            result_x=temp_x
            result_y=temp_y
    if result_x != -1 and result_y !=-1:
        b[result_x][result_y]=1
    return (result_x, result_y)

            
b[r][c]=1

new_x=r
new_y=c
while(1):
    print(a[new_x][new_y], end=" ")
    new_x, new_y= move(new_x, new_y)

    # print_grid(a)
    # print_grid(b)
    if (new_x == -1 or new_y ==-1):
        break
