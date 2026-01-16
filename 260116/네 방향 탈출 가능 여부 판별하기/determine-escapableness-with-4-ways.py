from collections import deque
n, m = map(int, input().split())
snake = [list(map(int, input().split())) for _ in range(n)]
visited=[ [0]*m for _ in range(n) ]
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
# Please write your code here.

queue = deque()

queue.append((0,0))
visited[0][0]=True

def BFS(x,y):

    while queue:
        curr_x, curr_y=queue.popleft()
        #print(curr_x, curr_y)

        # 종료지점 도착시 그만
        if curr_x==n-1 and curr_y==m-1:
            print(1)
            return

        for i in range(4):
            temp_x=curr_x+dx[i]
            temp_y=curr_y+dy[i]

            # 조건1. index를 초과하면 안됨
            if not(0<=temp_x<n and 0<=temp_y<m):
                continue
            
            # 조건2. 뱀이 없어야 함
            if snake[temp_x][temp_y]==0:
                continue
            
            # 조건3. 방문한적이 없어야 함
            if visited[temp_x][temp_y]:
                continue
            
            visited[temp_x][temp_y]=True
            queue.append((temp_x, temp_y))
    print(0)

BFS(0,0)
    