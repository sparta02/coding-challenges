N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

def check(x, y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

def check_LEE(x, y):
    temp=0
    dx, dy=[1,0,-1,0,1,1,-1,-1], [0,1,0,-1,1,-1,1,-1]
    if arr[x][y]=="L":
        for j in range(8):
            if check(x+dx[j], y+dy[j]) and check(x+dx[j]+dx[j], y+dy[j]+dy[j]) and arr[x+dx[j]][y+dy[j]]=="E" and arr[x+dx[j]+dx[j]][y+dy[j]+dy[j]]=="E":
                temp+=1
    return temp

result=0
for i in range(N):
    for j in range(M):
        result+=check_LEE(i, j)

print(result)
        
        
