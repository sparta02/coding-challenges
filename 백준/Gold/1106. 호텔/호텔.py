c, n= map(int, input().split())
plan=[]
for _ in range(n):
    cost, customer = map(int, input().split())
    plan.append((cost, customer))    

INF=10**10

# dp[i]: i명이 필요할 때
# 최소한의 인원
dp=[INF]*(1100)

for cost, customer in plan:
    # print(cost, customer)
    dp[customer]=min(dp[customer], cost)
    for i in range(customer, len(dp)):
        if dp[i-customer] != INF:
            dp[i]=min(dp[i], dp[i-customer]+cost)
    # print(dp)

print(min(dp[c:]))


