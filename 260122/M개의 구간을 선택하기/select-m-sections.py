import sys

# 입력을 sys.stdin.readline으로 받으면 더 빠릅니다.
n, m = map(int, sys.stdin.readline().split())
numbers = [0] + list(map(int, sys.stdin.readline().split()))

# 1. 초기값을 아주 작은 값으로 (음수 합 고려)
INF = float('inf')
dp = [[[-INF] * 2 for _ in range(m + 1)] for _ in range(n + 1)]

# 2. 시작점 설정
dp[0][0][0] = 0

for i in range(1, n + 1):
    for j in range(m + 1):
        # [현재 숫자를 포함하지 않는 경우]
        # 이전 숫자까지 j개를 완성했거나(dp[i-1][j][0]), 
        # 이전 숫자가 포함된 상태로 j개를 완성했거나(dp[i-1][j][1])
        # 둘 중 큰 값을 가져옵니다.
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])

        # [현재 숫자를 포함하는 경우]
        if j > 0:
            # 1. 새 구간 시작: 직전 숫자는 반드시 포함되지 않았어야 함 (dp[i-1][j-1][0])
            if dp[i-1][j-1][0] != -INF:
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][0] + numbers[i])
            
            # 2. 기존 구간 연장: 직전 숫자가 이미 j번째 구간에 포함되어 있어야 함 (dp[i-1][j][1])
            if dp[i-1][j][1] != -INF:
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1] + numbers[i])

# 결과 출력
ans = max(dp[n][m][0], dp[n][m][1])
print(ans)