n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# dp[n][k]
# 숫자 n까지 고려하고 음수를 k개 넣었을 때
# 최댓값

dp= [ [-99999]*(k+1) for _ in range(n)]

if numbers[0]>=0:
    dp[0][0]=numbers[0]
else:
    dp[0][1]=numbers[0]

def print_grid():
    for i in range(n):
        for j in range(k+1):
            print(dp[i][j], end=" ")
        print()
    print()

for i in range(1, n):
    for j in range(k+1):
        # numbers[i]가 짝수라면
        # 1. 이번 숫자부터 새로 시작하거나
        # 2. 저번 숫자에 이어서 더한다
        if numbers[i]>=0:
            dp[i][j]=max(numbers[i], dp[i-1][j]+numbers[i])
        # numbers[i]가 홀수라면
        # 1. 이번 숫자에 이어서 뺀다
        else:
            if j>=1:
                dp[i][j]=max(dp[i][j], dp[i-1][j-1]+numbers[i])


result=-9999
for i in range(n):
        for j in range(k+1):
            result=max(result, dp[i][j])
print(result)