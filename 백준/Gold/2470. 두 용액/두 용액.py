n=int(input())
arr=list(map(int, input().split()))
arr.sort()
# print(arr)

result=999999999999999999999
result_list=[]
i=0
j=n-1

while i<j:
    temp=arr[i]+arr[j]
    # print(i, j, temp)
    if result>abs(temp):
        result=abs(temp)
        result_list=[arr[i], arr[j]]
    if temp<0:
        i+=1
    elif temp>0:
        j-=1
    else:
        break

print(*result_list)