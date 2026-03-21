import sys
from collections import deque
m, n, h = map(int, input().split())
grid=[]

# 높이 h, 세로 n, 가로 m
for _ in range(h):
    temp=[]
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    grid.append(temp)

def count_zero():
    cnt=0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if grid[i][j][k]==0:
                    cnt+=1
    return cnt

def print_grid():
    for i in range(h):
        for j in range(n):
            print(*grid[i][j])
        print()

if count_zero()==0:
    print(0)
    sys.exit()

queue=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k]==1:
                queue.append((i,j,k))

while queue:
    curr_i, curr_j, curr_k=queue.popleft()

    direction=[(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    for num in range(6):
        next_i=curr_i+direction[num][0]
        next_j=curr_j+direction[num][1]
        next_k=curr_k+direction[num][2]

        if 0<=next_i<h and 0<=next_j<n and 0<=next_k<m:
            if grid[next_i][next_j][next_k]==0:
                grid[next_i][next_j][next_k]=grid[curr_i][curr_j][curr_k]+1
                queue.append((next_i, next_j,next_k))

# print_grid()

if count_zero():
    print(-1)
    sys.exit()

result=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            result=max(result, grid[i][j][k])
print(result-1)