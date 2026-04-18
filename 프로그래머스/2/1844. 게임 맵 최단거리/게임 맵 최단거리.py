from collections import deque

def bfs(maps):
    n=len(maps)
    m=len(maps[0])
    # x좌표, y좌표, 지나온 칸 수
    queue=deque()
    queue.append((0,0,1))
    
    # 방문 여부
    visited=[[0]*m for _ in range(n)]
    visited[0][0]=1
    
    while queue:
        curr_x, curr_y, dist=queue.popleft()
        # print(curr_x, curr_y, dist)
        #목표에 도착했으면
        if (curr_x, curr_y)==(n-1, m-1):
            return dist
        
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            next_x, next_y=curr_x+dx[i], curr_y+dy[i]
            if 0<=next_x<n and 0<=next_y<m and visited[next_x][next_y]==0 and maps[next_x][next_y]:
                visited[next_x][next_y]=1
                queue.append((next_x, next_y, dist+1))
    return -1
                
    
def solution(maps):
    return bfs(maps)