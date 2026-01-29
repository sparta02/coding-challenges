import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
pq=[]

for item in arr:
    heapq.heappush(pq, -item)
for _ in range(m)
    temp=heapq.heappop(pq)+1
    heapq.heappush(pq, temp)
print(heapq.heappop(pq)*-1)

