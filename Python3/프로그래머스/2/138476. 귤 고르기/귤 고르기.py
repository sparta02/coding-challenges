def solution(k, tangerine):
    answer = 0
    maps={}
    for num in tangerine:
        maps[num]=maps.get(num, 0)+1
    targer_list=list(maps.items())
    targer_list.sort(key= lambda x:(-x[1]))
    i=-1
    while True:
        answer+=1
        i+=1
        if targer_list[i][1]>=k:
            return answer
        k-=targer_list[i][1]
    return answer