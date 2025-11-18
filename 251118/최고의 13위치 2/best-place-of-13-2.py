N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# Please write your code here.
max1=0
standard_i=0
standard_j=0
for i in range(N):
    for j in range(N-2):
        if arr[i][j]+arr[i][j+1]+arr[i][j+2]>max1:
            max1=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            standard_i=i
            standard_j=j
if max1!=0:
    arr[standard_i][standard_j]=-9
    arr[standard_i][standard_j+1]=-9
    arr[standard_i][standard_j+2]=-9

max2=-1
#print(arr)
for i in range(N):
    for j in range(N-2):
        if arr[i][j]+arr[i][j+1]+arr[i][j+2]>max2:
            max2=arr[i][j]+arr[i][j+1]+arr[i][j+2]

print(max1+max2)