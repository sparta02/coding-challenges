N = int(input())

# Please write your code here.
def a(n):
    if n<=2:
        return n
    return n+a(n-2)
print(a(N))