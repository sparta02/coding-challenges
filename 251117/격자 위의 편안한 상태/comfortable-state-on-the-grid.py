n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def check(i, j):
    if 0<=i<n and 0<=j<n:
        return True
    return False

arr=[[0]*n for _ in range(n)]
dxs, dys=[1,0,-1,0], [0,-1,0,1]

for point in points:
    x=point[0]-1
    y=point[1]-1
    arr[x][y]=1
    
    cnt=0
    for i in range(4):
        if check(x+dxs[i], y+dys[i]) and arr[x+dxs[i]][y+dys[i]]==1:
            cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)

