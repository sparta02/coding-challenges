n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result=9999999999999999
for i in range(n):
    arr[i]*=2
    for j in range(n):
        temp_arr=[]
        for k in range(n):
            if j!=k:
                temp_arr.append(arr[k])
        sum=0
        for k in range(n-2):
            sum+=abs(temp_arr[k]-temp_arr[k+1])
        result=min(result, sum)
    arr[i]//=2
print(result)
            