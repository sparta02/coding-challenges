n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

for i in range(1, min(b)):
    temp=i
    체크=1
    for j in range(n):
        temp*=2
        if not a[j]<=temp<=b[j]:
            체크=0
            break
        
    if 체크==1:
        print(i)
        break
