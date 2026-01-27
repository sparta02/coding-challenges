n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result=0
if max(arr)<0:
    result=max(arr)

temp=-99999999
for i in range(n):
    if temp==-99999999:
        temp=arr[i]
        result=max(result,temp)
        if temp<0:
            temp=-99999999
    else:
        temp+=arr[i]
        result=max(result,temp)
        if temp<0:
            temp=-99999999
    result=max(result,temp)

print(result)