n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
def lower(num):
    left, right = 0, n-1
    lower_bound=n

    while left<=right:
        mid = (left+right)//2
        if num<=arr[mid]:
            lower_bound=min(lower_bound, mid)
            right=mid-1
        else:
            left=mid+1
    return lower_bound

def upper(num):
    left, right = 0, n-1
    upper_bound=n

    while left<=right:
        mid = (left+right)//2
        if num<arr[mid]:
            upper_bound=min(upper_bound, mid)
            right=mid-1
        else:
            left=mid+1
    return upper_bound


for num in queries:
    lower_bound=lower(num)
    upper_bound=upper(num)
    print(upper_bound- lower_bound)