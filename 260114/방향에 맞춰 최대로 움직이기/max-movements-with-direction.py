n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

dx=[0, -1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 0, 1, 1, 1, 0, -1, -1, -1]

result=0

def move(x, y, count):
    global result


    way= move_dir[x][y]
    #print(f"x:{x}, y:{y}, way:{way}")
    temp_list=[]
    # 1. 다음으로 이동 가능한 곳들 찾기
    find_x, find_y=x,y
    while(1):
        find_x+=dx[way]
        find_y+=dy[way]
        # print(find_x, find_y)
        if not (0<=find_x<n and 0<=find_y<n):
            break
        if num[x][y]>=num[find_x][find_y]:
            continue
        
        temp_list.append([find_x, find_y])
    #print(f"이동 가능한 곳들: {temp_list}")
    
    if len(temp_list)==0:
        #print(f"count:{count}")
        result=max(result, count)
        return
    
    for i in range(len(temp_list)):
        move(temp_list[i][0], temp_list[i][1], count+1)

move(r-1, c-1, 0)

print(result)
        