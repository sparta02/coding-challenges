n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 기본 방향 설정
# 우, 하, 좌, 상
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

# 현재 좌표, 방향
x=-1
y=-1
way=-1

def meet_1():
    global way
    if way==0:
        way+=3
    elif way==1:
        way+=1
    elif way==2:
        way-=1
    elif way==3:
        way-=3

def meet_2():
    global way
    if way==0:
        way+=1
    elif way==1:
        way-=1
    elif way==2:
        way+=1
    elif way==3:
        way-=1


def start():
    global x
    global y
    count=1
    while(1):
        x+=dx[way]
        y+=dy[way]
        count+=1

        if not (0<=x<n and 0<=y<n):
            break

        if grid[x][y]==1:
            meet_1()
        elif grid[x][y]==2:
            meet_2()
    return count

result=0
400*100*100

#위에서
for i in range(n):
    x=0
    y=i
    way=1
    #print(f"x:{x}, y:{y}, way:{way}")
    count=start()
    #print(f"count:{count}")
    result= max(result, count)

#오른쪽에서
for i in range(n):
    x=i
    y=n-1
    way=2
    #print(f"x:{x}, y:{y}, way:{way}")
    count=start()
    #print(f"count:{count}")
    result= max(result, count)

#아래에서
for i in range(n):
    
    x=n-1
    y=i
    way=3
    #print(f"x:{x}, y:{y}, way:{way}")
    count=start()
    #print(f"count:{count}")
    result= max(result, count)

#왼쪽에서
for i in range(n):
    x=i
    y=0
    way=0
    #print(f"x:{x}, y:{y}, way:{way}")
    count=start()
    #print(f"count:{count}")
    result= max(result, count)

print(result)