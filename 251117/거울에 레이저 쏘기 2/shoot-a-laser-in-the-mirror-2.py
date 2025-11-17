n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
x=0
y=0
way=0

dxs, dys=[1,0,-1,0], [0,-1,0,1]

    #↓(0) -> →(3)
    #↑(2) -> ←(1)
    #→(3) -> ↓(0)
    #←(1) -> ↑(2)
def right_down():
    global x
    global y
    global way
    if way==0 or way==2: # way+3
        way=(way+3)%4
        x+=dxs[way]
        y+=dys[way]

    else: # way==1 or 3-> way+1
        way=(way+1)%4
        x+=dxs[way]
        y+=dys[way]
        

    #↓(0) -> ←(1)
    #↑(2) -> →(3)
    #→(3) -> ↑(2)
    #←(1) -> ↓(0)
def right_up():
    global x
    global y
    global way
    if way==0 or way==2: # way+1
        way=(way+1)%4
        x+=dxs[way]
        y+=dys[way]
        
    else: # way==1 or 3-> way+2
        way=(way+3)%4
        x+=dxs[way]
        y+=dys[way]
        

# 초기 세팅
def test(n, k):
    global x
    global y
    if k<=n:
        x=0
        y=k-1
        way=0
    elif k<=2*n:
        x=(k%n-1)%n
        y=n-1
        way=1
    elif k<=3*n:
        x=n-1
        y=(n-(k%n))%n
        way=2
    else:
        x=(n-k%n)%n
        y=0
        way=3

test(n, k)

def check(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

cnt=1
while True:
    #print(x, y, grid[x][y], way, cnt)
    if grid[x][y]=='/':
        right_up()
    else:
        right_down()

    if check(x, y)==False:
        print(cnt)
        break
    cnt+=1
    #print(x, y, way, cnt)