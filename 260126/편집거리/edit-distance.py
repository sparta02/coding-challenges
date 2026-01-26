A = input()
B = input()
N=len(A)
M=len(B)

# dp[i][j]
# 문자열 A의 i번째와
# 문자열 B의 j번째까지 고려했을 때
# 최소 편집거리

dp= [[99]*len(B) for _ in range(len(A))]

def print_dp():
    print(" ", end=" ")
    for i in range(N):
        print(B[i], end=" ")
    print()
    for i in range(N):
        print(A[i], end=" ")
        for j in range(M):
            print(dp[i][j], end=" ")
        print()
    print()

if A[0]==B[0]:
    dp[0][0]=0
else:
    dp[0][0]=1

for i in range(1, M):
    if A[0]==B[i]:
        dp[0][i]=i
    else:
        dp[0][i]=dp[0][i-1]+1

for i in range(1, N):
    if A[i]==B[0]:
        dp[i][0]=i
    else:
        dp[i][0]=dp[i-1][0]+1

for i in range(1,N):
    for j in range(1,M):
        # A[i], B[j]가 같은 경우
        if A[i]==B[j]:
            dp[i][j]=min(dp[i-1][j-1],dp[i][j])
        else:
            # 하나의 문자 삽입
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
            # 특정 문자 삭제
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
            # 특정 문자를 다른 문자로 바꾸기
            dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)


# print_dp()
print(dp[-1][-1])