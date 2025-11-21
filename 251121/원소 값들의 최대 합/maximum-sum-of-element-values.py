n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result=0
for i in range(n):
    sum=0
    index=i+1
    #print(f"초기 인덱스: {index}")
    for j in range(m):
        sum+=arr[index-1]
        index=arr[index-1]
        #print(sum, index)
    result=max(result, sum)
print(result)
