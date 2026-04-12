s = int(input())

# Please write your code here.

left=0
right=s
max_idx=-1

while left<=right:
    mid=(left+right)//2
    if int((1+mid)/2*mid)<=s:
        # print(mid, int((1+mid)/2*mid))
        # print()
        max_idx=max(max_idx, mid)
        left=mid+1
    else:
        right=mid-1

print(max_idx)