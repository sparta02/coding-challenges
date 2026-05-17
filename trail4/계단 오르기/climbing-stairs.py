n = int(input())

# Please write your code here.

dp=[0]*(n+1)
dp[0]=1

for i in range(2, n+1):
    dp[i]+=dp[i-2]
    if i>=3:
        dp[i]+=dp[i-3]
print(dp[-1]%10007)