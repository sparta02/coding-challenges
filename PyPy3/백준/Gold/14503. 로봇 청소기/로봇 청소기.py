n, m = map(int, input().split())
temp=list(map(int, input().split()))
r, c = temp[:2]
direct=temp[-1]
grid=[ list(map(int, input().split())) for _ in range(n)]

if direct==1:
    direct=3
elif direct==3:
    direct=1

# 북 서 남 동
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]

def print_grid():
    for i in range(n):
        print(*grid[i])

# 주변 4칸 중 청소되지 않은 빈칸이 있는지 확인
def find(x, y):
    for i in range(4):
        next_x=x+dx[i]
        next_y=y+dy[i]
        if 0<=next_x<n and 0<=next_y<m and grid[next_x][next_y]==0:
            return True
    return False

# 로봇청소기가 청소하는 전체 칸 수
result=0

while True:
# while True:
    # print(f"x:{r}, y:{c}, direct:{direct}")
    # print_grid()
    # print()

    # 1. 현재 칸이 아직 청소되지 않은 경우, 청소
    if grid[r][c]==0:
        grid[r][c]=2
        result+=1
    
    # 2. 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    if find(r, c)==False:
        # 2-1. 후진이 가능한 경우
        # 후진 방향
        back_x, back_y = dx[(direct+2)%4], dy[(direct+2)%4]
        if 0<=r+back_x<n and 0<=c+back_y<m and grid[r+back_x][c+back_y]!=1:
            r+=back_x
            c+=back_y
            # print(f"x:{r}, y:{c}, direct:{direct}")
            # print_grid()
            # print()
            continue
            
        # 2-2. 후진이 불가능한 경우
        else:
            break
    # 3. 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
    else:
        for i in range(4):
            # 반시계 방향으로 회전
            direct=(direct+1)%4
            next_r, next_c=r+dx[direct], c+dy[direct]
            # print(f"check, {next_r}, {next_c}, {grid[next_r][next_c]}")
            if 0<=next_r<n and 0<=next_c<m and grid[next_r][next_c]==0:
                # print(f"ok, {next_r}, {next_c}")
                r=next_r
                c=next_c
                # print(f"x:{r}, y:{c}, direct:{direct}")
                # print_grid()
                # print()
                break

print(result)

