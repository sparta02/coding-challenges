from collections import deque
n = int(input())
time = [0]
edges=[ [] for _ in range(n+1)]
indegree= [0]*(n+1)
for i in range(1, n+1):
    line = list(map(int, input().split()))
    time.append(line[0])
    temp=line[2:]
    for curr in temp:
        indegree[i]+=1
        edges[curr].append(i)


# print(time[1:])

queue=deque()
for i in range(1, n+1):
    if indegree[i]==0:
        queue.append(i)

dp=[0]*(n+1)
while queue:
    
    curr = queue.popleft()
    # print(f"현재:{curr}")

    for next in edges[curr]:
        # print(f"다음:{next}")
        indegree[next]-=1
        dp[next]=max(dp[next], time[curr])
        # print(dp[1:])
        if indegree[next]==0:
            # print(f"{next} 추가완료")
            time[next]=time[next]+dp[next]
            # print(time[1:])
            queue.append(next)

# print(time[1:])
print(max(time))