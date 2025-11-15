n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
max_num=0
for i in range(n):
    temp=nums[i]+nums[2*n-i-1]
    max_num=max(max_num, temp)
print(max_num)

