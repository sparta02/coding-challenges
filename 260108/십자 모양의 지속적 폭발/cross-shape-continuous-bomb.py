n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input())-1 for _ in range(m)]

# Please write your code here.

def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()


def 폭파(row, col):
    offset=grid[row][col]-1
    # print(f"offset:{offset}")
    for x in range(row-offset, row+offset+1):
        # print(f"삭제할 x:{x}, y:{col}")
        if x<0 or x>=n:
            continue
        grid[x][col]=0

    for y in range(col-offset, col+offset+1):
        # print(f"삭제할 x:{row}, y:{y}")
        if y<0 or y>=n:
            continue
        grid[row][y]=0


def 재정렬():
    global grid
    temp_list=[ [0]*n for _ in range(n) ]

    for y in range(n):
        temp_x=n-1
        temp_y=y
        for x in range(n-1, -1, -1):
            if grid[x][y]!=0:
                temp_list[temp_x][temp_y]=grid[x][y]
                temp_x-=1
    
    grid=temp_list[:]



def 해당_열의_맨_위_숫자(col):
    for i in range(n):
        if grid[i][col] !=0:
            return i
    return -1

for com in commands:
    row=해당_열의_맨_위_숫자(com)
    if row == -1:
        continue
    # print(f"row:{row}, col: {com}")
    폭파(row, com)
    # print("폭파 후")
    # print_grid()
    재정렬()
    # print("재정렬 후")
    # print_grid()
print_grid()



