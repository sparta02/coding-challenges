from collections import deque

n=int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

# 상어의 위치, 사이즈, 먹은 물고기 수
shark_index=[-1,-1]
shark_size=2
shark_eated=0

for i in range(n):
    for j in range(n):
        if grid[i][j]==9:
            shark_index=(i,j)

def print_grid(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()

def find_fishs():
    fishs=[]
    queue=deque()
    shark_x, shark_y=shark_index
    # 큐에 들어가는 양식
    # 거리, x좌표, y좌표
    queue.append((0, shark_x, shark_y))
    visited=[ [0]*n for _ in range(n)]
    visited[shark_x][shark_y]=1
    
    while queue:
        curr_dist, curr_x, curr_y=queue.popleft()
        # 현재 위치에 물고기가 있고, 먹을 수 있다면
        # fishs에 추가
        if grid[curr_x][curr_y] not in (0, 9):
            if grid[curr_x][curr_y]<shark_size:
                fishs.append((curr_dist, curr_x, curr_y))
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]

        for i in range(4):
            next_x=curr_x+dx[i]
            next_y=curr_y+dy[i]
            # 물고기를 먹을 수 있는 조건
            # 현재 아기상어보다 크기가 작아야 함
            if 0<=next_x<n and 0<=next_y<n:
                if grid[next_x][next_y]<=shark_size and visited[next_x][next_y]==0:
                    visited[next_x][next_y]=1
                    queue.append((curr_dist+1,next_x,next_y))
    return fishs

def eat_fish(fish):
    global shark_index, shark_size, shark_eated
    _, target_x, target_y = fish
    new_grid=[row[:] for row in grid]

    shark_x, shark_y=shark_index
    # 먹이 먹기
    shark_eated+=1
    # 자기 몸무게만큼 먹었으면 크기 증가
    if shark_eated==shark_size:
        shark_size+=1
        shark_eated=0

    # 기존상어 위치 삭제
    new_grid[shark_x][shark_y]=0
    # 새로운 상어 위치 지정
    new_grid[target_x][target_y]=9
    shark_index=(target_x, target_y)

    return new_grid

    

# 결과 시간
time=0
while(1):
    # 현재 아기상어가 먹을 수 있는 생선들 목록
    fishs=find_fishs()

    # 만약 물고기가 없다면, 종료
    if len(fishs)==0:
        break
    
    # 물고기가 있다면, 아래 조건에 맞는 물고기를 맨 앞으로
    # 1. 거리가 가장 가깝다
    # 2. 가장 위, 가장 왼쪽에 있는 물고기
    fishs.sort()
    # print(fishs)

    # 해당 물고기 먹기
    grid=eat_fish(fishs[0])
    time+=fishs[0][0]
    # print_grid(grid)
    
print(time)