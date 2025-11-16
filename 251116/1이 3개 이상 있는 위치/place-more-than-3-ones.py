n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs, dys = [1,0,-1,0], [0,-1,0,1]

def check(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

cnt=0
for i in range(n):
    for j in range(n):
        temp=0
        for dx, dy in zip(dxs, dys):
            if check(i+dx, j+dy)==True and grid[i+dx][j+dy]==1:
                temp+=1
        if temp>=3:
            cnt+=1


print(cnt)