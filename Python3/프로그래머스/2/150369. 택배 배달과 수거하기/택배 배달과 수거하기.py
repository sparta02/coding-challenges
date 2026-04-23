def calc_index(i, j, deliveries, pickups):
    while i >= 0 and deliveries[i] == 0:
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1
    return i, j

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    i, j = n - 1, n - 1
    i, j = calc_index(i, j, deliveries, pickups)
    
    while i >= 0 or j >= 0:
        answer += (max(i, j) + 1) * 2
        
        d_cap, p_cap = cap, cap
        
        # 배달
        while i >= 0 and d_cap > 0:
            if deliveries[i] <= d_cap:
                d_cap -= deliveries[i]
                deliveries[i] = 0
                i -= 1
            else:
                deliveries[i] -= d_cap
                d_cap = 0
        
        # 수거
        while j >= 0 and p_cap > 0:
            if pickups[j] <= p_cap:
                p_cap -= pickups[j]
                pickups[j] = 0
                j -= 1
            else:
                pickups[j] -= p_cap
                p_cap = 0
        
        i, j = calc_index(i, j, deliveries, pickups)
    
    return answer