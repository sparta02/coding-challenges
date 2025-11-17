R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
cnt=0
x=0
y=0

def check(a,b):
    global R,C, grid
    if current != grid[a][b]:
        return True
    return False

for i in range(1, R-2):
    for j in range(1, C-2):
        x=0
        y=0
        current=grid[0][0]
        if check(x+i, y+j)==False:
            continue
        x+=i
        y+=j
        current=grid[x][y]
        c2=current
        #print(x, y, R-1-x, C-1-y)
        for k in range(1, R-1-x):
            for q in range(1, C-1-y):
                current=c2
                if check(x+k, y+q)==False:
                    continue
                x2=x+k
                y2=y+q
                current=grid[x2][y2]
                #print(x2,y2, grid[x2][y2])
            
                if R>x2 and C>y2 and check(R-1, C-1):
                    cnt+=1

print(cnt)
