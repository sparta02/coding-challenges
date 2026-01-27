n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
num_hash={}
for n in arr:
    if n in num_hash:
        num_hash[n]+=1
    else:
        num_hash[n]=1

for num in nums:
    print(num_hash.get(num, 0), end=" ")