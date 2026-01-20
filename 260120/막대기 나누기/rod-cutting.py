n = int(input())
profit = list(map(int, input().split()))
dp=[-1]*(n+1)
dp[0]=0
# Please write your code here.
for num in range(n):
    for i in range(1, n+1):
        if (num+1)>i:
            continue
        dp[i]=max(dp[i], dp[i-num-1]+profit[num])
    #print(dp)
print(dp[-1])