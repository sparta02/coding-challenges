n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

# x1보다 값이 크거나 같은 점 찾기
def x1_points(x1):
    left=0
    right=n-1
    lower_bound=n
    while left<=right:
        mid=(left+right)//2
        if x1<=arr[mid]:
            lower_bound=min(lower_bound, mid)
            right=mid-1
        else:
            left=mid+1
    return lower_bound

# x2보다 값이 작거나 같은 점 찾기
def x2_points(x2):
    left=0
    right=n-1
    lower_bound=-1
    while left<=right:
        mid=(left+right)//2
        if x2>=arr[mid]:
            lower_bound=max(lower_bound, mid)
            left=mid+1
        else:
            right=mid-1
    return lower_bound

for x1, x2 in segments:
    point1=x1_points(x1)
    point2=x2_points(x2)

    #print(point1, point2)
    if point1==n or point2==-1:
        print(0)
    else:
        print(point2-point1+1)