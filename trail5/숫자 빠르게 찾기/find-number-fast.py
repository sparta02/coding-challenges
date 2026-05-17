n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
def search(target):
    left=0
    right=n-1
    min_idx=n

    while left<=right:
        mid=(left+right)//2
        if target<=arr[mid]:
            right=mid-1
            min_idx=min(min_idx, mid)
        else:
            left=mid+1
    return min_idx

for num in queries:
    temp=search(num)
    if temp==n or arr[temp]!=num:
        print(-1)
    else:
        print(temp+1)