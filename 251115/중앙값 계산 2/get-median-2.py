n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(len(arr)):
    if i%2==0:
        temp_arr=arr[:i+1]
        temp_arr.sort()
        print(temp_arr[int(i/2)], end=" ")