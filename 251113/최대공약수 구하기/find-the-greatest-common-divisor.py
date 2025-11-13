n, m = map(int, input().split())

# Please write your code here.

def a(n, m):
    min_num = min(n,m)
    result=0
    for i in range(1, min_num+1):
        if n%i==0 and m%i==0:
            result=i
    print(result)

a(n,m)