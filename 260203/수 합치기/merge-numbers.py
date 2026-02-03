import heapq

n = int(input())
arr = list(map(int, input().split()))


# Please write your code here.
result=0
heapq.heapify(arr)

while (len(arr)>1):
    num1=heapq.heappop(arr)
    num2=heapq.heappop(arr)

    temp_num=num1+num2
    
    heapq.heappush(arr, temp_num)
    result+=temp_num
    #print(arr)

print(result)