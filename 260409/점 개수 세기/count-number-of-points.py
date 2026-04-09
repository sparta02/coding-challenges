n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
points.sort()
젤_왼쪽=points[0]
젤_오른쪽=points[-1]

maps_p_to_i={}
maps_i_to_p={}
for i, p in enumerate(points):
    maps_p_to_i[p]=i
    maps_i_to_p[i]=p

# 시작점 이상의 값 중 최초로 나오는 index
def find_a(num):
    left=0
    right=n-1
    min_idx=n
    while left<=right:
        mid=(left+right)//2
        if maps_i_to_p[mid]>=num:
            min_idx=min(min_idx, mid)
            right=mid-1
        else:
            left=mid+1
    return min_idx

# 시작점 이하의 값 중 가장 오른쪽에 있는 index
def find_b(num):
    left=0
    right=n-1
    max_idx=-1
    while left<=right:
        mid=(left+right)//2
        if maps_i_to_p[mid]<=num:
            max_idx=max(max_idx, mid)
            left=mid+1
        else:
            right=mid-1
    return max_idx

for a, b in queries:
    start=find_a(a)
    end=find_b(b)
    # print(start, end)
    if start==n or end==-1:
        print(0)
    else:
        print(end-start+1)