n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
i=0
j=0
temp_sum=0
result=9999999
for i in range(n):
    while (j<n and temp_sum<s):
        temp_sum+=arr[j]
        j+=1

    print(temp_sum)
    print(i, j)
    
    if temp_sum>=s:
        result=min(result, j-i)
        #print(f"갱신된 결과: {result}")
    temp_sum-=arr[i]

print(result if result!=9999999 else -1)