n, m = map(int, input().split())

# Please write your code here.

arr=[[0]*m for _ in range(n)]
# Please write your code here.
def pr():
    global arr,n,m
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print()


def check(x, y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

arr[0][0]='A'
x=0
y=0
way=0
dx, dy= [0,1,0,-1], [1,0,-1,0]
for i in range(2, n*m+1):
    if check(x+dx[way], y+dy[way])==False or arr[x+dx[way]][y+dy[way]]!=0:
        way=(way+1)%4
    x+=dx[way]
    y+=dy[way]
    arr[x][y]=chr((i)%26+64)

pr()

