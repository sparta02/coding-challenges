import sys

grid=[ list(map(int, input())) for _ in range(9)]

zeros=[]

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
    print()

for i in range(9):
    for j in range(9):
        if grid[i][j]==0:
            zeros.append((i, j))

available=[ [[i for i in range(1, 10)] for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        target=grid[i][j]
        if target!=0:

            for k in range(9):
                if target in available[i][k]:
                    available[i][k].remove(target)
                if target in available[k][j]:
                    available[k][j].remove(target)
            x=i//3
            y=j//3
            for x_offset in range(3):
                for y_offset in range(3):
                    curr_x=x*3+x_offset
                    curr_y=y*3+y_offset
                    if target in available[curr_x][curr_y]:
                        available[curr_x][curr_y].remove(target)

# print_grid(grid)

# zeros_2=[]

# while zeros !=zeros_2:
#     zeros_2= [ row[:] for row in zeros ]
#     for i in range(9):
#         for j in range(9):
#             if (i,j) in zeros and len(available[i][j])==1:
#                 target=available[i][j][0]
#                 grid[i][j]=target

#                 for k in range(9):
#                     if target in available[i][k]:
#                         available[i][k].remove(target)
#                     if target in available[k][j]:
#                         available[k][j].remove(target)
#                 x=i//3
#                 y=j//3
#                 for x_offset in range(3):
#                     for y_offset in range(3):
#                         curr_x=x*3+x_offset
#                         curr_y=y*3+y_offset
#                         if target in available[curr_x][curr_y]:
#                             available[curr_x][curr_y].remove(target)
#                 zeros.remove((i,j))
#     # print_grid(grid)

def check_row_col(x, y, target):
    for i in range(9):
        if grid[x][i]==target:
            return False
        if grid[i][y]==target:
            return False
    return True

def check_box(i, j, target):
    x=(i//3)*3
    y=(j//3)*3
    for x_offset in range(3):
        for y_offset in range(3):
            if grid[x+x_offset][y+y_offset]==target:
                return False
    return True

# print(zeros)
def choose(num):
    if num==len(zeros):
        for i in range(9):
            print("".join(map(str, grid[i])))
        sys.exit()
        
        return
    x, y=zeros[num]

    for i in range(1, 10):
        if check_row_col(x,y,i) and check_box(x,y,i):
            # print(i)
            grid[x][y]=i
            choose(num+1)
            grid[x][y]=0

choose(0)

