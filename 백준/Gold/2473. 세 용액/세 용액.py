n=int(input())
arr=list(map(int, input().split()))

arr.sort()
# print(arr)

min_dist=99999999999999
answer=[]

for i in range(n-1):
    left=i+1
    right=n-1
    while left<right:
        if abs(min_dist)>abs(arr[left]+arr[i]+arr[right]):
            min_dist=arr[left]+arr[i]+arr[right]
            answer=[arr[i],arr[left],arr[right]]
        if arr[left]+arr[i]+arr[right]<0:
            left+=1
        elif arr[left]+arr[i]+arr[right]>0:
            right-=1
        else:
            answer=[arr[i],arr[left],arr[right]]
            break

print(*answer)