def solution(progresses, speeds):
    answer = []
    
    j=0
    n=len(progresses)
    for i in range(1, 101):
        temp=0
        while j<n:
            if progresses[j]+i*speeds[j]>=100:
                j+=1
                temp+=1
            else:
                break
        if temp:
            answer.append(temp)
    
    return answer