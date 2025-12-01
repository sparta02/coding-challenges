n = int(input())
arr=list(input().split())

# Please write your code here.
result=0

for i in range(n-1):
    if arr[i]==chr(65+i):
        continue
    실제위치 = arr.index(chr(65+i))
    for j in range(실제위치, i,-1):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        result+=1
print(result)
