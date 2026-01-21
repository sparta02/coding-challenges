n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
목표번호=int(sum(arr)/2)
dp=[ [False]*(목표번호+1) for _ in range(n)]

dp[0][0]=True
dp[0][arr[0]] =True

for num in range(1, n):
    dp[num][0]=True
    for i in range(목표번호,0,-1):
        # index: i
        # 몇 번째 숫자: num
        # 해당 숫자: arr[num]
        if arr[num]>i:
            if dp[num-1][i]==True:
                dp[num][i]=True
        else:
            if dp[num-1][i-arr[num]]==True or dp[num-1][i]==True:
                dp[num][i]=True
    
# for i in range(n):
#     for j in range(목표번호+1):
#         print(dp[i][j], end=" ")
#     print()
# print()

result=-999
for i in range(목표번호, -1, -1):
    if dp[-1][i]==True:
        result=i
        break
# print(result)
print(sum(arr)-2*result)