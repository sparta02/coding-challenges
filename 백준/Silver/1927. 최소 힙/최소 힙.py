import heapq
import sys
input=sys.stdin.readline

n=int(input())
pq=[]
for _ in range(n):
    com=int(input())

    if com==0:
        if len(pq)==0:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, com)