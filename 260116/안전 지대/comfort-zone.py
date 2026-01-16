n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited= [ [0] *m for _ in range(n)  ]
result_count=-1
result_k=-1

# 위, 오른쪽, 아래, 왼쪽
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def print_visited():
    for i in range(n):
        for j in range(m):
            print(visited[i][j], end=" ")
        print()
    print()

# visited 행렬 초기화
def reset_visited():
    global visited
    visited= [ [0] *m for _ in range(n)  ]

def set_visited_k(k):
    for i in range(n):
        for j in range(m):
            if grid[i][j]<=k:
                visited[i][j]=True


def dps(x, y):
    stack=[(x,y)]
    visited[x][y]=True
    #print_visited()
    
    while stack:
        nx, ny=stack.pop()
        for i in range(4):
            temp_x = nx + dx[i]
            temp_y = ny + dy[i]
            # 인덱스 벗어나면 skip
            if not (0<=temp_x<n and 0<=temp_y<m):
                continue

            # 다음 칸이 True면 skip
            if visited[temp_x][temp_y]==True:
                continue
            visited[temp_x][temp_y]=True
            stack.append((temp_x, temp_y))


# 4. 메인 로직 (기존 루프 구조 유지)
# 격자 내 최대 높이 확인
max_h = 0
for row in grid:
    for val in row:
        if val > max_h:
            max_h = val

for hi in range(1, max_h + 1):
    reset_visited()
    
    set_visited_k(hi)
    
    temp_count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                temp_count += 1
                dps(i, j)
    
    if result_count < temp_count:
        result_count = temp_count
        result_k = hi

# 최종 결과 출력
print(result_count, result_k)