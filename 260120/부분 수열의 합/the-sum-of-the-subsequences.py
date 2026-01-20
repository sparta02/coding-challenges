n, m = map(int, input().split())
A = list(map(int, input().split()))

dp=[-1]*(m+1)
dp[0]=0
# Please write your code here.
for cost in A:
    if cost>m:
        continue
    for i in range(m, 0, -1):
        if cost>i:
            continue
        if dp[i-cost]==-1:
            continue
        dp[i]=dp[i-cost]+1
    #print(dp)
        
if dp[-1]==-1:
    print("No")
else:
    print("Yes")