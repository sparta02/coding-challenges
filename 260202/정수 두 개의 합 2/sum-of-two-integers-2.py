n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()

result=0

def find_num(num):
    #print(f"{num}이하인 수 중 가장 오른쪽")
    left=0
    right=n-1
    min_index=-1

    while(left<=right):
        mid = (left+right)//2
        if arr[mid]<=num:
            min_index=max(min_index, mid)
            left=mid+1
        else:
            right=mid-1
    return min_index

for i in range(n):
    if arr[i]>=k:
        break
    #k-arr[i] 이하인 수들 중 가장 오른쪽에 있는 수
    j=find_num(k-arr[i])
    #print(j)
    if j!=0 and i<j:
        result+=(j-i)

print(result)