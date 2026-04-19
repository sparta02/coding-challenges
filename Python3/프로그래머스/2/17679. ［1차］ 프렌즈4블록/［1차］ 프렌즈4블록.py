def calc_delete_list(n, m, board):
    delete_list=[ [0]*m for _ in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] != 'X' and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i+1][j+1]:
                delete_list[i][j]=1
                delete_list[i+1][j]=1
                delete_list[i][j+1]=1
                delete_list[i+1][j+1]=1
    return delete_list

def new_board(delete_list, n, m, board):
    new_board=[ row[:] for row in board]
    for i in range(n):
        for j in range(m):
            if delete_list[i][j]==1:
                x=i
                while(x):
                    new_board[x][j]=new_board[x-1][j]
                    x-=1
                new_board[x][j]='X'
    return new_board
                

def solution(n, m, board):
    answer = 0
    board=[list(row) for row in board]
    
    while True:
        delete_list=calc_delete_list(n, m, board)
        flag=0
        for i in range(n):
            flag+=sum(delete_list[i])
        if flag==0:
            break
        answer+=flag
        board=new_board(delete_list, n, m, board)
    
    return answer