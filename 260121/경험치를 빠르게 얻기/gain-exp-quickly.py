n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
행길이=1000000
dp=[ [-1]*(행길이+1) for _ in range(n)]

dp[0][0]=0
dp[0][quests[0][1]]=quests[0][0]

for i in range(1, n):
    for j in range(행길이, -1, -1):
        if dp[i-1][j]!=-1:
            dp[i][j]=max(dp[i][j], dp[i-1][j])
        
        if j>=quests[i][1] and dp[i-1][j-quests[i][1]]!=-1:
            dp[i][j]=max(dp[i][j], dp[i-1][j-quests[i][1]]+quests[i][0])
    # for i in range(n):
    #     for j in range(행길이):
    #         print(dp[i][j], end=" ")
    #     print()
    # print()

result=-1
for i in range(행길이+1):
    if dp[-1][i]>=m:
        result=i
        break
print(result)
