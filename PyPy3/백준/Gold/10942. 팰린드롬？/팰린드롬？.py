n=int(input())
arr=list(map(int, input().split()))

m=int(input())
question=[]

for _ in range(m):
    s, e = map(int, input().split())
    question.append((s, e))

#dp[i][j]
# i번째 숫자 기준으로
# 이전 j개의 숫자를 고려했을 때
# 팰린드롬이 맞는지

dp = [ [0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0]=1
    dp[i][1]=1

def print_dp():
    # print("",end="  ")
    # print(*arr)
    for i in range(1, n+1):
        print(arr[i-1], end=" ")
        for j in range(1, n+1):
            print(dp[i][j], end=" ")
        print()
    print()

for i in range(2, n+1):
    for j in range(2, i+1):
        # print(i, j)

        if dp[i-1][j-2]==1 and arr[i-1]==arr[i-j]:
            dp[i][j]=1



# print_dp()

for s, e in question:
    print(dp[e][e-s+1])