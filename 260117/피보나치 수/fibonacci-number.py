n = int(input())

# Please write your code here.


memo =[-1]*50


def fibo(num):
    if memo[num]!=-1:
        return memo[num]

    if num==1:
        memo[num]=1
    elif num==2:
        memo[num]=1
    else:
        memo[num]=fib(num-1)+fib(num-2)
    #print(memo)
    return memo[num]

print(fibo(n))