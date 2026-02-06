
def fact(num):
    result=1
    for i in range(1, num+1):
        result*=i
    return result

a, b = map(int, input().split())


print(int(fact(a)/fact(b)/fact(a-b)))