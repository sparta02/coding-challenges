n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 필요한 나무의 양: m
# m보다 크거나 같은 나무가 나오는 높이 중
# 가장 큰 값
# upper_bound

def count_trees(num):
    result=0
    for i in range(n):
        result+=max(0, arr[i]-num)
    return result


def find(target):
    left=0
    right=max(arr)
    mid_idx=0

    while(left<=right):
        #print("=========")
        mid=(left+right)//2
        #print(left, right, mid)
        temp=count_trees(mid)
        #print(f"count={temp}")
        if temp>=target:
            mid_idx=max(mid_idx, mid)
            #print(mid_idx)
            left=mid+1
            
        else:
            right=mid-1
    return mid_idx

print(find(m))