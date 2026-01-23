n = int(input())
s = [0]
b = [0]
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)



# dp[i][j][k]
# i번째 선수까지 고려하고
# 축구팀을 j명 뽑았고
# 야구팀을 k명 뽑았을 때
# 최대 점수

dp= [[[0]*10 for _ in range(12)] for _ in range(n+1)]

dp[1][1][0]=s[1]
dp[1][0][1]=b[1]


def print_grid():
    for i in range(1, n+1):
        print(f"{i}번째 선수 고려")
        for j in range(12):
            for k in range(10):
                if dp[i][j][k]!=0:
                    print(f"축구부: {j}명, 야구부: {k}명: ", end="")
                    print(dp[i][j][k])
        print()
    print()

for i in range(1, n):
    for j in range(12):
        for k in range(10):
            if dp[i][j][k]==0:
                continue
            #추가 안함
            dp[i+1][j][k]=max(dp[i+1][j][k], dp[i][j][k])
            
            # 축구부 추가
            if j+1<=11:
                dp[i+1][j+1][k]=max(dp[i+1][j+1][k], dp[i][j][k]+s[i+1])
            
            # 야구부 추가
            if k+1<=9:
                dp[i+1][j][k+1] =max(dp[i+1][j][k+1],dp[i][j][k]+b[i+1])

# print_grid()
print(dp[-1][-1][-1])