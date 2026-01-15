def solution(players, m, k):
    answer = 0
    server_list=[0]*400
    
    for i in range(24):
        # 만약 현재 서버로 충당이 불가능하다면
        if players[i]/m >= (server_list[i]+1):
            # k시간 동안 서버 추가
                server_count=int(players[i]/m) - (server_list[i])
                answer+=server_count
                for j in range(i, i+k):
                    server_list[j]+=server_count
    return answer