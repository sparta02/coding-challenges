n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
empty=[]
virus=[]
빈칸=n*m
for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                empty.append((i,j))
            elif grid[i][j]==2:
                virus.append((i,j))
                빈칸-=1
            elif grid[i][j]==1:
                빈칸-=1

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()


result=0
def test():
    global result 
    new_grid=[row[:] for row in grid]
    for i in select:
        new_grid[empty[i][0]][empty[i][1]]=1

    # if select==[0,4, 16]:
    #     print_grid(new_grid)

    stack=virus[:]
    visited=[ [0]*m for _ in range(n)]
    temp=0
    while stack:
        x, y = stack.pop()
        # if select==[0,4, 16]:
        #     print(x,y)

        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if 0<=next_x<n and 0<=next_y<m:
                if new_grid[next_x][next_y]==0:
                    if visited[next_x][next_y]==0:
                        visited[next_x][next_y]=1
                        temp+=1
                        # new_grid[next_x][next_y]=2
                        stack.append((next_x, next_y))
    result= max(result, 빈칸-3-temp)

    # if select==[0,4, 16]:
    #     print_grid(new_grid)
    # if select==[0,4, 16]:
    #     print(빈칸-3-temp)




select=[]
def choose(start, num):
    if num==3:
        test()
        return
    
    for i in range(start, len(empty)):
        select.append(i)
        choose(i+1, num+1)
        select.pop()

choose(0, 0)
print(result)