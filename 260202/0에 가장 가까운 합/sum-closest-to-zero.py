n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

i=0
j=n-1
result=99999999

for i in range(n):
    while (j>=0 and arr[i]+arr[j]>0):
        j-=1
    if 0<=j<n:
        result=min(result, abs(arr[i]+arr[j]))
      
    if 0<=j+1<n:
        result=min(result, abs(arr[i]+arr[j+1]))
    
    if i>j:
        break
print(result)
      
      
