n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.

def lower(num):
    left=0
    right=n-1
    lower_bound=n

    while(left<=right):
        mid = (left+right)//2
        if num<=arr[mid]:
            lower_bound=min(lower_bound,mid)
            right=mid-1
        else:
            left=mid+1
    return lower_bound


for num in query:
    lower_bound=lower(num)
    print(lower_bound)
    if lower_bound==n:
        print(-1)
    elif arr[lower_bound]==num:
        print(lower_bound+1)
    else:
        print(-1)