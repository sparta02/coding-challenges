n=int(input())
grid= [ list(map(int, input().split()))for _ in range(n)]

white=0
blue=0

def sum_grid(x, y, n, grid):
    cnt=0
    for i in range(x,x+n):
        for j in range(y,y+n):
            cnt+=grid[i][j]
    return cnt

def cut_paper(x, y, n, grid):
    global white, blue
    # print("==========")
    # print(x,y,n)
    cnt_grid = sum_grid(x, y, n, grid)
    # print(f"count:{cnt_grid}")
    # print(f"white: {white}, blue: {blue}")
    if cnt_grid==n*n:
        blue+=1
        return
    elif cnt_grid==0:
        white+=1
        return
    
    dx=[0,0,1,1]
    dy=[0,1,0,1]
    for i in range(4):
        cut_paper(x+int(dx[i]*n/2), y+int(dy[i]*n/2), int(n/2), grid)

    

cut_paper(0,0,n, grid)
print(white)
print(blue)