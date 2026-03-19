from collections import deque
n, m = map(int, input().split())
ladder=[ list(map(int, input().split())) for _ in range(n)]
snake=[ list(map(int, input().split())) for _ in range(m)]


def portal(num):
    for s, e in ladder:
        if s==num:
            return e
    for s, e in snake:
        if s==num:
            return e
    return num

queue=deque()
queue.append((1,0))
visited=[0]*101
while queue:
    curr, step=queue.popleft()
    visited[curr]=1
    if curr==100:
        print(step)
        break

    for i in range(1, 7):
        next=curr+i
        next=portal(next)
        if 1<=next<=100 and visited[next]==0:
            queue.append((next, step+1))


