A = input()
B = input()
N=len(A)
M=len(B)

dp= [['']*M for _ in range(N)]

if A[0] == B[0]:
    dp[0][0]=A[0]

for i in range(1, M):
    if A[0]==B[i]:
        dp[0][i]=A[0]
    else:
        dp[0][i]=dp[0][i-1]

for i in range(1, N):
    if A[i]==B[0]:
        dp[i][0]=B[0]
    else:
        dp[i][0]=dp[i-1][0]

for i in range(1, N):
    for j in range(1, M):
        if A[i]==B[j]:
            if dp[i-1][j-1]=='':
                dp[i][j]=A[i]
            else:
                dp[i][j]=dp[i-1][j-1]+A[i]


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