from collections import deque

n, m= map(int, input().split())

# 입력 받은 arr
arr=[ list(map(int, input().split())) for _ in range(n)]

# 결과로 출력할 arr
result_arr=[ [-1]*m for _ in range(n)]

# 시작위치 찾기
x=-1
y=-1
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            x=i
            y=j

queue=deque()
queue.append((x,y))
result_arr[x][y]=0

while(queue):
    curr_x, curr_y=queue.popleft()
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    for i in range(4):
        temp_x=curr_x+dx[i]
        temp_y=curr_y+dy[i]
        if 0<=temp_x<n and 0<=temp_y<m:
            if result_arr[temp_x][temp_y]==-1 and arr[temp_x][temp_y]==1:
                result_arr[temp_x][temp_y]=result_arr[curr_x][curr_y]+1
                queue.append((temp_x, temp_y))

for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            result_arr[i][j]=0

for i in range(n):
    for j in range(m):
        print(result_arr[i][j], end=" ")
    print()
print()
