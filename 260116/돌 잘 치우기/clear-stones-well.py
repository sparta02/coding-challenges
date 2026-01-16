from collections import deque 
n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
temp_rocks=[]
visited=[ [0]*n for _ in range(n)]

def reset_visited():
    global visited
    visited=[ [0]*n for _ in range(n)]

def print_grid(temp_grid):
    for i in range(n):
        for j in range(n):
            print(temp_grid[i][j], end=" ")
        print()
    print()



# 시작점
start_point=[]
for _ in range(k):
    ri, ci = map(int, input().split())
    temp=[]
    temp.append(ri - 1)
    temp.append(ci - 1)
    start_point.append(temp)

# 돌 위치
rocks=[]
rocks_count=0
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            rocks.append((i,j))
            rocks_count+=1


# 돌 선택 
selected=[]
def choose_rock(num):
    global temp_rocks
    global temp_count
    global result
    if num==rocks_count:
        if len(selected)==m:
            #print(selected)

            # temp_rocks 초기화
            temp_rocks=[ row[:] for row in grid ]
            # 선택된 돌들은 제거
            for i in selected:
                temp_rocks[rocks[i][0]][rocks[i][1]]=0
            #print_grid(temp_rocks)
            
            #visited 배열, temp_count 초기화
            reset_visited()
            temp_count=0

            # 각 시작점에 대해 BFS 실행
            for i in range(k):
                BFS(start_point[i][0], start_point[i][1])
                #print()

            #print(temp_count)
            result=max(result, temp_count)
        return
    
    selected.append(num)
    choose_rock(num+1)
    selected.pop()

    choose_rock(num+1)


#BFS

result=-1
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
def BFS(x, y):
    global temp_count

    # 만약 현재 시작점이 예전 다른 BFS로 인해 방문했다면 skip
    if visited[x][y]==True:
        return

    queue=deque()
    queue.append((x,y))
    visited[x][y]=True

    while queue:
        curr_x, curr_y=queue.popleft()
        #print(f"현재 위치: {curr_x}, {curr_y}")
        temp_count+=1
        for i in range(4):
            temp_x=curr_x+dx[i]
            temp_y=curr_y+dy[i]

            # 조건 1. index 초과하면 skip
            if not(0<=temp_x<n and 0<=temp_y<n):
                continue

            # 조건 2. 해당 위치에 돌이 존재하면 skip
            if temp_rocks[temp_x][temp_y]==1:
                continue

            # 조건 3. 이미 방문했다면 skip
            if visited[temp_x][temp_y]==True:
                continue

            visited[temp_x][temp_y]=True
            queue.append((temp_x, temp_y))


choose_rock(0)
print(result)