board = [list(input()) for _ in range(10)]

# Please write your code here.

L_x=0
L_y=0
R_x=0
R_y=0
B_x=0
B_y=0

for i in range(10):
    for j in range(10):
        if board[i][j]=='L':
            L_x=i
            L_y=j
        if board[i][j]=='R':
            R_x=i
            R_y=j
        if board[i][j]=='B':
            B_x=i
            B_y=j

# print(L_x, L_y)
# print(R_x, R_y)
# print(B_x, B_y)

dist = abs(L_x-B_x) + abs(L_y-B_y)-1
if (L_x==R_x and R_x==B_x and L_y<R_y<B_y) or (L_y==R_y and R_y==B_y and L_x<R_x<B_x):
    dist+=2

print(dist)