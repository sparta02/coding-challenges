command= list(map(int, input().split()))

command=command[:-1]
n=len(command)
# dp[i][j][k]
# i번째 입력까지 고려했을 때
# j번째 칸에 왼발이 있고
# k번째 칸에 오른발이 있을 때
# 최소로 드는 힘의 값

INF=99999999999
dp = [ [[INF]*5 for _ in range(5)] for _ in range(len(command))]

def print_dp():
    for i in range(n):
        for j in range(5):
            for k in range(5):
                print(dp[i][j][k], end=" ")
            print()
        print()
    print()

dp[0][command[0]][0]=2
dp[0][0][command[0]]=2

for i in range(n-1):
    next=command[i+1]
    # 특정 지점에서 다음 지점을 고려하면
    # (a, b)에서 이동한다치면
    # 왼발을 움직이거나 오른발을 움직이거나
    # 만약 다음 번호 c가 a나 b와 같다면
    # 무조건 번호를 그대로 가져감
    # (1,0)->(1,2) or (2,0)
    # (0,1)-> (2,1) or (0,2)
    # (1,2) -> (1,2)
    for j in range(5):
        for k in range(5):
            if dp[i][j][k]==INF:
                continue
            # 발을 움직이지 않는 경우
            if j==next or k==next:
                dp[i+1][j][k]=min(dp[i+1][j][k], dp[i][j][k]+1)
            else:
                # 왼발을 움직이는 경우
                # CASE1. 왼발이 0에서 움직이는 경우
                if j==0:
                    dp[i+1][next][k]=min(dp[i+1][next][k], dp[i][j][k]+2)
                # CASE2. 왼발이 바로 옆으로 움직이는 경우
                elif abs(j-next)!=2:
                    dp[i+1][next][k]=min(dp[i+1][next][k], dp[i][j][k]+3)
                # CASE3. 왼발이 반대편으로 이동
                else:
                    dp[i+1][next][k]=min(dp[i+1][next][k], dp[i][j][k]+4)
                
                # 오른발을 움직이는 경우
                # CASE1. 오른발이 0에서 움직이는 경우
                if k==0:
                    dp[i+1][j][next]=min(dp[i+1][j][next], dp[i][j][k]+2)
                # CASE2. 왼발이 바로 옆으로 움직이는 경우
                elif abs(k-next)!=2:
                    dp[i+1][j][next]=min(dp[i+1][j][next], dp[i][j][k]+3)
                # CASE3. 왼발이 반대편으로 이동
                else:
                    dp[i+1][j][next]=min(dp[i+1][j][next], dp[i][j][k]+4)


# print_dp()
min_num=INF



for j in range(5):
    for k in range(5):
        min_num=min(min_num, dp[-1][j][k])
print(min_num)