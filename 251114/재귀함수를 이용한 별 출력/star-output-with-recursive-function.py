n = int(input())

# Please write your code here.
stand=n
def a(n):
    if n==0:
        return
    print("*"*(stand-n+1))
    a (n-1)

a(n)
