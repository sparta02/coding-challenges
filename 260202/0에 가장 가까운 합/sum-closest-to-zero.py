n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

i=0
j=n-1
result=arr[i]+arr[j]

for i in range(n):
    while (j-1>i and arr[i]+arr[j]>0):
        j-=1
    
    if 0<=j<n:
        result=min(result, abs(arr[i]+arr[j]))
      
    if 0<=j+1<n:
        result=min(result, abs(arr[i]+arr[j+1]))
    if i>=j:
        break
if arr[-1]<0:
    result=abs(arr[-1]+arr[-2])
print(result)
      
      
