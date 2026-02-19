r, c = map(int, input().split())
grid=[]

for _ in range(r):
    grid.append(list(input()))



result=0
# DFS 방식으로 풀이
# x좌표, y좌표, depth

visited_alpha={grid[0][0]:1}
visited= [ [0]*c for _ in range(r)]
visited[0][0]=1

def dfs(x, y, depth):
    # print(x, y, depth)
    # print(visited_alpha.keys())
    global result
    result=max(result, depth)

    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    # 상하좌우 탐색
    for i in range(4):
        next_x, next_y=x+dx[i], y+dy[i]
        
        # index가 초과하는지 확인
        if 0<=next_x<r and 0<=next_y<c:
            next_alpha=grid[next_x][next_y]
            # 방문하지 않은 알파벳인지 확인
            if next_alpha not in visited_alpha:
                #방문하지 않은 칸인지 확인
                if visited[next_x][next_y]==0:
                    visited[next_x][next_y]=1

                    visited_alpha[next_alpha]=1
                    dfs(next_x, next_y, depth+1)
                    visited_alpha.pop(next_alpha)
                    visited[next_x][next_y]=0
dfs(0,0,1)
print(result)