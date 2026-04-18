def solution(land):
    n=len(land)
    dp=[[0]*4 for _ in range(n)]
    dp[0]=land[0][:]
    # print(dp)
    for i in range(1, n):
        for j in range(4):
            for k in range(4):
                if j==k:
                    continue
                dp[i][j]=max(dp[i][j], dp[i-1][k]+land[i][j])

    return max(dp[-1])