n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
for i in nums.sort():
    print(i, end=" ")

for i in nums.sort(reverse=True):
    print(i, end=" ")