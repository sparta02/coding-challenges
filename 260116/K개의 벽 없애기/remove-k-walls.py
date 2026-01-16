from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

result=99999999999999999

# 벽을 제거한 grid
new_grid=[]

# 거리를 저장하는 배열
distance=[ [-1]*n for _ in range(n) ]

# 방문 정보를 저장하는 배열
visited=[ [0]*n for _ in range(n) ]

# 기타 함수들
def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()

# 기존 벽들 위치 저장하는 배열
walls=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            walls.append((i,j))

# grid 설정 후 BFS 탐색
def start_BFS():
    global new_grid
    global visited
    global distance
    global result

    # 1. new_grid 세팅
    new_grid= [row[:] for row in grid]

    for i in range(len(selected)):
        new_grid[walls[selected[i]][0]][walls[selected[i]][1]]=0
    
    # 2. visited 세팅
    visited=[ [0]*n for _ in range(n) ]

    # 3. distance 세팅
    distance=[ [-1]*n for _ in range(n) ]
    
    distance[r1][c1]=0

    #print_grid(new_grid)

    # print_grid(distance)
    BFS(r1, c1)

    # print(distance[r2][c2])
    if distance[r2][c2]!=-1:
        result=min(result, distance[r2][c2])



# BFS 탐색
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def BFS(x, y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    
    while queue:
        curr_x, curr_y=queue.popleft()
        for i in range(4):
            temp_x=curr_x+dx[i]
            temp_y=curr_y+dy[i]

            # 조건 1. index 초과하면 skip
            if not(0<=temp_x<n and 0<=temp_y<n):
                continue
            
            # 조건 2. 벽으로 막혀 있으면 skip
            if new_grid[temp_x][temp_y]==1:
                continue
            
            # 조건 3. 이미 방문했으면 skip
            if visited[temp_x][temp_y]==True:
                continue

            visited[temp_x][temp_y]=True
            distance[temp_x][temp_y]=distance[curr_x][curr_y]+1
            queue.append((temp_x, temp_y))


# k개의 벽 선택
selected=[]


def choose_wall(num):
    if num==len(walls):
        if len(selected)==k:
            #print(selected)
            start_BFS()
        return
    
    selected.append(num)
    choose_wall(num+1)
    selected.pop()

    choose_wall(num+1)

choose_wall(0)

# print(result)
print(-1 if result==99999999999999999 else result)