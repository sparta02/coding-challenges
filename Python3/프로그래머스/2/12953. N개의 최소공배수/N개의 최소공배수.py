def solution(arr):
    minor=[0]*100
    n = len(arr)
    
    for i in range(n):
        temp_minor=[0]*100
        curr=arr[i]
        
        while curr!=1:
            for j in range(2, 100):
                if curr%j==0:
                    temp_minor[j]+=1
                    curr//=j
                    break
        for k in range(2, 100):
            minor[k]=max(temp_minor[k], minor[k])
        
    result=1
    for i in range(2, 100):
        if minor[i]>=1:
            result*=i**minor[i]
    return result