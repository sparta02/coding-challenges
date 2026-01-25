n, k = map(int, input().split())
str = input()

# dp[i][j][k]
# i번째 수정까지 고려하고
# j번 이동하고
# 현재 k(L또는R)에 있을 때
# 최대 점수
dp=[ [[-999]*(2) for _ in range(k+1)] for j in range(n) ]
if str[0]=="L":
    dp[0][0][0]=1
    dp[0][1][1]=1
else:
    dp[0][0][1]=1
    dp[0][1][0]=1

def print_dp():
    for i in range(n):
        print(f"{i+1}번째 수정")
        for j in range(k+1):
            for p in range(2):
                print(f"{j}번 이동하고 현재 {p}: " , end=" ")
                print(dp[i][j][p])
        print()
    print()

for i in range(1, n):
    for j in range(k+1):
        # 현재 칸이 L이든, R이든 상관없이
        # dp[i][j][현재위치]+str의 현재위치가 같다면 1
        # dp[i][j-1][다른위치]
        for p in range(2):
            # 움직이지 않는 경우
            dp[i][j][p]=max(dp[i-1][j][p]+ (1 if (str[i]=="L" and p==0) or (str[i]=="R" and p==1) else 0), dp[i][j][p])

            # 움직이는 경우
            # 현재 위치가 0이면
            if j>=1:
                if p==0:
                    dp[i][j][p]=max(dp[i-1][j-1][1]+(1 if str[i]=="L" else 0), dp[i][j][p])
                # 현재 위치가 1이면
                elif p==1:
                    dp[i][j][p]=max(dp[i-1][j-1][0]+(1 if str[i]=="R" else 0), dp[i][j][p])

# print_dp()
result=0
for i in range(k+1):
    for j in range(2):
        result=max(result, dp[-1][i][j])
print(result)
