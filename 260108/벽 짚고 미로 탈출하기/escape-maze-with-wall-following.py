N = int(input())
x, y = map(int, input().split())
x-=1
y-=1

grid = [list(input()) for _ in range(N)]
# print(grid)

# 0. 시작 점으로 돌아온다면 탈출이 불가능 하다는 것
start_x=x
start_y=y

# 현재 방향: 0~3
# 시계방향으로 90도 회전: +1
# 반시계방향으로 90도 회전: -1
i=0
# 1. 바라보는 방향, 우, 하, 좌, 상
dx_look=[0, 1, 0, -1]
dy_look=[1, 0, -1, 0]

# 2. 내 오른쪽 위치: 하, 좌, 상, 우
dx_right=[1, 0, -1, 0]
dy_right=[0, -1, 0, 1]

# print(f"x:{x}, y:{y}, i:{i}")
result=0

사면초가=0
while(1):

    # Step 1: 바라보고 있는 방향이 벽으로 막혀 있는 경우
    if 0<=(x+dx_look[i])<N and 0<=(y+dy_look[i])<N:
        if grid[x+dx_look[i]][y+dy_look[i]]=="#":
            i=(i-1)%4
            # print("막혀있음")
            # print(f"x:{x}, y:{y}, i:{i}")
            사면초가+=1
            if 사면초가==4:
                print(-1)
                break
            continue
    
    # Step 2: 이동이 가능한 경우
    # 우선 이동 후 판단
    x+=dx_look[i]
    y+=dy_look[i]
    result+=1
    사면초가=0
    # print(f"x:{x}, y:{y}, i:{i}")

    # 이동한 곳이 격자 밖이면 종료
    if x<0 or x>=N or y<0 or y>=N:
        print(result)
        break
    
    # 이동한 곳이 시작 위치면 종료
    if x== start_x and y==start_y:
        print(-1)
        break

    # 만약 오른쪽에 그대로 벽이 없으면 회전 후 이동
    if 0<=x+dx_right[i]<N and 0<=y+dy_right[i]<N:
        if grid[x+dx_right[i]][y+dy_right[i]]==".":
            i=(i+1)%4
            x+=dx_look[i]
            y+=dy_look[i]
            result+=1
            # print("오른쪽에 벽이 없음")
            # print(f"x:{x}, y:{y}, i:{i}")
            사면초가=0

    # 이동한 곳이 격자 밖이면 종료
    if x<0 or x>=N or y<0 or y>=N:
        print(result)
        break
    
    # 이동한 곳이 시작 위치면 종료
    if x== start_x and y==start_y:
        print(-1)
        break