import heapq
n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.

pq=[]

for num in x:
    if num==0:
        if len(pq)==0:
            print(0)
        else:
            print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -num)