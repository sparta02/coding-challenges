n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def calc_how_many(dist):
    cnt=0
    left=-dist
    for start, end in segments:
        left=max(left+dist, start)
        # print(f"left:{left}")
        if left<=end:
            cnt+=(end-left)//dist
            cnt+=1
        # print(cnt)
        left+=(end-left)//dist*dist
    return cnt

left=1
right=10**18+1
max_idx=0

while left<=right:
    mid=(left+right)//2
    if calc_how_many(mid)>=n:
        max_idx=max(max_idx, mid)
        left=mid+1
    else:
        right=mid-1
print(max_idx)
