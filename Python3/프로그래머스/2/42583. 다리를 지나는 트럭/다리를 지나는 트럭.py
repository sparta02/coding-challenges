from collections import deque
def solution(bridge_length, max_weight, truck_list):
    answer = 0

    queue=deque()
    for i in range(bridge_length):
        queue.append(0)
    print(queue)
    curr_weight=0
    while True:
        answer+=1
        curr_weight-=queue.pop()
        if truck_list and curr_weight+truck_list[0]<=max_weight:
            queue.appendleft(truck_list[0])
            curr_weight+=truck_list.pop(0)
        else:
            queue.appendleft(0)
        
        if curr_weight==0 and len(truck_list)==0:
            break
    return answer