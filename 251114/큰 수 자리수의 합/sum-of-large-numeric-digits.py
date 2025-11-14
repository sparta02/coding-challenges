a, b, c = map(int, input().split())

# Please write your code here.
def cal(n):
    if n==0:
        return 0
    return n%10 + cal(n//10)

print(cal(a*b*c))