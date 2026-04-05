def count_person(total_time, times):
    # total_time내에 몇 명이 심사 가능한지 반환
    return sum([total_time//time for time in times])

def solution(n, times):
    left=0
    right=n*max(times)
    min_idx=n*max(times)+1
    
    while left<=right:
        mid=(left+right)//2
        if count_person(mid, times)>=n:
            min_idx=min(min_idx, mid)
            right=mid-1
        else:
            left=mid+1
    return min_idx