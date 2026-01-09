T = int(input())

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end=" ")
        print()
    print()


# 위, 오른쪽, 아래, 왼쪽
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for _ in range(T):
    n, m = map(int, input().split())
    balls=[]

    for _ in range(m):
        xi, yi, di = input().split()
        x=int(xi)-1
        y=int(yi)-1

        # 위, 오른쪽, 아래, 왼쪽
        if di=="U":
            d=0
        elif di=="R":
            d=1
        elif di=="D":
            d=2
        elif di=="L":
            d=3
        list=[x,y,d]
        balls.append([x,y,d])
    # print(balls)

    for time in range(5):
        # print(f"{time+1}번째 시도")
        count_list=[[0]*n for _ in range(n)]
        for i in range(len(balls)):
            #i번째 ball 이동
            #balls[i][0]: x좌표
            #balls[i][1]: y좌표
            #balls[i][2]: 방향

            #벽에 닿는다면 방향 바꾸기
            if not (0<=balls[i][0]+dx[balls[i][2]]<n and 0<=balls[i][1]+dy[balls[i][2]]<n):
                balls[i][2]= (balls[i][2]+2)%4
            #아니라면 이동
            else:
                balls[i][0]+=dx[balls[i][2]]
                balls[i][1]+=dy[balls[i][2]]
            count_list[balls[i][0]][balls[i][1]]+=1

        # print_grid(count_list)
        # print("움직인 후 공들")
        # print(balls)

        new_balls=[]
        for i in range(len(balls)):
            if count_list[balls[i][0]][balls[i][1]] ==1:
                new_balls.append(balls[i])
        

        balls=[row[:] for row in new_balls]
        # print("중복 제거 후 공들")
        # print(balls)

    print(len(balls))


        

    
        