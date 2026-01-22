n,m = map(int, input().split())
numbers = [0]+ list(map(int, input().split()))

#dp[i][j][0]
#i번째 숫자까지 고려했을 때,
#j개의 구간을 선택했고
#i번째 숫자는 선택하지 않은 경우의 최대 합.

#dp[i][j][1]: i번째 숫자까지 고려했을 때
#j개의 구간을 선택했고
#i번째 숫자가 j번째 구간에 포함된 경우의 최대 합.

dp= [[ [-99999]*2 for _ in range(m+1)] for _ in range(n+1) ]

dp[0][0][0]=0

for i in range(1, n+1):
    for j in range(m+1):
        # dp[i][j][0]
        # i번째 숫자, j개의 구간이 있고 i번째 숫자는 포함 안 시킴
        dp[i][j][0]=max(dp[i-1][j][0], dp[i-1][j][1])

        # dp[i][j][1]
        # i번째 숫자, j개의 구간이 있고 i번째 숫자가 j번째에 포함
        if j>0:
            # 1. 새로운 구간을 선택하는 경우
            if j>=1 and dp[i-1][j-1][0] != -99999:
                dp[i][j][1]=max(dp[i][j][1], dp[i-1][j-1][0]+numbers[i])
            # 2. 기존 구간을 연결하는 경우
            if dp[i-1][j][1] != -99999:
                dp[i][j][1]= max(dp[i][j][1], dp[i-1][j][1]+numbers[i])


def print_dp():
    for i in range(n+1):
        print(f"{i}번째 숫자 고려")
        for j in range(m+1):
            print(f"구간 {j}")
            for k in range(2):
                print(dp[i][j][k], end=" ")
            print()
        print()
    print()

ans = max(dp[n][m][0], dp[n][m][1])
print(ans)