N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
result=999999999999999999999999999999999999999

for i in range(N-H+1):
    temp_arr=arr[i:i+T]
    #print(arr[i:i+T])
    temp=0
    for j in range(T):
        temp+=abs(H-temp_arr[j])
    #print(temp)
    result=min(result, temp)
if N==H:
    result=0
    for i in range(N):
        result+=abs(H-arr[j])
print(result)