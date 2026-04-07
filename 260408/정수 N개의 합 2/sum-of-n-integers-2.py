n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
prefix_sum=[0, arr[0]]

for num in arr[1:]:
    prefix_sum.append(num+prefix_sum[-1])
# print(prefix_sum)
result=-99999999999999999
for i in range(n-k+1):
    a=i
    b=i+k
    result=max(result, prefix_sum[b]-prefix_sum[a])

print(result)
# i부터 j번째까지 합:
# prefix_sum[j+1]-prefix_sum[i]
