A = input()
B = input()
N=len(A)
M=len(B)

dp= [[0]*M for _ in range(N)]

if A[0] == B[0]:
    dp[0][0]=1

for i in range(1, M):
    if A[0]==B[i]:
        dp[0][i]=1
    else:
        dp[0][i]=dp[0][i-1]

for i in range(1, N):
    if A[i]==B[0]:
        dp[i][0]=1
    else:
        dp[i][0]=dp[i-1][0]

for i in range(1, N):
    for j in range(1, M):
        if A[i]==B[j]:
            dp[i][j]=max(dp[i][j], dp[i-1][j-1]+1)
        else:
            dp[i][j]=max(dp[i][j], dp[i-1][j], dp[i][j-1])


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

# 3. 역추적 (실제 문자열 찾기)
result = []
i, j = N, M
while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        result.append(A[i-1])
        i -= 1
        j -= 1
    else:
        # 더 큰 값을 가진 쪽으로 이동
        if dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
print(result)

print("".join(reverse(result)))