n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

for _ in range(t):
    temp=d[-1]
    for i in range(n-1):
        d[n-i-1]=d[n-i-2]
    d[0] = u[-1]
    for i in range(n-1):
        u[n-i-1]=u[n-i-2]
    u[0]=temp

for i in u:
    print(i, end=" ")
print()
for i in d:
    print(i, end=" ")
    

# 1 2 3
# 6 5 1

# 1 1 2
# 3 6 5

# 5 1 1
# 2 3 6

# 6 5 1
#  1 2 3