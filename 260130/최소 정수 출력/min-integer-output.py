import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
dp=[]

for num in x:
    if num==0:
        if len(dp)==0:
            print(0)
        else:
            print(heapq.heappop(dp))
    else:
        heapq.heappush(dp, num)