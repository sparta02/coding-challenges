t= int(input())
for _ in range(t):
    n=int(input())
    stickers=[]
    for _ in range(2):
        temp=list(map(int, input().split()))
        stickers.append(temp)
    if n==1:
        # print(stickers)
        print(max(stickers[0][0], stickers[1][0]))
    else:
        dp=[[-1]*2 for _ in range(n)]
        
        dp[0][0]=stickers[0][0]
        dp[0][1]=stickers[1][0]
        dp[1][0]=stickers[1][0]+stickers[0][1]
        dp[1][1]=stickers[0][0]+stickers[1][1]

        for i in range(2, n):
            for j in range(2):
                dp[i][j]=max(dp[i-1][j^1]+stickers[j][i], dp[i-2][j^1]+stickers[j][i])

        print(max(dp[-1]))
