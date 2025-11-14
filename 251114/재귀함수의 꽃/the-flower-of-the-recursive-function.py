N = int(input())

# Please write your code here.

def a(n):
    if n==0:
        return
    print(n, end=" ")
    a(n-1)
    print(n, end=" ")
a(N)