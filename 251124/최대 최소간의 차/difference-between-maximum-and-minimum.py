n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

min_result=999999999999999
for i in range(min(arr), max(arr)+1):
    sum=0
    #print(f"i: {i}")
    for j in arr:
        if j<i:
            sum+=(i-j)
        elif i+k<j:
            sum+=j-(i+k)
    min_result=min(min_result,sum)

print(min_result)