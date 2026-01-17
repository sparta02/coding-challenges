n = int(input())

# Please write your code here.
dp=[-1]*1005

dp[1]=2
dp[2]=7

# Case 1. 1x2 사각형을 추가한다
# dp[i-1] + 1

# Case 2. 1x1 사각형을 2개 추가한다
# dp[i-1] + 1

# Case 3. 2x1 사각형을 2개 추가한다
# dp[i-2] + 1

for i in (3, n+1):
    dp[i]=dp[i-1]*2+dp[i-2]*4

print(dp[n])