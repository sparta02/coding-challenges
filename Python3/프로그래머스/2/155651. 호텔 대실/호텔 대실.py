def solution(book_time):
    arr=[0]*(60*25)
    
    for start, end in book_time:
        # print(start, end)
        start_temp=int(start[:2])*60+int(start[-2:])
        end_temp=int(end[:2])*60+int(end[-2:])+10
        # print(start_temp, end_temp)
        arr[start_temp]+=1
        arr[end_temp]-=1
    answer = 0
    temp=0
    for i in range(60*25):
        temp+=arr[i]
        answer=max(answer, temp)
    
    return answer