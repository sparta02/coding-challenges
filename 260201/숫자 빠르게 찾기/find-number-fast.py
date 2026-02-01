n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.

def find_num(num):
    left=0
    right=n-1
    while(left<=right):
        mid= int((right+left)/2)
        if num<arr[mid]:
            right=mid-1
        elif num>arr[mid]:
            left=mid+1
        elif num==arr[mid]:
            return mid+1
    return -1

# print(find_num(2))
for num in queries:
    print(find_num(num))
