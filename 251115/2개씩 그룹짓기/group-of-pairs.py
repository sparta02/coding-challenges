n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
a=0
b=0
for i in range(n/2):
    a+=nums[i]
    b+=nums[i+1]
print(max(a,b))