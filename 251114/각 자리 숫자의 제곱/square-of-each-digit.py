N = int(input())

# Please write your code here.

def calc(n):
    if n==0:
        return 0
    return (n%10)**2+calc(n//10)
print(calc(N))