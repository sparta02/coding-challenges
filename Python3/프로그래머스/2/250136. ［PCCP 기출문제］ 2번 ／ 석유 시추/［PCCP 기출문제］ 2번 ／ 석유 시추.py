def solution(land):
    n = len(land)
    m = len(land[0])
    
    # 1. 방문 여부를 체크할 배열 (딱 한 번만 생성)
    visited = [[False] * m for _ in range(n)]
    # 2. 각 열별 최종 석유량을 저장할 리스트
    result = [0] * m
    
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            # 기름이 있고 아직 방문하지 않은 새로운 덩어리 발견!
            if land[i][j] == 1 and not visited[i][j]:
                # --- 반복문 DFS (Stack 방식) ---
                stack = [(i, j)]
                visited[i][j] = True
                
                oil_size = 0  # 덩어리 크기
                columns_touched = set()  # 이 덩어리가 지나는 열 번호들
                
                while stack:
                    cx, cy = stack.pop()
                    oil_size += 1
                    columns_touched.add(cy) # 어느 열을 지나는지 기록
                    
                    for k in range(4):
                        nx, ny = cx + dx[k], cy + dy[k]
                        
                        # 인덱스 범위 확인 및 방문 여부/기름 존재 확인
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and land[nx][ny] == 1:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                
                # --- 덩어리 탐색 종료 후 ---
                # 이 덩어리가 걸쳐 있는 모든 열(column)에 덩어리 크기를 더해줌
                for col in columns_touched:
                    result[col] += oil_size
                    
    # 모든 열 중 가장 큰 값 반환
    return max(result)