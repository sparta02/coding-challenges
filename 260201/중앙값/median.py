import heapq
t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    # 중앙값보다 작은 숫자들
    pq_down=[]
    # 중앙값보다 큰 숫자들
    pq_up=[]

    mid_num=arr[0]
    print(mid_num, end=" ")
    
    for i in range(1, m):
        if arr[i]<mid_num:
            heapq.heappush(pq_down, -arr[i])
        else:
            heapq.heappush(pq_up, arr[i])

        # 홀수 번째
        if i%2==0:
            # print(pq_down)
            # print(pq_up)
            
            if len(pq_down)==len(pq_up):
                print(mid_num, end=" ")
            else:
                while(len(pq_down)!=len(pq_up)):
                    if len(pq_down)>len(pq_up):
                        temp_num=-heapq.heappop(pq_down)
                        heapq.heappush(pq_up, -mid_num)
                        mid_num=temp_num
                        
                    elif len(pq_down)<len(pq_up):
                        temp_num=heapq.heappop(pq_up)
                        heapq.heappush(pq_down, mid_num)
                        mid_num=temp_num
                
                print(mid_num, end=" ")
    print()


    
# 처음에 1을 중앙값으로 잡고
# 큰 pq, 작은 pq 만들어서
# [ ], 1,[2, 3]
# 길이가 다르니
# 1. 큰 곳에서 pop
# [ ], 1, 2, [3]
# 2. 기존 중앙값 작은 곳에 넣기 [1], 2, [3]