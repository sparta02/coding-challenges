import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
pq=[]

for num in x:
    if num!=0:
        heapq.heappush(pq, (abs(num), num))
    else:
        if len(pq)==0:
            print(0)
        else:
            _, curr_num=heapq.heappop(pq)
            print(curr_num)
        