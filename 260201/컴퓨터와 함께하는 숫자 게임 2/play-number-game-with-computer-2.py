m = int(input())
a, b = map(int, input().split())

# Please write your code here.
def count_game(target):
    left=1
    right=m
    counts=0
    while left<=right:
        counts+=1
        mid= (left+right)//2

        if target==mid:
            return counts
        elif target < mid:
            right=mid-1
        else:
            left=mid+1

low=999999999999
high=0
for i in range(a, b+1):
    counts=count_game(i)
    low=min(low, counts)
    high=max(high, counts)
    # print(counts)
print(low, high)