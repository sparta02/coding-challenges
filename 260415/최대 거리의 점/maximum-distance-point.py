n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

def calc_points(dist):
    temp=0
    cnt=1
    for i in range(n-1):
        temp+=arr[i+1]-arr[i]
        if temp>=dist:
            cnt+=1
            temp=0
    
    return cnt

left=1
right=10**9
max_idx=0

while left<=right:
    mid=(left+right)//2
    if calc_points(mid)>=m:
        max_idx=max(max_idx, mid)
        left=mid+1
    else:
        right=mid-1

print(max_idx)