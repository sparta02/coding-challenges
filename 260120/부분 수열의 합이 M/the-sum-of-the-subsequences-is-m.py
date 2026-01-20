n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
dp=[999999]*(m+1)
dp[0]=0

for num in A:
    #print(num)
    # num 혼자 m을 초과해버리면 skip
    if m>num:
        # 기존에 가능한 모든 숫자들에 대해
        for i in range(m, 1, -1):
            if num>i:
                continue
            
            if dp[i-num]==999999:
                continue
            #print(i, num)
            dp[i]=min(dp[i], dp[i-num]+1)

    #print(dp)

print(dp[m])