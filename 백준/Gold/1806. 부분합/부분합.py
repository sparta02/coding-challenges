n, target=map(int, input().split())
arr=list(map(int, input().split()))

i, j=0,0
result=10**6

temp=0
for i in range(n):
    while temp<target and j<n:
        temp+=arr[j]
        j+=1
    
    # print(i, j, temp)
    if temp>=target:
        result=min(result, j-i)
    temp-=arr[i]

print(0 if result==10**6 else result)