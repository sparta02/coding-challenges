N = int(input())
seat = input()

# Please write your code here.
arr=[]
for i in range(N):
    if seat[i]=="1":
        arr.append(i)

#print(arr)

result=0
for k in range(len(arr)):
    if k==0:
        result=max(result, arr[k])
    elif k==(len(arr)-1):
        result=max(result, len(seat)-arr[k]-1)
    else:
        result=max(result, int((arr[k]-arr[k-1])/2))

print(result)