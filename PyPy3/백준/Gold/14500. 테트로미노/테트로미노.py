n, m = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(n)]
result=0

def check1(x, y):
    global result
    result=max(result, sum(grid[i][j:j+4]))

def check2(x, y):
    global result
    temp=0
    for i in range(4):
        temp+=grid[x+i][y]
    result=max(result, temp)

def check3(x, y):
    global result
    temp=0
    for i in range(2):
        for j in range(2):
            temp+=grid[x+i][y+j]
    result=max(result, temp)

def check4(x, y):
    global result
    temp=0
    for i in range(2):
        for j in range(3):
            temp+=grid[x+i][y+j]
    direct=[[(0,1),(0,2)],[(0,0),(0,1)],[(0,2),(1,0)],[(0,0),(1,2)],[(1,1),(1,2)],[(1,0),(1,2)],[(1,0),(1,1)],[(0,0),(0,2)]]
    for i in range(8):
        new_temp=temp
        new_temp-=grid[x+direct[i][0][0]][y+direct[i][0][1]]
        new_temp-=grid[x+direct[i][1][0]][y+direct[i][1][1]]
        result=max(result, new_temp)

def check5(x, y):
    global result
    temp=0
    for i in range(3):
        for j in range(2):
            temp+=grid[x+i][y+j]
    direct=[[(0,0),(2,1)],[(0,1),(2,0)],[(0,0),(2,0)],[(0,1),(2,1)],[(1,1),(2,1)],[(0,1),(1,1)],[(1,0),(2,0)],[(0,0),(1,0)]]
    for i in range(8):
        new_temp=temp
        new_temp-=grid[x+direct[i][0][0]][y+direct[i][0][1]]
        new_temp-=grid[x+direct[i][1][0]][y+direct[i][1][1]]
        result=max(result, new_temp)

# 1x4
for i in range(n):
    for j in range(m-3):
        check1(i, j)
# 4x1
for i in range(n-3):
    for j in range(m):
        check2(i, j)
# 2x2
for i in range(n-1):
    for j in range(m-1):
        check3(i, j)
# 2x3
for i in range(n-1):
    for j in range(m-2):
        check4(i, j)
# 3x2
for i in range(n-2):
    for j in range(m-1):
        check5(i, j)

print(result)