n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
def pr():
    global grid,n
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()


def check(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

grid[int(n/2)][int(n/2)]=1
x=int(n/2)
y=int(n/2)
way=0
temp=1
cnt=1
dx, dy= [0,-1,0,1], [1,0,-1,0]

while(cnt<=n*n):
    for j in range(temp):
        cnt+=1
        if cnt>n*n:
            break
        x+=dx[way]
        y+=dy[way]
        grid[x][y]=cnt
        #pr()
    way=(way+1)%4
    for j in range(temp):
        cnt+=1
        if cnt>n*n:
            break
        x+=dx[way]
        y+=dy[way]
        grid[x][y]=cnt
        #pr()
    way=(way+1)%4
    temp+=1

pr()
