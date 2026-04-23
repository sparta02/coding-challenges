def solution(sequence, k):
    answer = []
    n=len(sequence)
    
    j=0
    curr_sum=0
    for i in range(n):
        while j<n and curr_sum+sequence[j]<=k:
            curr_sum+=sequence[j]
            j+=1
            
        # print(i,j, curr_sum)
        if curr_sum==k:
            if len(answer)==0:
                answer=[i,j-1]
            else:
                if (j-1-i)<answer[1]-answer[0]:
                    answer=[i,j-1]
            
        curr_sum-=sequence[i]
    
    
    return answer