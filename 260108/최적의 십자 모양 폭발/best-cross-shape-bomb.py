n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def print_grid(new_grid):
    for i in range(n):
        for j in range(n):
            print(new_grid[i][j], end=" ")
        print()
    print()


def 폭파(row, col):
    new_grid=[ [0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_grid[i][j]=grid[i][j]

    offset=new_grid[row][col]-1
    # print(f"offset:{offset}")
    for x in range(row-offset, row+offset+1):
        # print(f"삭제할 x:{x}, y:{col}")
        if x<0 or x>=n:
            continue
        new_grid[x][col]=0

    for y in range(col-offset, col+offset+1):
        # print(f"삭제할 x:{row}, y:{y}")
        if y<0 or y>=n:
            continue
        new_grid[row][y]=0
    return new_grid


def 재정렬(new_grid):
    
    temp_list=[ [0]*n for _ in range(n) ]

    for y in range(n):
        temp_x=n-1
        temp_y=y
        for x in range(n-1, -1, -1):
            if new_grid[x][y]!=0:
                temp_list[temp_x][temp_y]=new_grid[x][y]
                temp_x-=1
    
    for i in range(n):
        for j in range(n):
            new_grid[i][j]=temp_list[i][j]

def count_twin(new_grid):
    temp=0
    # 1. 가로 탐색
    for x in range(n):
        for y in range(n-1):
            if new_grid[x][y] == new_grid[x][y+1] and new_grid[x][y]!=0:
                temp+=1
    
    # 2. 세로 탐색
    for x in range(n-1):
        for y in range(n):
            if new_grid[x][y] == new_grid[x+1][y] and new_grid[x][y]!=0:
                temp+=1
    # print(f"temp:{temp}")
    return temp
    


result=0
for i in range(n):
    for j in range(n):
        # print(f"row:{i}, col: {j}")

        new_grid=폭파(i, j)
        # print("폭파 후")
        # print_grid(new_grid)

        재정렬(new_grid)
        # print("재정렬 후")
        # print_grid(new_grid)

        result=max(result, count_twin(new_grid))
print(result)




