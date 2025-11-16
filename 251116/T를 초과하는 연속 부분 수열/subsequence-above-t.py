n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# Please write your code here.
result=0
temp=0
for i in range(len(arr)): 
    if arr[i]>t:
        temp+=1
        if result<temp:
            result=temp
    else:
        temp=1
    

print(result)