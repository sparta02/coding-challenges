from collections import deque
n, m = map(int, input().split())
grid = [ list(map(int, input())) for _ in range(n)]


# dp[i][j][k]
# [i][j]까지 고려했을 때
# k=0:벽을 1번도 안부수고 왔을 때
# k=1:벽을 1번 부쉈을 때
# 각각 최단거리
dp= [ [[-1,-1] for _ in range(m)] for _ in range(n) ]


def print_dp():
    for i in range(n):
        for j in range(m):
            print(dp[i][j][0], end=" ")
        print()
    print()
    for i in range(n):
        for j in range(m):
            print(dp[i][j][1], end=" ")
        print()
    print()

# print_dp()

queue=deque()
queue.append((0,0,0))


dp[0][0][0]=1

while queue:
    curr_x, curr_y, curr_k=queue.popleft()
    # print(curr_x, curr_y, curr_k)
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    for i in range(4):
        next_x=curr_x+dx[i]
        next_y=curr_y+dy[i]

        if 0<=next_x<n and 0<=next_y<m:
            # 벽 부수지 않고 그대로 이동
            if grid[next_x][next_y]==0 and dp[next_x][next_y][curr_k]==-1:
                dp[next_x][next_y][curr_k]=dp[curr_x][curr_y][curr_k]+1
                queue.append((next_x, next_y, curr_k))
            # 벽을 부수고 이동
            elif grid[next_x][next_y]==1 and curr_k==0 and dp[next_x][next_y][1]==-1:
                dp[next_x][next_y][1]=dp[curr_x][curr_y][curr_k]+1
                queue.append((next_x, next_y, 1))

# print_dp()

a, b=dp[-1][-1]

if a==b and a==-1:
    print(-1)
elif a==-1:
    print(b)
elif b==-1:
    print(a)
else:
    print(min(a,b))