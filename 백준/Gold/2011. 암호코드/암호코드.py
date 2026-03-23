import sys
arr=[0]+list(map(int, input()))

n=len(arr)
for i in range(1, n):
    if 1<=arr[i]<=9:
        continue
    if i>=2 and 10<=arr[i-1]*10+arr[i]<=26:
        continue
    print(0)
    sys.exit()


dp=[0]*(n)

dp[0]=1
dp[1]=1
for i in range(2, n):
    

    # 기본적으로 dp[i-1] 가능
    if 1<=arr[i]<=9:
        dp[i]=dp[i-1]%1000000

    #현재 기준에서 앞 숫자 2개를 붙인
    #ab가 다른 알파벳이 될 수 있다면?
    #dp[i-2] 가능
    a,b=arr[i-1],arr[i]
    if 10<=a*10+b<=26:
        dp[i]= (dp[i]+dp[i-2])%1000000
    

print(dp[-1]%1000000)

