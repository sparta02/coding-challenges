n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr=[0]*(100002)

for a, b in point:
    arr[a]+=1
    arr[b+1]-=1

result=0
curr=0
for i in range(100002):
    curr+=arr[i]
    result=max(result, curr)
print(result)