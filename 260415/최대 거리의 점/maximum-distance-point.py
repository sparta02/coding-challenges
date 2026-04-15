n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 기존
# m개의 점을 선택해서 -> 최단 거리 계산

# NEW
# 최단 거리를 n 이상으로 설정해서
# 몇 개의 점을 선택할 수 있냐

# 최소 거리를 dist로 설정했을 때
# 몇 개의 점을 선택할 수 있나
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