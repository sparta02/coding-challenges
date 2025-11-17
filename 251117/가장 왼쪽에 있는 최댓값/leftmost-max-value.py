n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

while True:
    #print(arr)

    max_index=0
    for i in range(len(arr)):
        if arr[max_index]<arr[i]:
            max_index=i
    print(max_index+1)
    if max_index==0:
        break
    arr=arr[:max_index]
    