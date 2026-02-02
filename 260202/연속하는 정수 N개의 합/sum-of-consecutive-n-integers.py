n, m = map(int, input().split())
arr = list(map(int, input().split()))

result=0


i, j=0,0

temp_sum=0
for i in range(n):
    # 합이 m 이하일 때까지 더하기
    while j<n and temp_sum+arr[j]<=m:
        temp_sum+=arr[j]
        j+=1
    # 만일 합이 m이라면 result+=1
    if temp_sum==m:
        result+=1
    
    # 다음 cycle로 넘어가기 전에 arr[i] 제외
    temp_sum-=arr[i]

print(result)