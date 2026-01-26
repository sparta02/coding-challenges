A = input()
B = input()

N=len(A)
M=len(B)

# dp[i][j]
# A는 i번째
# B는 j번째까지 고려
dp= [ [99999999999]*M for _ in range(N)]


dp[0][0]=1 if A[0]==B[0] else 2

for i in range(1, M):
    if A[0]==B[i]:
        dp[0][i]=i+1
    else:
        dp[0][i]=dp[0][i-1]+1

for i in range(1, N):
    if A[i]==B[0]:
        dp[i][0]=i+1
    else:
        dp[i][0]=dp[i-1][0]+1

for i in range(1,N):
    for j in range(1,M):
        # A[i]==B[j]인 경우
        if A[i]==B[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=min(dp[i][j], dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)


def print_dp():
    print(" ", end=" ")
    for i in range(M):
        print(B[i], end=" ")
    print()
    for i in range(N):
        print(A[i], end=" ")
        for j in range(M):
            print(dp[i][j], end=" ")
        print()
    print()

# print_dp()
print(dp[-1][-1])