n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]



left =0
right=min(arr)
max_idx=-1

def check_num(num):
    temp=0
    if num!=0:
        for i in arr:
            temp+=i//num
    else:
        temp=10**9
    return temp

while left<=right:
    mid=(left+right)//2
    if check_num(mid)>=m:
        max_idx=max(max_idx, mid)
        left=mid+1
    else:
        right=mid-1

print(max_idx)