def solution(edges):
    # 각 정점의 [in, out] 차수를 기록할 딕셔너리
    counts = {}
    for a, b in edges:
        if a not in counts: counts[a] = [0, 0]
        if b not in counts: counts[b] = [0, 0]
        counts[a][1] += 1 # out-degree
        counts[b][0] += 1 # in-degree
    
    res = [0, 0, 0, 0]
    for node, (inc, outc) in counts.items():
        # 생성된 정점 찾기
        if inc == 0 and outc >= 2:
            res[0] = node
        # 막대 모양 찾기 (끝점의 특징)
        elif outc == 0:
            res[2] += 1
        # 8자 모양 찾기 (중심점의 특징)
        elif outc == 2 and inc >= 2:
            res[3] += 1
            
    # 도넛 모양 = 생성된 정점에서 나간 총 간선 수 - 나머지 그래프들
    res[1] = counts[res[0]][1] - res[2] - res[3]
    
    return res