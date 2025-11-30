N = int(input())

# Please write your code here.


temp_list=[-1]*100


def fib(num):
    if temp_list[num] !=-1:
        return temp_list[num]

    if num==1 or num==2:
        temp_list[num]=1
    else:
        temp_list[num]=fib(num-1)+fib(num-2)

fib(N)
print(temp_list[N])