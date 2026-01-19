n = int(input())
m = list(map(int, input().split()))

#dp의 조건
# j(앞에 있는 수)가 i(뒤에 있는 수)보다 작으면 된다

dp=[0]*n
dp[0]=0
for i in range(1,n):
    for j in range(i):
        #print(f"i:{i} j:{j}")
        if j+m[j]>=i and dp[j]+1>dp[i]:
            dp[i]=dp[j]+1
    #print(dp)

끝=n-1
for i in range(1, n):
    if dp[i]==0:
        끝=i

print(max(dp[1:끝+1]))