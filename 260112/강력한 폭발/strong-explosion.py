from itertools import combinations

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def print_grid(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()

def bomb():
    #print(num_list)
    next_list=[ [0]*n for _ in range(n)]
    현재숫자=0
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                next_list[i][j]=1
                # 숫자 1
                if num_list[현재숫자]==1:
                    for k in range(-2, 3):
                        # [i+k][j]에 색칠
                        if 0<=i+k<n:
                            next_list[i+k][j]=1
                # 숫자 2
                elif num_list[현재숫자]==2:
                    for k in range(4):
                        dx=[-1,0,1,0]
                        dy=[0,-1,0,1]
                        if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                            next_list[i+dx[k]][j+dy[k]]=1
                # 숫자 3
                elif num_list[현재숫자]==3:
                    for k in range(4):
                        dx=[-1,1,-1,1]
                        dy=[-1,-1,1,1]
                        if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                            next_list[i+dx[k]][j+dy[k]]=1
                현재숫자+=1
    #print_grid(next_list)
    count=0
    for i in range(n):
        for j in range(n):
            count+=next_list[i][j]
    #print(count)
    return count


result=0
num_list=[]         

def call(num, bombs_count):
    global result
    if num==bombs_count:
        result=max(result, bomb())
        return
    
    for i in range(1, 4):
        num_list.append(i)
        call(num+1, bombs_count)
        num_list.pop()

bombs_count=0
for i in range(n):
        for j in range(n):
            bombs_count+=grid[i][j]
#print(bombs_count)
call(0, bombs_count)

print(result)