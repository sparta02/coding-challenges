a = list(map(int, input().split()))

# Please write your code here.

a.sort()

if a[1]-a[0]==1 and a[2]-a[1]==1:
    print(0)
else:
    print(max(a[1]-a[0]-1, a[2]-a[1]-1))

# 1 0 0 0 1 1
# 1 0 0 1 1 0
# 1 0 1 1 0 0
# 1 1 1 0 0 0 