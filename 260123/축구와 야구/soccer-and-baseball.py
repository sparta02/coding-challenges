n = int(input())
s = [0]
b = [0]
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)



# dp[i][j]
# i번째 선수까지 고려하고
# 축구팀을 j명 뽑았을 때
# 최대 점수

dp= [[0]*12 for _ in range(n+1)]

dp[1][1]=s[1]
dp[1][0]=b[1]

def print_grid():
    for i in range(n+1):
        for j in range(12):
            print(dp[i][j], end=" ")
        print()
    print()

for i in range(1, n):
    for j in range(12):
        if dp[i][j]==0:
            continue
        
        # 축구부 추가
        if j+1<=11:
            dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j]+s[i+1])
        
        # 야구부 추가
        dp[i+1][j] =max(dp[i+1][j],dp[i][j]+b[i+1])

print(dp[-1][-1])