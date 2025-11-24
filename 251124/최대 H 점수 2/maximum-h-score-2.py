N, L = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort(reverse=True)

#print(arr)
result=0
for i in range(N):
    temp_arr=arr[:]
    for j in range(i+1, min(i+L+1, N)):
        temp_arr[j]+=1
    #print(temp_arr)

    temp=0
    for j in range(N):
        #print(temp_arr[j], j+1)
        if temp_arr[j]<=j+1:
            temp=temp_arr[j]
            break
    #print(temp)
    result=max(result,temp)

print(result)
