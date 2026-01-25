A = "-"+input()
B = "-"+input()
N= len(A)-1
M= len(B)-1
# dp[i][j]
# A 문자열의 i번째 문자열
# B 문자열의 j번째 문자열까지 고려했을 때
# 나올 수 있는 공통 부분 수열의 최대 길이

dp=[ [0]*(M+1) for _ in range(N+1) ]


def print_dp():
    print(f" ", end=" ")
    for i in range(1, M+1):
        print(f"{B[i]}", end=" ")
    print()
    for i in range(1, N+1):
        print(f"{A[i]}", end=" ")
        for j in range(1, M+1):
            print(dp[i][j], end=" ")
        print()
    print()

if A[1]==B[1]:
    dp[1][1]=1

for j in range(2, M+1):
    if A[1]==B[j]:
        dp[1][j]=1
    else:
        dp[1][j]=dp[1][j-1]

for j in range(2, N+1):
    if A[j]==B[1]:
        dp[j][1]=1
    else:
        dp[j][1]=dp[j-1][1]

for i in range(2, N+1):
    for j in range(2, M+1):
        if A[i]==B[j]:
            dp[i][j]=max(dp[i][j], dp[i-1][j-1]+1)
        else:
            dp[i][j]=max(dp[i][j], dp[i-1][j], dp[i][j-1])

# print_dp()
print(dp[-1][-1])
