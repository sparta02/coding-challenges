n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
result=0
temp=0
for i in range(len(arr)): 
    if i==0 or arr[i]==arr[i-1]:
        temp+=1
        if result<temp:
            result=temp
    else:
        temp=1


print(result)