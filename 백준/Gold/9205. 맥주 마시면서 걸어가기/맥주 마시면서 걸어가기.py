import sys
input=sys.stdin.readline

def dfs():
    visited=[0]*n
    stack=[(start[0], start[1])]

    while stack:
        curr_x, curr_y = stack.pop()
        if abs(end[0]-curr_x)+abs(end[1]-curr_y) <=1000:
            print('happy')
            return
        
        for i, (next_x, next_y) in enumerate(mart):
            dist= abs(curr_x-next_x)+abs(curr_y-next_y)
            if 0<dist<=1000 and visited[i]==0:
                stack.append((next_x, next_y))
                visited[i]=1
                
    print('sad')


t = int(input().strip())
for _ in range(t):
    n=int(input().strip())
    start=list(map(int, input().split()))
    mart=[]
    for _ in range(n):
        mart.append(list(map(int, input().split())))
    end=list(map(int, input().split()))

    dfs()