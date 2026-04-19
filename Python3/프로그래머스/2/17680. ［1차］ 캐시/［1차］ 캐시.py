from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    queue=deque()
    
    for next in cities:
        next_refine=next.upper()
        if next_refine in queue:
            answer+=1
            new_queue=deque()
            for i in range(len(queue)):
                temp=queue.popleft()
                if temp!=next_refine:
                    new_queue.append(temp)
            new_queue.append(next_refine)
            queue=new_queue
        else:
            answer+=5
            if len(queue)<cacheSize:
                queue.append(next_refine)
            else:
                queue.append(next_refine)
                queue.popleft()
    
    return answer