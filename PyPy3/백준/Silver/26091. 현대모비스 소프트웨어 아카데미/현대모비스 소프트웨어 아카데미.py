import sys
input=sys.stdin.readline
n, m = map(int, input().split())
arr=list(map(int,input().split()))

arr.sort(reverse=True)
# print(*arr)

cnt=0

i=-1
j=n-1

while i<j and i<n-2:
    i+=1
    while j<n-1 and i+1<j and arr[i]+arr[j]<m:
        j-=1
    if 0<=i<n and 0<=j<n and i<j and arr[i]+arr[j]>=m:
        # print(i, j)
        cnt+=1
    j-=1

print(cnt)