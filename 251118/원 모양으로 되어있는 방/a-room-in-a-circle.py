n = int(input())
arr = [int(input()) for _ in range(n)]
brr=[0,1,2,3,4]
# arr=[4,7,8,6,4]


min=99999999999999999999999
for i in range(n):
    temp=0
    first=arr.pop(0)
    arr.append(first)
    #print(arr)
    for j in range(n):
        temp+=arr[j]*brr[j]
        #print(arr[j], brr[j], arr[j]*brr[j],temp)
    #print(temp)
    if min>temp:
        min=temp
print(min)