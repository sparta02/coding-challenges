def solution(n, words):
    answer = []
    
    maps=set()
    last_word=words[0][0]
    idx=-1
    
    for i in range(len(words)):
        # 1. 글자가 다르거나
        if words[i][0]!=last_word:
            idx=i
            break
        # 2. 이미 나온거면 중단
        if words[i] in maps:
            idx=i
            break
        maps.add(words[i])
        last_word=words[i][-1]
    print(idx)
    if idx==-1:
        return [0, 0]
    
    return [idx%n+1, ((idx)//n)+1]