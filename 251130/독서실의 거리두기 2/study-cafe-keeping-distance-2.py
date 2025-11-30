N = int(input())
seats = input()

# Please write your code here.

def check_dist(arr_temp):
    result=9999999999999
    current=-1
    for i in range(N):
        if arr_temp[i]=='1' :
            # print(i, current)
            if current ==-1:
                current=i
            else:
                result=min(result, i-current)
                current=i
    return result


arr=list(seats)

결과=0
for i in range(N):
    if arr[i]=='1':
        continue
    arr_temp=arr[:]
    arr_temp[i]='1'
    # print(arr_temp)
    # print(check_dist(arr_temp))
    결과=max(결과, check_dist(arr_temp))

print(결과)