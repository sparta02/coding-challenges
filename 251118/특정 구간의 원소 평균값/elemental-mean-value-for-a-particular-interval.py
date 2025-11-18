n = int(input())
arr = list(map(int, input().split()))

cnt=0

# Please write your code here.
for i in range(n):
    for j in range(i, n):
        temp=0
        temp=int(sum(arr[i:j+1])/len(arr[i:j+1]))
        print(temp, arr[i:j+1])
        if temp in arr[i:j+1]:
            cnt+=1
print(cnt)
