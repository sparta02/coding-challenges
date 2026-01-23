n = int(input())

# dp[i][j][k]

# i번째 날까지 고려했을 때
# B를 연속 J번 받고
# T를 지금까지 k번 받았을 경우의 수

dp= [[[0]*3 for _ in range(3)] for _ in range(n+1)]
dp[0][0][0]=1

def print_dp():
    for i in range(n+1):
        print(f"{i}번째 날")
        for j in range(3):
            
            for k in range(3):
                print(f"B를 {j}번, T 총 {k}번:", end=" ")
                print(dp[i][j][k])
            print()
        print()
    print()

for i in range(1, n+1):
    # B 0번, T 0번
    dp[i][0][0]+=(dp[i-1][0][0]+dp[i-1][1][0]+dp[i-1][2][0])
    
    # B 0번, T 1번
    # G가 나오는 경우
    dp[i][0][1]+=(dp[i-1][0][1]+dp[i-1][1][1]+dp[i-1][2][1])
    # T가 나오는 경우
    dp[i][0][1]+=(dp[i-1][0][0]+dp[i-1][1][0]+dp[i-1][2][0])
    
    # B 0번, T 2번
    # G가 나오는 경우
    dp[i][0][2]+=(dp[i-1][0][2]+dp[i-1][1][2]+dp[i-1][2][2])
    # T가 나오는 경우
    dp[i][0][2]+=(dp[i-1][0][1]+dp[i-1][1][1]+dp[i-1][2][1])

    # B 1번, T 0번
    # G, T가 나오는 경우 - 불가능
    # B가 나오는 경우
    dp[i][1][0]+=(dp[i-1][0][0])

    # B 1번, T 1번
    # G, T가 나오는 경우 - 불가능
    # B가 나오는 경우
    dp[i][1][1]+=(dp[i-1][0][1])

    # B 1번, T 2번
    # G, T가 나오는 경우 - 불가능
    # B가 나오는 경우
    dp[i][1][2]+=(dp[i-1][0][2])

    # B 2번, T 0번
    # G, T가 나오는 경우 - 불가능
    # B가 나오는 경우
    dp[i][2][0]+=(dp[i-1][1][0])

    # B 2번, T 1번
    # G, T가 나오는 경우 - 불가능
    # B가 나오는 경우
    dp[i][2][1]+=(dp[i-1][1][1])

    # B 2번, T 2번
    # G, T가 나오는 경우 - 불가능
    # B가 나오는 경우
    dp[i][2][2]+=(dp[i-1][1][2])

# print_dp()
result=0
for j in range(3):
    for k in range(3):
        result+=dp[-1][j][k]

print(result%(10**9+7))