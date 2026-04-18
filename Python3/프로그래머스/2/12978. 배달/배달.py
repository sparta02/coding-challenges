import heapq

def solution(n, road, K):
    answer = 0
    edges=[[] for _ in range(n+1)]
    for s, e, d in road:
        edges[s].append((e, d))
        edges[e].append((s, d))

    INF=10**9
    dist=[INF]*(n+1)
    
    dist[1]=0
    pq=[]
    heapq.heappush(pq, (0, 1))
    
    while pq:
        curr_dist, curr_node=heapq.heappop(pq)
        
        if dist[curr_node]<curr_dist:
            continue
            
        for next_node, next_dist in edges[curr_node]:
            weight=curr_dist+next_dist
            if dist[next_node]>weight:
                dist[next_node]=weight
                heapq.heappush(pq, (weight, next_node))
    
    result=0
    for i in range(n+1):
        if dist[i]<=K:
            result+=1
    return result