n = int(input())
arr_1 = list(map(int, input().split()))

# 왼쪽 -> 오른쪽
# dp_1[i]는 오름차순으로 나올 수 있는
# 배열의 가장 긴 길이
dp_1=[1]*(n)

# 오른쪽 -> 왼쪽
# dp_2[i]는 내림차순으로 나올 수 있는
# 배열의 가장 긴 길이
dp_2=[1]*(n)
arr_2=arr_1[::-1]

def set_dp(arr, dp):
    # i번째 원소 테스트
    for i in range(1, n):
        for k in range(i):
            if arr[k]<arr[i]:
                dp[i]=max(dp[i], dp[k]+1)

set_dp(arr_1, dp_1)
set_dp(arr_2, dp_2)
dp_2=dp_2[::-1]
# print(dp_1)
# print(dp_2)

result=0

for i in range(n):
    result=max(result, dp_1[i]+dp_2[i]-1)
print(result)
