import heapq
n, m = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(m)]


edges= [[0]*(n+1) for _ in range(n+1)]
for s, e, d in temp:
    edges[s][e] = d if edges[s][e]==0 or edges[s][e]>d else edges[s][e]
    edges[e][s] = d if edges[e][s]==0 or edges[e][s]>d else edges[e][s]

def print_edges():
    for i in range(1, n+1):
        print(*edges[i][1:])

visited=[0]*(n+1)

pq=[(0, 1)]

result=0
while pq:
    cost, curr=heapq.heappop(pq)
    
    if visited[curr]==1:
        continue
    # print(cost, curr)
    visited[curr]=1
    result+=cost

    for i in range(1, n+1):
        next_cost=edges[curr][i]
        # print(f"i:{i}")
        if next_cost==0 or visited[i]==1:
            continue
        heapq.heappush(pq, (next_cost, i))

print(result)

    