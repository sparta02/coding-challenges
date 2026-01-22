n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))

# 할 수 있는 행동
# 1. 카드 비교하기 (작으면 득점 후 버리기, 같으면 둘 다 버리기)
# 2. 둘 다 버리기

# dp[i][j]
# 남우가 i, 상대방이 j번째 카드를 들고 있을 때
# 가질 수 있는 최고 점수

dp= [ [-1]*(n+1) for _ in range(n+1) ]

def print_grid():
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(dp[i][j], end=" ")
        print()
    print()

dp[0][0]=0
for i in range(1, n+1):
    dp[0][i]=0

for i in range(1, n+1):
    for j in range(n+1):
        temp1, temp2, temp3=-1,-1,-1
        # 카드를 2장 다 버리는 경우
        # dp[i-1][j-1]
        if i>=1 and j>=1:
            temp1=dp[i-1][j-1]

        # 싸워서 내가 점수를 얻는 경우
        # second_cards[i-1] < first_cards[j]를 만족하면
        # dp[i-1][j] + second_cards[i-1]
        if i>=1 and j<n and second_cards[i-1] < first_cards[j]:
            temp2=dp[i-1][j] + second_cards[i-1]

        # 싸워서 상대방에게 점수를 주는 경우
        # second_cards[i] > first_cards[j-1]를 만족하면
        # dp[i][j-1]
        if j>=1 and i<n and second_cards[i] > first_cards[j-1]:
            temp3=dp[i][j-1]
        
        dp[i][j]=max(temp1, temp2, temp3)

# print_grid()

print(max(max(dp[-1]), max(x[-1] for x in dp)))