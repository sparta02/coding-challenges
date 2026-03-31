import sys
input=sys.stdin.readline


n, m = map(int, input().split())
friends= [ list(map(int, input().split())) for _ in range(m)]
visited=[0]*n

edges=[ [] for _ in range(n)]

for s, e in friends:
    edges[s].append(e)
    edges[e].append(s)

# print(edges)


def dfs(num, cnt):
    if cnt==5:
        print(1)
        sys.exit()
    # print(f"curr:{num}, cnt:{cnt}")
    for next in edges[num]:
        if visited[next]==0:
            visited[next]=1
            dfs(next, cnt+1)
            visited[next]=0

for i in range(n):
    # print(f"start{i}")
    visited=[0]*n
    visited[i]=1
    dfs(i, 1)

print(0)
