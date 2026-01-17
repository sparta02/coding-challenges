n = int(input())

# dp 테이블 초기화 (n이 1이나 2일 경우를 대비해 넉넉하게 선언)
dp = [0] * (max(n, 2) + 1)

dp[0] = 1 # 아무것도 안 채우는 경우 1가지
dp[1] = 2
dp[2] = 7

MOD = 1000000007

for i in range(3, n + 1):
    # 점화식: dp[i] = 3*dp[i-1] + dp[i-2] - dp[i-3]
    # 파이썬은 음수 나머지도 처리하지만, 안전하게 MOD를 더해줄 수 있습니다.
    dp[i] = (3 * dp[i-1] + dp[i-2] - dp[i-3]) % MOD

print(dp[n])