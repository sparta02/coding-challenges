N = int(input())

# Please write your code here.
def a(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    return a(int(n/3))+a(n-1)

print(a(N))