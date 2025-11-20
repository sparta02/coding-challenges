n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


result=0
for i in range(min(arr)+1, max(arr)):
    temp=0
    for j in range(len(arr)):
        for k in range(j+1, len(arr)):
            #print(arr[j],n,arr[k])
            if i-arr[j] == arr[k]-i:
                temp+=1
    result=max(result, temp)
print(result)
