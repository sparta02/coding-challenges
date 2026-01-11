n, m, t, k = map(int, input().split())

balls=[]
for i in range(m):
    ri, ci, di, vi = input().split()
    r=[]
    r.append(int(ri)-1)
    r.append(int(ci)-1)
    if di=='U':
        r.append(0)
    elif di=='R':
        r.append(1)
    elif di=='D':
        r.append(2)
    elif di=='L':
        r.append(3)
    r.append(int(vi))
    r.append(i)
    balls.append(r)

# 위, 오른쪽, 아래, 왼쪽
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

# 행렬 출력
def print_grid(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()



# 각 시간에 대해
for time in range(2):
    #print(balls)
    # 각 공에 대해 이동
    next_grid=[[0]*n for _ in range(n)]
    for i in range(len(balls)):
        #print(balls[i][0], balls[i][1], balls[i][2], balls[i][3])
        for d in range(balls[i][3]):
            if not (0<=balls[i][0]+dx[balls[i][2]]<n and 0<=balls[i][1]+dy[balls[i][2]]<n):
                balls[i][2]=(balls[i][2]+2)%4
            balls[i][0]+=dx[balls[i][2]]
            balls[i][1]+=dy[balls[i][2]]
            # print(x, y)
        next_grid[balls[i][0]][balls[i][1]]+=1
    #print_grid(next_grid)
    
        
    # 재정렬
    grid= [[] for _ in range(n*n)]
    for x, y, way, dist, num in balls:
        grid[x*n+y].append(balls[num])
    #print(grid)
    
    new_balls=[]
    for i in range(n*n):
        if 0<len(grid[i])<=k:
            new_balls+=grid[i]

        if k<len(grid[i]):
            temp_list=grid[i]

            temp_list=sorted(temp_list, key=lambda x:(-x[3], x[4]))
            #print(temp_list)
            for j in range(k):
                new_balls.append(temp_list[j])
    
    balls=new_balls[:]
    #print(balls)
print(len(balls))