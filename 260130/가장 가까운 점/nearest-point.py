import heapq
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
pq=[]

for x, y in points:
    #print(x,y)
    heapq.heappush(pq, (x+y,x,y))
    #print(pq)

for i in range(m):
    (x_y,x,y)=heapq.heappop(pq)
    heapq.heappush(pq, (x+y+4,x+2,y+2))
    #print(pq)
(x_y,x,y)=heapq.heappop(pq)
print(x,y)