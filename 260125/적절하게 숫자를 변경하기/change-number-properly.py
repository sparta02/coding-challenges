import sys

# 1. 입력 받기
input = sys.stdin.read().split()
if not input:
    exit()

N = int(input[0])
M = int(input[1])
# 수열을 0~3 범위로 조정 (1,2,3,4 -> 0,1,2,3)
target = [int(x) - 1 for x in input[2:]]

# 2. DP 테이블 초기화
# dp[i][j][k]: i번째 위치에서 숫자 j를 선택했고, 인접한 숫자가 달랐던 횟수가 k번일 때의 최대 유사도
# 도달할 수 없는 상태는 -1로 설정
dp = [[[-1] * (M + 1) for _ in range(4)] for _ in range(N)]

# 3. 첫 번째 숫자 처리 (i = 0)
for j in range(4):
    # 첫 번째 숫자는 이전 숫자가 없으므로 변경 횟수(k)는 항상 0
    score = 1 if j == target[0] else 0
    dp[0][j][0] = score

# 4. DP 전이 (i = 1 ~ N-1)
for i in range(1, N):
    for curr in range(4): # 현재 선택할 숫자
        score = 1 if curr == target[i] else 0
        
        for prev in range(4): # 직전 숫자
            for k in range(M + 1): # 직전까지의 변경 횟수
                if dp[i-1][prev][k] == -1:
                    continue
                
                # 다음 변경 횟수 계산
                next_k = k if curr == prev else k + 1
                
                # 변경 횟수가 제한(M)을 넘지 않을 때만 갱신
                if next_k <= M:
                    if dp[i][curr][next_k] < dp[i-1][prev][k] + score:
                        dp[i][curr][next_k] = dp[i-1][prev][k] + score

# 5. 최종 결과 도출
# 마지막 위치(N-1)에서 모든 숫자(j)와 모든 변경 횟수(k) 중 최댓값 탐색
ans = 0
for j in range(4):
    for k in range(M + 1):
        if dp[N-1][j][k] > ans:
            ans = dp[N-1][j][k]

print(ans)