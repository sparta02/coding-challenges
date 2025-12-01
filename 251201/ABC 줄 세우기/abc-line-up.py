n = int(input())
arr=list(input().split())

# Please write your code here.
result=0

for i in range(n):
    result+=abs(ord(arr[i]) - (i+1))

print(int(result/2))


# 1 4 3 2
# 1 2 3 4

# 0 2 0 2