n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

def calc_how_many(time):
    temp=0
    for num in arr:
        temp+=time//num
    return temp

left=0
right=10**15
min_idx=10**15+1

while left<=right:
    mid=(left+right)//2
    if calc_how_many(mid)>=n:
        min_idx=min(min_idx, mid)
        right=mid-1
    else:
        left=mid+1
print(min_idx)