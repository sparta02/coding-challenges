n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# dp[i][j]
# i번째 카드까지 고려했을 때
# 파란카드를 j개 고른다면
# 나올 수 있는 최대 합

dp=[ [0]*(n+1) for _ in range(2*n) ]

def print_dp():
    for i in range(2*n):
        for j in range(n+1):
            print(dp[i][j], end="  ")
        print()
    print()

dp[0][0]=red[0]
dp[0][1]=blue[0]



for i in range(1, 2*n):
    for j in range(n+1):
        # Case A. 빨간카드를 뽑으면
        # dp[i-1][j]
        dp[i][j]=max(dp[i][j], dp[i-1][j]+red[i])
        # Case B. 파란카드를 뽑으면
        # dp[i-1][j-1]
        if j:
            dp[i][j]=max(dp[i][j], dp[i-1][j-1]+blue[i])

# print_dp()

print(dp[-1][-1])