n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
def check_stone(check_num):
    temp_arr=[]
    for i, n in enumerate(arr):
        if n<=check_num:
            temp_arr.append(i)
    #print(check_num,temp_arr)
    if 0 not in temp_arr or (n-1) not in temp_arr:
        return False
    for i in range(len(temp_arr)-1):
        dist = temp_arr[i+1] - temp_arr[i]
        #print(temp_arr[i+1], temp_arr[i], dist)
        if dist>k:
            return False
    return True



result=999

for i in range(n, 0,-1):
    if check_stone(i):
        result=min(result, i)

print(result)