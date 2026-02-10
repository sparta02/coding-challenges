import heapq
n= int(input())

arr=list(map(int, input().split()))

# O(n)
arr2=list(set(arr))
pq=[]

#O(nlogn)
for i in arr2:
    heapq.heappush(pq, i)
#print(pq)

maps={}
#O(nlogn)
for i in range(len(pq)):
    curr=heapq.heappop(pq)
    maps[curr]= i

#print(maps)
# O(n)
for i in arr:
    print(maps[i], end=" ")