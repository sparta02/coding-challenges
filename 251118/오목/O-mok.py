board = [list(map(int, input().split())) for _ in range(19)]


# Please write your code here.

def check_y(x,y):
    standard=board[x][y]
    if board[x][y+1]==standard and board[x][y+2]==standard and board[x][y+3]==standard and board[x][y+4]==standard:
        return True
    return False

def check_x(x,y):
    standard=board[x][y]
    if board[x+1][y]==standard and board[x+2][y]==standard and board[x+3][y]==standard and board[x+4][y]==standard:
        return True
    return False

def check_side1(x,y):
    standard=board[x][y]
    if board[x+1][y+1]==standard and board[x+2][y+2]==standard and board[x+3][y+3]==standard and board[x+4][y+4]==standard:
        return True
    return False

def check_side2(x,y):
    standard=board[x][y]
    if board[x-1][y+1]==standard and board[x-2][y+2]==standard and board[x-3][y+3]==standard and board[x-4][y+4]==standard:
        return True
    return False

result=0
result_x=0
result_y=0
for x in range(15):
    for y in range(19):
        if check_x(x,y) and (board[x][y]==1 or board[x][y]==2):
            result=board[x][y]
            result_x=x+3
            result_y=y+1
for x in range(19):
    for y in range(15):
        if check_y(x,y) and (board[x][y]==1 or board[x][y]==2):
            result=board[x][y]
            result_x=x+1
            result_y=y+3

for x in range(15):
    for y in range(15):
        if check_side1(x,y) and (board[x][y]==1 or board[x][y]==2):
            result=board[x][y]
            result_x=x+3
            result_y=y+3

for x in range(4,19):
    for y in range(15):
        if check_side1(x,y) and (board[x][y]==1 or board[x][y]==2):
            result=board[x][y]
            result_x=x-3
            result_y=y+3

print(result)
if result!=0:
    print(result_x, result_y)