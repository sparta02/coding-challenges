n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

# O(n)
sum_arr=arr[-1]
min_num=arr[-1]
result=0

# O(n)
for k in range(n-2, 0, -1):
    # O(1)
    sum_arr+=arr[k]
    if min_num>arr[k]:
        min_num=arr[k]

    #print((sum_arr-min_num)/(n-k-1))
    result=max(result, (sum_arr-min_num)/(n-k-1))

print(f"{result:.2f}")
