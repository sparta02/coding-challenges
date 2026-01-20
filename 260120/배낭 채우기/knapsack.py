N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp= [ [0]*(M+1) for _ in range(N) ]
for 보석번호 in range(N):
    for i in range(w[보석번호], M+1):
        dp[보석번호][i]=v[보석번호]


for 보석번호 in range(1, N):
    for i in range(w[보석번호], M+1):
        dp[보석번호][i]=max(dp[보석번호][i], dp[보석번호-1][i], dp[보석번호-1][i-w[보석번호]]+v[보석번호],)


print(dp[-1])