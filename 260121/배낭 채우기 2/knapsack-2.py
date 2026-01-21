N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

dp=[-1]*(M+1)
dp[0]=0

for i in range(N):

    for j in range(1, M+1):
        if w[i]>j:
            continue
        
        if dp[j-w[i]]==-1:
            continue
        dp[j]=max(dp[j], dp[j-w[i]]+v[i])
print(max(dp))