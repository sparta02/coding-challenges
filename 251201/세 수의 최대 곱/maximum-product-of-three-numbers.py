from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

comb = list(combinations(arr,3))

result=-99999999999999999999999999999999

for nums in comb:
    result=max(result, nums[0]*nums[1]*nums[2])

print(result)