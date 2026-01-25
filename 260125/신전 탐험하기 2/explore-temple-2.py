n = int(input())
l, m, r = [], [], []
cost=[]
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)
    cost.append((left,mid,right))

# Please write your code here.

# dp[i][p][j]
# i층까지 가고
# 시작 위치가 p고
# 현재 j 위치 방이라면
# 얻을 수 있는 최대 개수

dp= [[[-9999]*3 for _ in range(3)] for _ in range(n)]

dp[0][0][0]=l[0]
dp[0][1][1]=m[0]
dp[0][2][2]=r[0]

for i in range(1, n-1):
    for p in range(3):
        for j in range(3):

            for p2 in range(3):
                for j2 in range(3):
                    if j==j2:
                        continue
                    if p!=p2:
                        continue
                    # print(p2, j2)
                    dp[i][p][j]=max(dp[i][p][j], dp[i-1][p2][j2]+cost[i][j])

for i in range(n-1, n):
    for p in range(3):
        for j in range(3):
            #print(f"===p:{p}, j:{j}===")
            for p2 in range(3):
                for j2 in range(3):
                    if j==j2:
                        continue
                    if j==p2:
                        continue
                    #print(f"p2:{p2}, j2:{j2}")
                    dp[i][p][j]=max(dp[i][p][j], dp[i-1][p2][j2]+cost[i][j])



# for i in range(1, n):
#     print(f"{i+1}번째 층")
#     for p in range(3):
#         for j in range(3):
#             print(f"시작위치: {p}, 방 번호: {j}: ", end=" ")
#             print(dp[i][p][j])
#         print()
#     print()
# print()

result=0
for i in range(n):
    for p in range(3):
        for j in range(3):
            result=max(result, dp[i][p][j])

print(result)