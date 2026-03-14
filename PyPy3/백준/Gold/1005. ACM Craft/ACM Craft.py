from collections import deque
t= int(input())
for _ in range(t):
    n, k = map(int, input().split())
    times=list(map(int, input().split()))
    times=[0]+times
    edges=[ [] for _ in range(n+1)]
    indegree=[0]*(n+1)

    for _ in range(k):
        s, e = map(int, input().split())
        edges[s].append(e)
        indegree[e]+=1
    
    target = int(input())

    # print(edges[1:])
    # print(indegree[1:])
    
    queue=deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            queue.append(i)

    dp=[0]*(n+1)
    while queue:
        curr=queue.popleft()

        for next in edges[curr]:
            indegree[next]-=1
            dp[next]=max(dp[next], times[curr])

            if indegree[next]==0:
                times[next]+=dp[next]
                queue.append(next)
    
    print(times[target])