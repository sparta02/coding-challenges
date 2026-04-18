def solution(clothes):
    
    maps={}
    
    for _, name in clothes:
        maps[name]=maps.get(name, 0)+1
    
    answer = 1
    for item, value in maps.items():
        answer*=(value+1)
    return answer-1