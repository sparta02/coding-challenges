n=int(input())

arr=list(map(int, input().split()))
dp=[1]*n


for i in range(1, n):
    # i번째 숫자 기준
    for j in range(i):
        # 0~i-1숫자와 비교
        if arr[i]>arr[j]:
            dp[i]=max(dp[i], dp[j]+1)

print(max(dp))