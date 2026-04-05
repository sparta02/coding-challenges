from collections import deque

def print_com(computers):
    for i in range(len(computers)):
        print(*computers[i])

def bfs(start, computers, visited):
    visited[start]=1
    queue=deque()
    queue.append(start)
    
    while queue:
        curr=queue.popleft()
        for i in range(len(computers)):
            if curr!=i and visited[i]==0 and computers[curr][i]==1:
                visited[i]=1
                queue.append(i)
    # print(visited)
        
def solution(n, computers):
    answer=0
    visited=[0]*n
    for i in range(n):
        if visited[i]==0:
            bfs(i, computers, visited)
            answer+=1
        
    
    return answer