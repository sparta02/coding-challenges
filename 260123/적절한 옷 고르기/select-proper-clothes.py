N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.

# dp[i][j]
# i번째 날까지 고려했을 때
# 마지막에 입은 옷이 j인 경우
# 만족도의 값

dp= [ [-99999]*N for _ in range(M+1)]

def print_grid():
    for i in range(M+1):
        for j in range(N):
            print(dp[i][j], end=" ")
        print()
    print()

for i in range(N):
    if s[i]==1:
        dp[1][i]=0

for i in range(2, M+1):
    for j in range(N):
        # i번째 날
        # 현재 입은 옷이 j라면

        # 오늘 못 입는 날이면 skip
        if i<s[j] or e[j]<i:
            continue
        
        # 전체 옷들과 비교
        for k in range(N):
            dp[i][j]=max(dp[i][j], dp[i-1][k]+ abs(v[k]-v[j]))


# print_grid()
print(max(dp[-1]))