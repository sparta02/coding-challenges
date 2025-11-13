n = int(input())

# Please write your code here.

def a(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    sum=sum/10
    return sum

result=a(n)
print(result)

