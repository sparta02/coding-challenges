import heapq

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

pq=[]
for num in arr:
    heapq.heappush(pq, -num)

while(len(pq)>1):
    num1=-heapq.heappop(pq)
    num2=-heapq.heappop(pq)
    
    if (num1-num2)!=0:
        heapq.heappush(pq, -abs(num1-num2))

print(-1 if len(pq)==0 else -pq[0])

