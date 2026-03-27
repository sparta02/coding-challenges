n, m=map(int, input().split())
arr=list(map(int, input().split()))

# 블루레이의 크기는
# 최소 left부터, 최대 arr중 최대값
left=max(arr)
right=sum(arr)
# print(left, right)
def calc(num):
    cnt=0
    temp=0
    for i in arr:
        # print(f"i:{i}")
        # 이번 숫자를 더해도 num 이하면
        if temp+i <=num:
            temp+=i
            # print(temp)
        else:
            temp=i
            cnt+=1
            # print(temp, cnt)
    if temp:
        cnt+=1
    return cnt


result=99999999
while left<=right:
    mid=(left+right)//2
    temp=calc(mid)
    # print(mid, temp)
    if temp<=m:
        right=mid-1
        result=mid
    else:
        left=mid+1

print(result)
