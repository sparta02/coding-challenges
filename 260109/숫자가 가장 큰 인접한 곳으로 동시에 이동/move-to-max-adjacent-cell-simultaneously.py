n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]

# count_list 설정
count_list= [[0]*n for _ in range(n)]
for i in range(m):
    count_list[r[i]][c[i]]=1


def print_grid(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()

#print("처음: ")
#print_grid(count_list)


for time in range(t):
    # 우, 좌, 하, 상 순서로
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0, 0]

    new_count_list= [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if count_list[x][y]==1:
                temp_way=0
                temp_value=-1
                #print(f"x:{x}, y:{y}")
                for way in range(4):
                    if 0<=(x+dx[way])<n and 0<=(y+dy[way])<n:
                        #print(f"{x+dx[way]}, {y+dy[way]} 체크")
                        if temp_value < a[x+dx[way]][y+dy[way]]:
                            temp_way=way
                            temp_value=a[x+dx[way]][y+dy[way]]
                        #print(temp_value)
                new_count_list[x+dx[temp_way]][y+dy[temp_way]]+=1
    
    #print(f"{time+1}번째")
    #print_grid(new_count_list)


    for x in range(n):
        for y in range(n):
            if new_count_list[x][y]>1:
                new_count_list[x][y]=0
    count_list=[ row[:] for row in new_count_list]
    #print_grid(count_list)

result=0
for x in range(n):
        for y in range(n):
            result+=count_list[x][y]

print(result)