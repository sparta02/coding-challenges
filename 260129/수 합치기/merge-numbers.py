n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result=0

while (len(arr)>1):
    arr.sort()
    temp_num=arr[0]+arr[1]
    arr.pop(0)
    arr.pop(0)
    arr.append(temp_num)
    result+=temp_num
    #print(arr)

print(result)