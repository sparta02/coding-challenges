def solution(n):
    answer = 0
    dp=[0]*(n+1)
    dp[0]=1
    dp[2]=3

    for i in range(4, n+1,2):
        #print(dp[:i-3])
        dp[i]=(dp[i-2]*3)
        dp[i]+=sum(dp[:i-3])*2
        
        dp[i]%=1000000007
    print(dp)
    return dp[-1]