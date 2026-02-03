n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

# Please write your code here.

fires.sort()
stations.sort()

def left_station(target):
    left=0
    right=m-1
    mid_idx=-1

    while left<=right:
        mid=(left+right)//2
        if stations[mid]<=target:
            mid_idx=max(mid_idx, mid)
            left=mid+1
        else:
            right=mid-1
    return mid_idx 

def right_station(target):
    left=0
    right=m-1
    mid_idx=9999999

    while left<=right:
        mid=(left+right)//2
        if target<=stations[mid]:
            mid_idx=min(mid_idx, mid)
            right=mid-1
        else:
            left=mid+1
    return mid_idx 


result=0
for i in range(n):
    left=left_station(fires[i])
    right=right_station(fires[i])
    # print(fires[i])
    # print(left, right)

    if left != -1:
        result=max(result, abs(stations[left]-fires[i]))
    if right !=9999999:
        result=max(result, abs(stations[right]-fires[i]))

print(result)