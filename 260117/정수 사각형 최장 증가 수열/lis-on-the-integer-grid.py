n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 모든 칸의 정보를 (숫자, 행, 열) 형태로 리스트에 담기
cells = []
for r in range(n):
    for c in range(n):
        cells.append((grid[r][c], r, c))

# 2. 숫자 크기순으로 오름차순 정렬
cells.sort()

# dp[r][c]: (r, c)까지 도달했을 때의 최장 경로 길이
dp = [[1] * n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 3. 작은 숫자가 적힌 칸부터 하나씩 꺼내며 주변 업데이트
# (이 과정이 스택에서 하나씩 꺼내 처리하는 것과 논리적으로 같습니다)
for val, r, c in cells:
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        # 격자 내부에 있고, 다음 칸이 현재 칸보다 숫자가 크다면
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] > grid[r][c]:
                # 다음 칸의 최장거리는 (현재 칸의 최장거리 + 1) 중 최댓값
                dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)

# 4. dp 테이블의 모든 값 중 최댓값 출력
ans = 0
for row in dp:
    ans = max(ans, max(row))

print(ans)