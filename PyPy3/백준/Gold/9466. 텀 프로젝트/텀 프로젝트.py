import sys
sys.setrecursionlimit(100000)
result=0
t=int(input())

def dfs(num, visited, arr):
    global result
    visited[num]=1
    next= arr[num]

    if visited[next]==0:
        dfs(next, visited, arr)
    elif visited[next]==1:
        # 사이클 시작
        cur=next
        while True:
            result -= 1
            cur = arr[cur]
            if cur == next:
                break

    visited[num] = 2


for _ in range(t):
    n=int(input())
    arr=[0]+list(map(int, input().split()))

    visited=[0]*(n+1)
    result=n
    for i in range(1, n+1):
        if visited[i]==0:
            dfs(i, visited, arr)

    print(result)