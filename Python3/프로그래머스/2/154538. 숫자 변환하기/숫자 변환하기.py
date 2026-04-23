from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue=deque()
    queue.append((x, 0))
        
    visited=[0]*1000001
    visited[x]=1
    
    while queue:
        curr, dist=queue.popleft()
        
        if curr==y:
            return dist
        
        if 1<=curr+n<=1000000 and visited[curr+n]==0:
            visited[curr+n]=1
            queue.append((curr+n,dist+1))
        if 1<=curr*2<=1000000 and visited[curr*2]==0:
            visited[curr*2]=1
            queue.append((curr*2,dist+1))
        if 1<=curr*3<=1000000 and visited[curr*3]==0:
            visited[curr*3]=1
            queue.append((curr*3,dist+1))
        
        
    
    return -1