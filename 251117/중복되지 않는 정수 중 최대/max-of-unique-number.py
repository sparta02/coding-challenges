n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

arr=[0]*1001

for num in nums:
    arr[num]+=1

max=-1
for i in range(1001):
    if arr[i]==1:
        max=i
print(max)