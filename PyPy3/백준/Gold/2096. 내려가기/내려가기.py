n=int(input())

dp_best=[]
dp_worst=[]

for i in range(n):
    a, b, c=list(map(int, input().split()))
    if i==0:
        dp_best=[a,b,c]
        dp_worst=[a,b,c]
        # print(dp_best)
        # print(dp_worst)
    else:
        dp_best2=[max(dp_best[0]+a, dp_best[1]+a), max(dp_best[0]+b,dp_best[1]+b,dp_best[2]+b), max(dp_best[1]+c, dp_best[2]+c)]
        dp_worst2=[min(dp_worst[0]+a, dp_worst[1]+a), min(dp_worst[0]+b,dp_worst[1]+b,dp_worst[2]+b), min(dp_worst[1]+c, dp_worst[2]+c)]
        dp_best=dp_best2
        dp_worst=dp_worst2
        # print(dp_best)
        # print(dp_worst)


print(max(dp_best), min(dp_worst))