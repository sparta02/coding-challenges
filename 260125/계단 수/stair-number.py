n = int(input())

# dp[i][j]
# i번째 칸까지 고려하고
# 현재 수가 j일 때
# 가능한 경우의 수

dp= [ [0]*10 for _ in range(n) ]

for i in range(1, 10):
    dp[0][i]=1

for i in range(1, n):
    for j in range(10):
        if j:
            dp[i][j]+=dp[i-1][j-1]
        if j<9:
            dp[i][j]+=dp[i-1][j+1]


# for i in range(n):
#     for j in range(10):
#         print(dp[i][j], end=" ")
#     print()
# print()


print(sum(dp[-1]))