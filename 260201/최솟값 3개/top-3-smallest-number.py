
import heapq
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

pq=[]
for i in range(n):
    heapq.heappush(pq, arr[i])
    if i<=1:
        print(-1)
    else:
        num1=heapq.heappop(pq)
        num2=heapq.heappop(pq)
        num3=heapq.heappop(pq)

        print(num1*num2*num3)

        heapq.heappush(pq, num1)
        heapq.heappush(pq, num2)
        heapq.heappush(pq, num3)
    
    